# urllib库中含有四个模块
# 《1》 request     HTTP请求模块，模拟发送请求
# 《2》 error       异常处理模块
# 《3》 parse       提供了许多URL处理方法，比如拆分，解析，合并
# 《4》 robotparser 识别网站的robots.txt文件
    
                       ### 《1》request
                      ### 1，urlopen()

#import urllib.request

#response = urllib.request.urlopen('http://www.python.org')
#print(response.read().decode('utf-8'))
#print(type(response))              
#print(response.status)              # <状态码>
#print(response.getheaders())        # <响应的头信息>     
#print(response.getheader('Server')) # <响应头信息中具体的某一项>

# urlopen()返回的是一个HTTPResponse类型的对象，主要包含
# read(),getheader(name)<响应头信息中具体的某一项>,getheaders()<响应的头信息>
# 等方法以及msg,version,status<状态码>,reason等属性

                     ### urlopen()中的data参数

#import urllib.request
#import urllib.parse

#data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding ='utf-8')
#response = urllib.request.urlopen('http://httpbin.org/post',data = data)
#print(response.read())

# data 用来传递附加信息需要被转码成bytes(字节流)类型
# bytes()方法第一个参数应为字符串类型，第二个参数指定编码格式
# urlencode()方法可以将字典类型转化为字符串类型
# 此次请求为POST方式

                     ### timeout参数

#import urllib.request
#import socket
#import urllib.error

#try: 
#    response = urllib.request.urlopen('http://httpbin.org/get',timeout = 0.1)
#except urllib.error.URLError as e:
#    if isinstance(e.reason , socket.timeout):
#        print('TIME OUT')

# timeout参数用于设置超时时间，单位为秒
# isinstance()方法可以用来判断两个参数类型是否一致

                 # Request类的用法

#import urllib.request
#import urllib.parse

#url = 'http://httpbin.org/post'
#headers = {
#    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
#                 +'(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
#    'Host' : 'httpbin.org'
#    }
#dict = {'name' : 'Germey'}
#data = bytes(urllib.parse.urlencode(dict),encoding = 'utf-8')

#req = urllib.request.Request(url,data = data,headers = headers,method = 'POST')
#response = urllib.request.urlopen(req)
#print(response.read().decode('utf-8'))

# Request(url,data=None, headers={},
#                origin_req_host=None, unverifiable=False,
#                method=None）
# 第二个参数为附加信息
# 第三个参数headers是一个字典，为请求头，常用来修改User-Agent
# 来伪装为浏览器   第六个参数为指示请求的方法

              # urllib库的高级用法
              # 验证

#from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
#from urllib.error import URLError

#username = 'passname'
#password = 'password'
#url = 'https://www.saikr.com'

#p = HTTPPasswordMgrWithDefaultRealm()
#p.add_password(None,url,username,password)
#auth_handler = HTTPBasicAuthHandler(p)
#opener = build_opener(auth_handler)

#try:
#    result = opener.open(url)
#    html = result.read().decode('utf-8')
#    print(html)
#except URLError as e:
#    print(e.reason)

# 先实例化 HTTPBasicAuthHandler对象其参数为
# HTTPPasswordMgrWithDefaultRealm对象，
# 利用add_password()添加进去用户名和密码

                      # 代理

#from urllib.error import URLError
#from urllib.request import ProxyHandler,build_opener

#proxy_handler = ProxyHandler(
#    {
#        'http': 'http://59.49.50.135:9743',
#        'https': 'https://59.49.50.135:9743'
#        })
#opener = build_opener(proxy_handler)
#try:
#    response = opener.open('https://baidu.com')
#    print(response.read().decode('utf-8'))
#except URLError as e:
#    print(e.reason)

                    #Cookies
#import http.cookiejar, urllib.request

#cookie = http.cookiejar.CookieJar()
#handler = urllib.request.HTTPCookieProcessor(cookie)
#opener = urllib.request.build_opener(handler)
#response = opener.open('http://www.baidu.com')
#for item in cookie:
#    print(item.name+'='+item.value)

# 保存为文件格式
#import urllib.request, http.cookiejar

#filename = "coolies.txt"
#cookie = http.cookiejar.MozillaCookieJar(filename)
#handler = urllib.request.HTTPCookieProcessor(cookie)
#opener = urllib.request.build_opener(handler)
#respones = opener.open("http://www.baidu.com")
#cookie.save(ignore_discard=True,ignore_expires=True)
# 将文件写入

# MozillaCookieJar 在生成文件时会用到 
# 用来处理cookie和相关文件的的事件
# LWPCookieJar 可以将文件保存为LWP格式

#import urllib.request, http.cookiejar

#cookie = http.cookiejar.LWPCookieJar()
#cookie.load('cookies.txt',ignore_discard = True,ignore_expires = True)
#handler = urllib.request.HTTPCookieProcessor(cookie)
#opener = urllib.request.build_opener(handler)
#response = opener.open('http://www.baidu.com')
#print(response.read().decode('utf-8'))

# 利用load()来读取本地的cookies文件


#                处理异常

# 1 URLError

#from urllib import error, request

#try:
#    response = urllib.request.urlopen("HTTP://cuiqingcai.com/index.htm")
#except error.URLError as e:
#    print(e.reason)

# URLError 具有一个属性reason它可以返回错误原因
# 由request模块产生的错误都可以通过捕获这个类来获取

# 2 HTTPError
#from urllib import error, request
#try:
#    response = urllib.request.urlopen("http://cuiqingcai.com/index.htm")
#except error.HTTPError as e:
#    print(e.reason,e.code,e.headers, sep='\n')

# URLError 为 HTTPError的一个父类
# 有3个属性code状态码, reason错误原因,headers返回请求头

#import socket
#import urllib.request
#import urllib.error

#try:
#   response = urllib.request.urlopen('http://www.baidu.com',timeout=0.01)
#except urllib.error.URLError as e:
#    print(type(e.reason))
#    if isinstance(e.reason,socket.timeout):
#        print('time out')

#                   解析链接
#           1，urlparse

#from urllib.parse import urlparse

#result = urlparse('http://www.baidu.com/index.html;user?id=5#count')
#print(type(result),result)

# URL 可以实现URL的识别和分段

# 标准的链接格式
# scheme(协议)://netloc(域名)/path(路径);params(参数)?query(查询条件)#fragment(锚点)
# 锚点用于直接定位页面内部的下拉位置

#from urllib.parse import urlparse

#result = urlparse('www.baidu.com/index.html;user?id=5#comment',scheme = 'https')
#print(result)
# 参数 urlstring(为必填项)scheme(默认的协议)allow_fragments()

#          2, urlunparse()

#from urllib.parse import urlunparse

#data = urlunparse(['http','www.baidu.com','index.html','user','id=5','count'])
#print(data)

# 与urlparse相反构造url链接

#          3， urlsplit

#from urllib.parse import urlsplit

#result = urlsplit('http://www.baidu.com/index.html;user?id=5#count')
#print(result.scheme,result[0])

# 与urlparse相似只是不再单独解析params而是会合并到path中

#         4， urlunsplit

#from urllib.parse import urlunsplit

#data = ['http','www.baidu.com','index.html','a=6','comment']
#print(urlunsplit(data))

# 将链接各部分组合为完整链接的方法

#         5， urljoin()
#from urllib.parse  import urljoin

#print(urljoin('http://www.baidu.com','FAQ.html'))
#print(urljoin('http://www.baidu.com','https://cuiqingcai.com/FAQ.html'))
#print(urljoin('www.baidu.com','?category=2#comment'))

# 第一个参数为基础链接，将新的链接作为第二个参数，该方法会
# 分析基础链接的scheme，netloc和path这3个内容并对新链接缺失的部分进行补充

#           6. urlencode()
#from urllib.parse import urlencode

#params = {
#    'name' : 'germey',
#    "age" : 22
#    }
#base_url = 'http://www.baidu.com?'
#url = base_url+urlencode(params)
#print(url)

# urlencode()在构造参数时十分有用
# 将字典序列化

#           7. parse_qs()
#from urllib.parse import parse_qs

#query = 'name=germey&age=22'
#print(parse_qs(query))

# 反序列化将序列化转换为字典

#          8. parse_qsl()
#from urllib.parse import parse_qsl

#query = 'name=germey&age=22'
#print(parse_qsl(query))

# 将序列化转换为元组

#         9. quote()
#from urllib.parse import quote

#keyword = '壁纸'
#url = 'https://www.baidu.com/s?wd=' +quote(keyword)
#print(url)

# 这个方法可以将内容转换为url编码形式

#         10. unquote()
#from urllib.parse import unquote

#url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
#print(unquote(url))

# 可以利用unquote来解码

#           Robots协议
#           robotparser模块
#from urllib.robotparser import RobotFileParser

#rp = RobotFileParser()
#rp.set_url('http://www.jianshu.com/robots.txt')# 如果创建对象时已经传入链接则无需这一步
#rp.read()                                      # 读取robots.txt文件，如果没有这一步，接下来的判断将都为False
#                                               # 并不会返回任何内容
#print(rp.can_fetch('*','http://www.jianshu.com/p/b67554025d7d')) # 检测搜索引擎是否可以抓取这个链接返回True或False
#print(rp.can_fetch('*','http://www.jianshu.com/search?q=python&page=1&type=collections'))

# 利用它，就可以判断哪些页面可以抓取哪些不可以
# mtime()返回上次抓取和分析robots.txt的时间
# modified() 将当前时间设置为上次抓取和分析robots.txt的时间




