import socket
import requests


headers = {
'Host':'10.10.11.12',
'Connection':'keep-alive',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language':'zh-CN,zh;q=0.8'
}

data = {
'loginType':'',
'auth_type':'0',
'isBindMac':'0',
'pageid':'1',
'templatetype':'3',
'listbindmac':'0',
'isRemind':'0',
'loginTimes':'',
'groupId':'',
'userId':'这里输入账号',
'passwd':'这里输入密码'
}
# gethostbyname 返回的是 主机名 的IPv4 的地址格式，如果传入的参数是IPv4 的地址格式，则返回值跟参数一样，
# 这个函数不支持IPv6 的域名解析
localIP = socket.gethostbyname(socket.gethostname())
#gethostbyname_ex()它能够返回 一个三元组 （原始主机名，域名列表，IP地址列表），这个函数不支持IPv6的域名解析
#参数传入域名
ipList = socket.gethostbyname_ex(socket.gethostname())
ip = ipList[2][0]

url = 'http://10.10.11.12/portal.do?wlanuserip='+ ip +'&wlanacname=XF_BRAS&mac=eb:57:14:ac:00:00&vlan=0&rand=d2c08f2fd07e2'


p = requests.post(url,headers=headers,data=data)
r = requests.get('https://www.baidu.com')
if r.status_code == 200:
    print("登陆成功")
else:
    print("登陆失败")
