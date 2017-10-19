# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import os
import re

#设置http头

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0'}
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0',
          'Referer':'http://www.mzitu.com/'}
url = 'http://www.mzitu.com/'
r = requests.get(url,headers=headers).text
soup = BeautifulSoup(r)
page = soup.find('div',class_='nav-links').find_all('a')[-2].text
x = 1
for x in range(1,int(page)+1):
    url = 'http://www.mzitu.com/'
    url = url+'page/'+str(x)
    r = requests.get(url,headers=headers).text
    soup = BeautifulSoup(r)
    all_limian = soup.find('div',class_='postlist').find('ul',id='pins').find_all('li')
    for li in all_limian:
        limian = li.find('a')['href']
        url = limian + '/'
        r = requests.get(url,headers=headers).text
        soup = BeautifulSoup(r)
        max_page = soup.find('div',class_='pagenavi').find_all('a')[-2].find('span').text
        i = 1
        for i in range(1,int(max_page)+1):
            url = limian+'/'
            url = url+str(i)
            print(url)
            r = requests.get(url,headers=headers).text
            soup = BeautifulSoup(r)
            title = soup.find('h2', class_='main-title').text
            dizhi = soup.find('div',class_='main-image').find('p').find('a').find('img')['src']
            print('正在爬取%s'%title)
            filename = 'F://mzitu//%s.jpg'%title
            s = requests.get(dizhi,headers=header).content
            with open(filename,'wb+') as fp:
                fp.write(s)
            print('%s爬取完成'%title)

print('全部完成')



