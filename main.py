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

class Page():
	__metaclass__ = ABCMeta
	def __init__(self, link):
		self.link = link
	def StartDriver(self):
		driver = webdriver.Chrome()
		driver.get(self.link)
		self.driver = driver
		time.sleep(1)
	def FindCss(self,css,save='last'):
		element = self.driver.find_element_by_css_selector(css)
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
		self.driver.save_screenshot(dir_screenshots+name)
		location = element.location
		size = element.size
		im = Image.open(dir_screenshots+name)
		left = location['x']
		top = location['y']
		right = location['x'] + size['width']
		bottom = location['y'] + size['height']
		im = im.crop((left, top, right, bottom))
		im.save(dir_screenshots+name+'.jpg')
	def FinishDriver(self):
		time.sleep(5)
		self.driver.close()
	def StartBS(self, test):
		loop = asyncio.get_event_loop()
		HTML = open(self._link,'r').read() if test else loop.run_until_complete(self.get_html(loop,self._link))
		bs = BeautifulSoup(HTML, "html.parser")
	async def fetch(self,session, url):
		with async_timeout.timeout(10):
			async with session.get(url) as response:
				return await response.text()
	async def get_html(self,loop,url):
		async with aiohttp.ClientSession(loop=loop) as session:
			html = await self.fetch(session, url)
			return html