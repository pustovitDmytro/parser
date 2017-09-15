import main

url="https://www.google.com.ua/"
page="html/google.example.page"
query = 'REQUEST'

class MainPage(main.Page):
	def __init__(self, link):
		super(MainPage,self).__init__(link)
	def GetLinks(self):
		self.StartDriver()
		input = self.DriverFind('input[type="text"]')
		self.Type(input,query,True)
		Html = self.GetHtml(page, type='driver')
		self.FinishDriver()
		#Html = self.GetHtml(page,type='file')
		self.StartBs(Html);
		blocks = self.BsFind('div',{'class':'g'}, many=True)
		arr=[]
		for block in blocks:
			title = self.BsFind('h3',root=block);
			link = self.BsFind('cite',root=block);
			arr = self.push(arr,['title','link'],[title,link])
		self.save('json','results',arr)


def main():
	page = MainPage(url)
	page.GetLinks()

if __name__ == '__main__':
    main()