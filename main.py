# -*- encoding: utf-8 -*-
from bs4 import BeautifulSoup
import aiohttp
import asyncio
import async_timeout
import time
from abc import ABCMeta
from selenium import webdriver
import re
import os
from selenium.webdriver.common.keys import Keys
from PIL import Image
from json import JSONEncoder

class Page():
	__metaclass__ = ABCMeta
	def __init__(self, link, dir_screenshots="screenshots/", dir_results="results/"):
		self.link = link
		self.dir_screenshots = dir_screenshots
		self._prepare_folder(self.dir_screenshots)
		self.dir_results= dir_results
		self._prepare_folder(self.dir_results);
	#Selenium
	def StartDriver(self):
		driver = webdriver.Chrome()
		driver.get(self.link)
		self.driver = driver
		time.sleep(1)
	def DriverFind(self,css,save='last',many=False,root=False):
		if not root:
			root = self.driver
		elements = root.find_elements_by_css_selector(css)
		if many:
			for element in elements:
				self.ScreenShot(element,save+'['+str(k)+']')
			return elements
		self.ScreenShot(elements[0],save)
		return elements[0]
	def Type(self,element, text, ENTER=False, save='last'):
		element.send_keys(text)
		time.sleep(1)
		self.ScreenShot(element,save)
		if ENTER:
			element.send_keys(Keys.ENTER)
		time.sleep(1)
	def ScreenShot(self,element,name):
		self.driver.save_screenshot(self.dir_screenshots+name+"_full.jpg")
		location = element.location
		size = element.size
		im = Image.open(self.dir_screenshots+name+"_full.jpg")
		left = location['x']
		top = location['y']
		right = location['x'] + size['width']
		bottom = location['y'] + size['height']
		im = im.crop((left, top, right, bottom))
		im.save(self.dir_screenshots+name+'.jpg')
	def FinishDriver(self):
		time.sleep(5)
		self.driver.close()
	#BeautifulSoap
	def GetHtml(self,link,type='web'):
		if type == 'file':
			return open(link,'r', encoding='utf8').read()
		elif type == 'driver':
			return self.driver.page_source
		loop = asyncio.get_event_loop()
		return loop.run_until_complete(self._get_html(loop,link))
	def StartBs(self, HTML):
		self.bs = BeautifulSoup(HTML, "html.parser")
	def BsFind(self, tag, attributes = {},many=False, root=False):
		if not root:
			root = self.bs
		found = root.findAll(tag,attributes)
		if many:
			return found
		if len(found)>0:
			return found[0]
		return False
	# General methods
	def push(self,array=[],fields=[],elements=[]):
		obj = {}
		for f,v in zip(fields,elements):
			try:
				obj[f]=v.get_text()
			except AttributeError:
				pass
		array.append(obj)
		return array
	def save(self,type,name,elements):
		if type=='json':
			self._save_json(self.dir_results+name,elements)

	# protected level
	def _save_json(self,name,elements):
		jsonString = JSONEncoder(ensure_ascii = False).encode(elements)
		f = open(name+'.json', 'w', encoding='utf8')
		f.write(jsonString)

	def _prepare_folder(self,path):
		if not os.path.isdir(path):
			os.makedirs(path)
	async def _fetch(self,session, url):
		with async_timeout.timeout(10):
			async with session.get(url) as response:
				return await response.text()
	async def _get_html(self,loop,url):
		async with aiohttp.ClientSession(loop=loop) as session:
			html = await self.fetch(session, url)
			return html