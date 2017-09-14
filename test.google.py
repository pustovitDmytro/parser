import main

url ="http://google.com.ua"
html="https://www.google.com.ua/"

class MainPage(main.Page):
	def __init__(self, link, test=False):
		super(MainPage,self).__init__(link)
	def GetLinks(self):
		self.StartDriver()
		input = self.FindCss('input[type="text"]')
		self.Type(input,'REQUEST',True)
		self.FinishDriver()


def main():
	page = MainPage(url)
	page.GetLinks()

if __name__ == '__main__':
    main()