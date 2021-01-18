#        requests库的使用



#import requests

#r = requests.get('https://baidu.com/')
#print(type(r))
#print(r.status_code)
#print(r.text)
#print(r.cookies)

#            1 GET请求

#import requests

#r = requests.get('http://httpbin.org/get')
#print(r.text)

# 这样就可以构造一个GET请求返回结果中包含请求头、URL、IP等

#    parame 参数

#import requests

#data = {
#    'name' : 'germey',
#    'age': '22'
#    }
#r = requests.get("http://httpbin.org/get",params= data)
#print(r.text)

# 对于GET请求，附加额外信息

#   json()方法
#import requests

#r = requests.get('http://httpbin.org/get')
#print(type(r.text))
#print(r.text)
#print(r.json())
#print(type(r.json()))

# text为str类型方法json()可以得到字典格式
# 如果返回结果不为JSON格式

#          抓取网页
#import requests
#import re

#headers = {
#   'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
#   +'Chrome/75.0.3770.100 Safari/537.36'
#    }
#r = requests.get("https://www.zhihu.com/explore",headers = headers)
#pattern = re.compile('data-za-detail-view-id="5794">(.*?)</a>',re.S)
#titles = re.findall(pattern,r.text)
#print(titles)

# 这里加入了headers信息，其中User-Agent浏览器标识信息

#        抓取二进制数据
#import requests

#r = requests.get("https://github.com/favicon.ico")
#with open('favicon.ico','wb') as f:
#    f.write(r.content)

# 这里用来open方法第一个参数为文件名称，第二个参数代表以二进制写的形式
# 打开，可以向文件里写入二进制数据 

#print(r.text)
#print(r.content)

# 由于图片为二进制数据r.text打印转换为str类型，也就是直接转换为字符串，故出现乱码

#         添加headers
#import requests

#headers = {
#    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
#    }
#r =  requests.get("https://www.zhihu.com/explore",headers = headers)
#print(r.text)

#           2、 POST请求
#import requests

#data = {'name':'germey','age':'22'}
#r = requests.post("http://httpbin.org/post",data = data)
#print(r.text)

# 利用request.post 可以完成POST请求

#          3、 响应
#import requests 

#headers = {
#    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
#    }
#r = requests.get("http://www.jianshu.com", headers = headers)
#print(type(r.status_code),r.status_code)
#print(type(r.headers),r.headers)
#print(type(r.cookies),r.cookies)
#print(type(r.url),r.url)
#print(type(r.history),r.history)

#status_code 状态码
#headers 响应头
#cookies Cookies
#url URL
#history 请求历史

#import requests

#headers = {
#    'user-agent' : 'mozilla/5.0 (windows nt 10.0; wow64) applewebkit/537.36 (khtml, like gecko)'
#    }
#r = requests.get('http://www.jianshu.com',headers = headers)
#if not r.status_code == requests.codes.ok:
#    print('defoult')
#else:
#   print('Request Successfully')

#               高级用法

#        文件上传
#import requests

#files = {'file' : open('favicon.ico','rb')}
#r = requests.post("http://httpbin.org/post",files = files)
#print(r.text)

# rb为二进制方法读取       

#        Cookies 
#import requests

#headers = {
#    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
#    }
#r = requests.get("https://www.zhihu.com",headers = headers)
#print(r.cookies)
#for key,value in r.cookies.items():
#    print(key + '=' + value)

#import requests

#headers = {
#    'Cookie' : 'HMACCOUNT=63C7B76F501F48AD; HMVT=6bcd52f51e9b3dce32bec4a3997715ac|1579052032|; BAIDUID=CAB85AE969F075BD282A3EA9C2707E54:FG=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BIDUPSID=F5C8694B81A59F59CECA32399ADE4860 _xsrf=AxTlOJJCSqFJ2GDcCDm0GzSfBEt6Wg7Q; _zap=9dbcb083-59a1-45cc-a3ae-69afa7d9b1ac; d_c0="AHBjS1gOgRCPTop-AAzXBHbvIPatHFEftZk=|1576318710"; client_id="RDQ0N0JBOUJGQ0ZBQjU1MDZEMjJBNzc5RThBQzk0QkY=|1577528256|bc39f2bed06ead84bbd72f3cf1f7db6abaf26633"; tst=r; q_c1=76d722a6129a412bb0e53954af00a906|1577529440000|1577529440000; l_n_c=1; n_c=1; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1578992640,1579048926,1579050155,1579050163; capsion_ticket="2|1:0|10:1579050396|14:capsion_ticket|44:ODg3NGE4MDRjN2VmNDdjZWFiMzVkMWRhNDRmODk5YWE=|c929b9ee4ff4102bc87aff6bcd3c886392f91f4d87c1819c349913e1384ddac4"; l_cap_id="MjA1MDk3Yzk2MTRkNDc2ZmE1MzdmN2I4MDA4YmRmNjA=|1579050398|deb1915c7e958069b35868e49f5ed83b47b25e26"; r_cap_id="OWY3MzUxYmZkZThmNDliNWE4N2RjMzg0ZDlkZDM5NTg=|1579050398|decca780f36b93c4921760fbc1fe33f46c5ce3fb"; cap_id="ZmE0NDA0MWU4OWI1NDY0NWI4MTMzYjM2OGYxMTUwNTA=|1579050398|697397d37aa5106d91c3b1b1269159149491aef8"; z_c0=Mi4xdkFqckZnQUFBQUFBY0dOTFdBNkJFQmNBQUFCaEFsVk45N01MWHdBdnhDbWlxNi11VWsxb1FRLWUxS0ZMMTV1V2hn|1579050488|fdeceff07878f2611a7c697c2302989fa8e37492; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1579050499; KLBRSID=81978cf28cf03c58e07f705c156aa833|1579050824|1579048914',
#    'Host': 'www.zhihu.com',
#    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
#r = requests.get('http://www.zhihu.com',headers = headers)
#print(r.text)

#         会话维持
#import requests

#requests.get('http://httpbin.org/cookies/set/number/123456789')
#r = requests.get('http://httpbin.org/cookies')
#print(r.text)

# 这样并不能成功获取设置的Cookies
#import requests

#s = requests.Session()
#s.get('http://httpbin.org/cookies/set/number/123456789')
#r = s.get('http://httpbin.org/cookies')
#print(r.text)

# 利用Session对象可以维持一个会话

#    4、 SSL证书验证
#import requests
#from requests.packages import urllib3

#urllib3.disable_warnings()
#response = requests.get('https://www.12306.cn',verify = False)
#print(response.status_code)

# 设置忽略警告来屏蔽警告

#import requests
#import logging

#logging.captureWarnings(True)
#response = requests.get('https://www.12306.cn',verify = False)
#print(response.status_code)

# 通过捕获警告日志到日志的方式忽略警告

#    5、代理设置
#import requests

#proxies = {
#    "http" : "http://113.116.50.182:808",
#    "https" : "https://113.116.50.182:808"
#    }

#requests.get("https://taobao.com",proxies = proxies)

#    6、 超时设置
#import requests

#r = requests.get("http://www.taobao.com",timeout = 0.01)
#print(r.status_code)

# timeout为超时参数如果要永久等待timeout = None

#    7、 身份认证
#import requests
#from requests.auth import HTTPBasicAuth

#r = requests.get('http://localhost:5000', auth = HTTPBasicAuth('username','password'))
#print(r.status_code)

# 如果要身份验证则需要auth参数

#    8、 Prepared Request
from requests import Request,Session

url = 'http://httpbin.org/post'
data = {
    'name' : 'germey'
    }
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
s = Session()
req = Request('POST',url,data = data,headers = headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)

# 这里引入了Request,然后用url、data和headers构造了一个Request对象
# 再调用Session的prepare_request()方法将其转换为一个Prepared Request对象
# 最后调用send()方法发送即可

