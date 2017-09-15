# -*- encoding: utf-8 -*-
from bs4 import BeautifulSoup
import aiohttp
import asyncio
import async_timeout
import time
from abc import ABCMeta
from selenium import webdriver
import re
from selenium.webdriver.common.keys import Keys
from PIL import Image

dir_screenshots="screenshots/"
dir_results="results/"

class Page():
	__metaclass__ = ABCMeta
	def __init__(self, link):
		self.link = link
	def StartDriver(self):
		driver = webdriver.Chrome()
		driver.get(self.link)
		self.driver = driver
		time.sleep(1)
	def FindCss(self,css,save='last',many=false):
		elements = self.driver.find_elements_by_css_selector(css)
		for element in elements
			self.ScreenShot(element,save)
		time.sleep(1)
		return element
	def Type(self,element, text, ENTER=False, save='last'):
		element.send_keys(text)
		time.sleep(1)
		self.ScreenShot(element,save)
		if ENTER:
			element.send_keys(Keys.ENTER)
		time.sleep(1)
	def ScreenShot(self,element,name):
		self.driver.save_screenshot(dir_screenshots+name+"full.jpg")
		location = element.location
		size = element.size
		im = Image.open(dir_screenshots+name+"full.jpeg")
		left = location['x']
		top = location['y']
		right = location['x'] + size['width']
		bottom = location['y'] + size['height']
		im = im.crop((left, top, right, bottom))
		im.save(dir_screenshots+name+'.jpg')
	def FinishDriver(self):
		time.sleep(5)
		self.driver.close()
	def GetHtml(self):
		loop = asyncio.get_event_loop()
		return loop.run_until_complete(self._get_html(loop,self._link))
	def StartBS(self, HTML)
		self.bs = BeautifulSoup(HTML, "html.parser")
	async def _fetch(self,session, url):
		with async_timeout.timeout(10):
			async with session.get(url) as response:
				return await response.text()
	async def _get_html(self,loop,url):
		async with aiohttp.ClientSession(loop=loop) as session:
			html = await self.fetch(session, url)
			return html