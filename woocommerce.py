from bs4 import BeautifulSoup
from urllib2 import urlopen
 
filename = 'woocommerce.csv'
f = open(filename,'w')
headers = 'title,info,price\n'
f.write(headers)

block=[]

i=0
while i<32:

	i=i+1
	html = urlopen('https://woocommerce.com/product-category/woocommerce-extensions/page/'+ str(i) + '/' ).read()
	soup = BeautifulSoup(html,'lxml')

	for conteiners in soup.find_all('li',{'class', 'product'}):

		title=conteiners.find('h3').text.encode('utf-8')

		info=conteiners.find('p').text.encode('utf-8')

		zp=conteiners.find_all('span')[2].text.encode('utf-8')

		f.write(title.replace(',',' ').replace('\n',' ') + ',' + info.replace(',',' ').replace('\n',' ') + ',' + zp.replace(',',' ').replace('\n',' ') + '\n')

	for conteiners in soup.find_all('li',{'class', 'product first'}):

		title=conteiners.find('h3').text.encode('utf-8')

		info=conteiners.find('p').text.encode('utf-8')

		zp=conteiners.find_all('span')[2].text.encode('utf-8')

		f.write(title.replace(',',' ').replace('\n',' ') + ',' + info.replace(',',' ').replace('\n',' ') + ',' + zp.replace(',',' ').replace('\n',' ') + '\n')

	for conteiners in soup.find_all('li',{'class', 'product last'}):

		title=conteiners.find('h3').text.encode('utf-8')

		info=conteiners.find('p').text.encode('utf-8')

		zp=conteiners.find_all('span')[2].text.encode('utf-8')

		f.write(title.replace(',',' ').replace('\n',' ') + ',' + info.replace(',',' ').replace('\n',' ') + ',' + zp.replace(',',' ').replace('\n',' ') + '\n')

f.close






	




