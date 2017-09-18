import requests

login_url = 'https://accounts.douban.com/login'

headers = {
'Host':'accounts.douban.com',
'Content-Length':'104',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Referer':'https://www.douban.com/login',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.8'
}

data = {
'source':'None',
'redir':'https://www.douban.com',
'form_email':'',
'form_password':''
}
def login(user,pas):
    data['form_email'] = user
    data['form_password'] = pas
    s = requests.Session()
    p = s.post(login_url,headers=headers,data=data)
    print(p.status_code)
    print(p.url)
    print(p.text)

if __name__ == '__main__':
    user = input("输入用户名:")
    pas = input("输入密码:")
