import requests
from bs4 import BeautifulSoup
import os
import random
import re



def get_user_agent():
	user_agent = """Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0
	Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1
	Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11
	Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"""
	agent = user_agent.split('\n')
	length = len(agent)
	return agent[random.randint(0,length-1)]

def geturl():

	
	x = 2
	
	while x<14:
		url = 'https://www.qiushibaike.com'
		headers = {'User-Agent':'get_user_agent()'}
		r = requests.get(url,headers =headers).text
		fanye = '/8hr/page/'+ str(x) + '/'
		url = url+fanye
		x = x+1
		return url

def neirong():
	duanzi = []
	url = 'https://www.qiushibaike.com'
	headers = {'User-Agent':'get_user_agent()'}
	r = requests.get(geturl(),headers=headers).text
	soup = BeautifulSoup(r)
	kuang = soup.find('div',class_='coll')
	suoyou = kuang.find_all('div',id = re.compile('qiushi_tag\_\d?'))
	for suoyou_neirong in suoyou:
		neirong = suoyou_neirong.find('div',class_='content').find('span').getText()
		duanzi.append(neirong)
		return duanzi

def cunchu():
	path = 'D://duanzi'
	with open(path,'wb') as fp:
		fp.write(neirong())


if __name__ == '__main__':
	cunchu()

	
	


