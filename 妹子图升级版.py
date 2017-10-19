import requests
import re
import os
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0'}
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0',
          'Referer':'http://www.mzitu.com/'}


def get_maxnum():
    url = 'http://www.mzitu.com/'
    r = requests.get(url,headers=headers).text
    soup = BeautifulSoup(r)
    max_num = soup.find('div',class_='nav-links').find_all('a')[-2].text
    return max_num

def get_all_li_url(url):

    #url = 'http://www.mzitu.com/'
    r = requests.get(url,headers=headers).text
    soup = BeautifulSoup(r)
    hrefs = []
    all_li = soup.find('div',class_='postlist').find('ul',id='pins').find_all('li')
    for li_url in all_li:
        href = li_url.find('a')['href']
        hrefs.append(href)
    return hrefs

def downloads(url):
    r = requests.get(url,headers=headers).text
    soup = BeautifulSoup(r)
    max_page = soup.find('div',class_='pagenavi').find_all('a')[-2].find('span').text
    m = 1
    for i in range(1,int(max_page)+1):

        url1 = url+'/'+str(i)
        print(url1)
        r = requests.get(url1,headers=headers).text
        soup = BeautifulSoup(r)
        title = soup.find('h2',class_='main-title').text
        img = soup.find('div',class_='main-image').find('p').find('a').find('img')['src']
        tupian = requests.get(img,headers=header).content
        dizhi = "E://mzitu//%s.jpg"%title
        print('正在爬取%s'%title)
        with open(dizhi,'wb+') as fp:
            fp.write(tupian)
        print('%s爬取完成'%title)

if __name__ == '__main__':
    s = get_maxnum()
    for i in range(1,int(s)+1):
        url = 'http://www.mzitu.com/'
        url = url+'page/'+str(i)
        p = get_all_li_url(url)
        for e in p:
            downloads(e)







