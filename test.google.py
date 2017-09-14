import main

url ="http://google.com.ua"
html="https://www.google.com.ua/"

class MainPage(main.Page):
	def __init__(self, link, test=False):
		super(MainPage,self).__init__(link)

page = MainPage(url)
page.StartDriver()

