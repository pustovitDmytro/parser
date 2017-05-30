# -*- encoding: utf-8 -*-
from bs4 import BeautifulSoup
import aiohttp
import asyncio
import async_timeout
import time
from abc import ABCMeta
from selenium import webdriver
import re

BaseUrl =""
TestUrl = "test/"

def main():
	print("main")

class Page():
	__metaclass__ = ABCMeta
	def __init__(self, link):
		self.link = link
	def StartDriver(self):
		driver = webdriver.Firefox()
		driver.get(self.link)
		self.driver = driver
	def FinishDriver(self):
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

class MainPage(Page):
	def __init__(self, link, test=False):
		super(MainPage,self).__init__(link)
if __name__ == '__main__':
    main()