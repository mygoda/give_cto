#coding = utf-8
from django.shortcuts import render
from django.http import HttpResponse 
import urllib2
from igoda.models import ShopList
from bs4 import BeautifulSoup

import sys 
reload(sys) 
sys.setdefaultencoding('utf8') 
def getWeb(req):
	url = "http://www.dianping.com/search/category/2/45/g147"
	url1 = 'http://www.dianping.com'
	req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
	webpage= urllib2.urlopen(req)
	parser = BeautifulSoup(webpage)
	shop_list = parser.find('div','shop-all-list').findAll('li')
	for title_shop in shop_list:
        	tit_div = title_shop.find('div','tit')
        	name = tit_div.a.get_text().encode('utf-8').replace(u'\n','')
        	hre =url1 + tit_div.a['href']
        	#print name
        	requ = urllib2.Request(hre, headers={'User-Agent' : "Magic Browser"})
        	res = urllib2.urlopen(requ)
        	soup = BeautifulSoup(res)
        	base_info = soup.find('div','basic-info')
        	title = base_info.find('span',itemprop="street-address")
        	title_text= title.get_text().replace(u'\n','').encode('utf-8')
        	diqu = base_info.find('span',itemprop="locality region").get_text()
		#print diqu.get_text() + title_text
        	#print("%s %s" % (diqu,title_text))
		#shop address
		addr = str(diqu + title_text)
        	tel = soup.find('span',itemprop="tel")
        	telphone = str(tel.get_text().replace(u'\n','').encode('utf-8'))
		#print telphone
		#save in database
		new = ShopList(shop_name=name,shop_address=addr,shop_tel=telphone)
		new.save()
		return HttpResponse('<h1>save ok</h1>')



	
