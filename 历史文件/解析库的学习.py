#  #  #   解析库使用
#  XPath

#from lxml import etree
#import json
#text = '''
#<div>
#<ul>
#<li class="item-0"><a href="link1.html">first item</a></li>
#<li class="item-1"><a href="link2.html">second item</a></li>
#<li class="item-inactive"><a href="link3.html">third item</a></li>
#<li class="item-1"><a href="link4.html">fourth item</a></li>
#<li class="item-0"><a href="link5.html">fifth item</a>
#</ul>
#</div>
#'''
#html = etree.HTML(text)
#result = etree.tostring(html)
#with open('text.txt','a',encoding='utf-8') as f:
#    f.write(json.dumps(result.decode('utf-8'),ensure_ascii=False)+'\n')
#print(result.decode('utf-8'))

# 首先声明了一段HTML文本，调用HTML类来初始化
# 这就成功构造了一个XPath的解析对象，etree可以自动修正HTML文本
# 调用tostring()方法即可输出修正后的HTML代码但为bytes类型，利用
# decode()方法将其转成str类型

#from lxml import etree

#html = etree.parse('D:/程序/PythonApplication1/text.html',etree.HTMLParser())
#result = etree.tostring(html)
#print(result.decode('utf-8'))

#       1、所有节点
#from lxml import etree

#html = etree.parse('./text.html',etree.HTMLParser())
#result = html.xpath('//*')
#print(result)

# 一般用//开头的XPath规则来选取所有符合要求的节点
# 使用*代表匹配所有节点，也就是整个HTML文本中的所有节点都会被获取

#from lxml import etree

#html = etree.parse('./text.html',etree.HTMLParser())
#result = html.xpath('//li')
#print(result)
#print(result[0])

# 如果要提取某一节点可以使用//加上节点名称
# 直接使用xpath方法即可

#      2、子节点
#from lxml import etree

#html = etree.parse('./text.html',etree.HTMLParser())
#result = html.xpath('//li/a')
#print(result)

# 通过//或/即可查找元素的子节点或子孙节点
# //li/a 表示li节点的所有直接a子节点
# /用来选取直接子节点，如果要获取所有子孙节点，就使用//

#     3、 父节点
#from lxml import etree

#html = etree.parse('./text.html',etree.HTMLParser())
#result = html.xpath('//a[@href="link4.html"]/../@class')
#print(result)

# 首先选中href属性为link4.html的a节点
# 然后获取其父节点
#最后再获取其class属性

#from lxml import etree

#html = etree.parse('./text.html',etree.HTMLParser())
#result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
#print(result)

# ..获取父节点
# 也可以用parent::来获取父节点

#     4、属性匹配
#from lxml import etree

#html = etree.parse('./text.html',etree.HTMLParser())
#result = html.xpath('//li[@class="item-0"]')
#print(result)

# 通过加入[@class="item-0"]限制了节点得到class属性

#    5、 文本获取
#from lxml import etree

#html = etree.parse('./text.html',etree.HTMLParser())
#result = html.xpath('//li[@class="item-0"]/a/text()')
#print(result) 

# 先选取li的直接子节点都是a节点，文本都是在a节点内部
# text()方法获取节点中的文本

#from lxml import etree

#html = etree.parse('./text.html',etree.HTMLParser())
#result = html.xpath('//li[@class="item-0"]//text()')
#print(result)

# 第二种方式利用//选取所有子孙节点的文本

#      6、属性获取
#from lxml import etree

#html = etree.parse('./text.html',etree.HTMLParser())
#result = html.xpath('//li/a/@href')
#print(result)

# 通过@href即可获取节点的href属性。
# 这里与属性匹配的方法不同，属性匹配是中括号加属性名和值
# 来限定某个属性，而此处@href是获取节点的某个属性

#        7、属性多值匹配
#from lxml import etree
#text = '''
#<li class="li li-first"><a href="link.html">first item</a></li>
#'''
#html = etree.HTML(text)
#result = html.xpath('//li[contains(@class,"li")]/a/text()')
#print(result)

# 当某些节点的某个属性可能有多个值
# 需利用contains()
# 第一个参数传入属性名称，第二个参数传入属性值
# 只要这个属性包含所传入的属性值就可以匹配

#     8、 多属性匹配
#from lxml import etree

#text = '''
#<li class="li li-first" name="item"><a href="link.html">first item</a></li>
#'''
#html = etree.HTML(text)
#result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
#print(result)

# 要确定li节点，需要同时根据class和name属性来选择
# 一个条件是class属性里面包含li字符串
# 另一个条件是name属性为item字符串

#      9、按序选择
#from lxml import etree

#text = '''
#<div>
#<ul>
#<li class="item-0"><a href="link1.html">first item</a></li>
#<li class="item-1"><a href="link2.html">second item</a></li>
#<li class="item-inactive"><a href="link3.html">third item</a></li>
#<li class="item-1"><a href="link4.html">fourth item</a></li>
#<li class="item-0"><a href="link5.html">fifth item</a>
#</ul>
#</div>
#'''
#html = etree.HTML(text)
#result = html.xpath('//li[1]/a/text()')
#print(result)
#result = html.xpath('//li[last()]/a/text()')
#print(result)
#result = html.xpath('//li[position()<3]/a/text()')
#print(result)
#result = html.xpath('//li[last()-2]/a/text()')
#print(result)

# 当选择时某些属性可能匹配了多个节点
# position(),last()也可以利用数字，但第一个为1

#      10、节点轴的选择
#from lxml import etree

#text = '''
#<div>
#<ul>
#<li class="item-0"><a href="link1.html"><span>first item</span></a></li>
#<li class="item-1"><a href="link2.html">second item</a></li>
#<li class="item-inactive"><a href="link3.html">third item</a></li>
#<li class="item-1"><a href="link4.html">fourth item</a></li>
#<li class="item-0"><a href="link5.html">fifth item</a>
#</ul>
#</div>
#'''
#html = etree.HTML(text)
#result = html.xpath('//li[1]/ancestor::*')
#print(result)
#result = html.xpath('//li[1]/ancestor::div')
#print(result)
#result = html.xpath('//li[1]/attribute::*')
#print(result)
#result = html.xpath('//li[1]/child::a[@href="link1.html"]')
#print(result)
#result = html.xpath('//li[1]/descendant::span')
#print(result)
#result = html.xpath('//li[1]/following::*[2]')
#print(result)
#result = html.xpath('//li[1]/following-sibling::*')
#print(result)

# 第一个ancestor轴，可以获取所有祖先节点，其后需要两个冒号，然后是节点的选择器
# 第二个选择时加了限定条件，故得到的结果只有div
# 第三个attribute轴，可以获取所有属性 值 其后需要两个冒号，然后是节点选择器
# 第四个child轴，可以获取所有直接子节点
# 第五个descendant轴，可以获取所有子孙节点
# 第六个following轴，可以获取当前节点之后的所有节点，但加了索引选择，故只获取了第二个后续节点
# 第七个following-sibling轴，可以获取当前节点之后的所有同级节点


#   #   Beautiful Soup
#from bs4 import BeautifulSoup
#soup = BeautifulSoup('<p>Hello</p>','lxml')
#print(soup.p.string)

#html = '''
#<html><head><title>The Dormouse's story</title></head>
#<body>
#<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
#<p class="story">Once upon a time there were three little sisters; and their names were
#<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
#<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
#<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
#and they lived at the bottom of a well.</p>
#<p class="story">...</p>
#'''
#from bs4 import BeautifulSoup

#soup = BeautifulSoup(html,'lxml')
#print(soup.prettify())
#print(soup.title.string)

# 将HTML作为第一个参数,该对象第二个参数为解析器的类型
# 这样就完成了BeautifulSoup对象的初始化
# prettify方法可以把要解析的字符串以标准的缩进格式输出
# 更正HTML在初始化BeautifulSoup时就完成了
# 调用soup.title.string,实际上输出HTML中title节点的文本内容
# soup.title可以选出HTML中的title节点，再利用string可以得到节点中文本

#    1、 选择元素
#html = '''
#<html><head><title>The Dormouse's story</title></head>
#<body>
#<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
#<p class="story">Once upon a time there were three little sisters; and their names were
#<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
#<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
#<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
#and they lived at the bottom of a well.</p>
#<p class="story">...</p>
#'''
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html,'lxml')
#print(soup.title)
#print(type(soup.title))
#print(soup.title.string)
#print(soup.head)
#print(soup.p)

# 当有多个节点时，这种选择方式只会选择到第一个匹配的节点

#      2、 提取信息
## 《1》获取名称
#print(soup.title.name)
# 调用name属性就可以得到节点名称
## 《2》获取属性
#print(soup.p.attrs)
#print(soup.p.attrs['name'])
# 调用attrs获取全部属性
#print(soup.p['name'])
#print(soup.p['class'])
# 注意有的返回结果是字符串，有的为列表
# name属性的值是唯一的而class一个节点元素可能有多个class，故返回列表
#  《3》嵌套选择
#html='''
#<html><head><title>The Dormouse's story</title><head>
#<body>
#'''
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html,'lxml')
#print(soup.head.title)
#print(type(soup.head.title))
#print(soup.head.title.string)

#   3、关联选择
#  《1》子节点和子孙节点
#html = '''
#<html>
#<head>
#<title>The Dormouse's story</title>
#</head>
#<body>
#<p class="story">
#    Once upon a time there were three little sisters; and their names were
#    <a href="http://example.com/elsie" class="sister" id="link1">
#<span>Elsie</span>
#</a>
#<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#and
#<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#and they lived at the bottom of a well.
#</p>
#<p class="story">...</p>
#'''
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html,'lxml')
#print(soup.p.contents)

# 返回列表形式。p节点里既包含文本，又包含节点
# 列表中的每个元素都是p节点的直接子节点
# contents属性得到的结果为直接子节点的列表

#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html,'lxml')
#print(soup.p.children)
#for i,child in enumerate(soup.p.children):
#    print(i, child)

# 和content一样children属性也得到直接子节点

#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html,'lxml')
#print(soup.p.descendants)
#for i,child in enumerate(soup.p.descendants):
#    print(i,child)

# descendants属性可以得到所有子孙节点

#    《2》父节点和祖先节点
#html = '''
#<html>
#<head>
#<title>The Dormouse's story</title>
#</head>
#<body>
#<p class="story">
#    Once upon a time there were three little sisters; and their names were
#    <a href="http://example.com/elsie" class="sister" id="link1">
#<span>Elsie</span>
#</a>
#<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#and
#<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#and they lived at the bottom of a well.
#</p>
#<p class="story">...</p>
#'''
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html,'lxml')
##print(soup.a.parent)
#print(type(soup.a.parents))
#print(list(enumerate(soup.a.parents)))

# parent属性只是输出a节点的直接父节点
# parents属性输出所有的祖先节点，返回结果为生成器类型
# 这里用列表输出了它的索引和内容

#    《3》兄弟节点
#html = '''
#<html>
#<head>
#<title>The Dormouse's story</title>
#</head>
#<body>
#<p class="story">
#    Once upon a time there were three little sisters; and their names were
#    <a href="http://example.com/elsie" class="sister" id="link1">
#<span>Elsie</span>
#</a>
#        Hello
#<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#and
#<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#and they lived at the bottom of a well.
#</p>
#'''
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html,'lxml')
#print('Next Sibling',soup.a.next_sibling)
#print('Prev Sibling',soup.a.previous_sibling)
#print('Next Siblings',list(enumerate(soup.a.next_siblings)))
#print('Prev Siblings',list(enumerate(soup.a.previous_siblings)))

# next_sibling和previous_sibling分别获取节点的下一个和上一个兄弟元素
# next_siblings和previous_siblings则分别获取后面和前面的兄弟节点

#     《4》提取信息
#html = '''
#<html>
#<body>
#<p class="story">
#            Once upon a time there were three little sisters;and their names were
#<a href="http://example.com/elsie" class="sister" id="link1">Bob</a>
#<a href="http://example.com/lacie"class="sister" id="link2">Lacie</a>
#</p>
#'''
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html,'lxml')
#print('Next Sibling:')
#print(type(soup.a.next_sibling))
#print(soup.a.next_sibling)
#print(soup.a.next_sibling.string)
#print('Parent:')
#print(type(soup.a.parents))
#print(list(soup.a.parents)[0])
#print(list(soup.a.parents)[0].attrs['class'])

# 如果返回结果是单个节点，那么直接调用string，attrs属性获取其文本和属性
# 如果返回的是多个节点的生成器，则可以转成列表后取出某个元素

#      4、 方法选择器
#     《1》find_all()
# find_all(name,attrs,recursive,text,**kwargs)
#     <1>name
#html = '''
#<div class="panel">
#<div class="panel-heading">
#<h4>Hello</h4>
#</div>
#<div class="panel-body">
#<ul class="list" id="list-1">
#<li class="element">Foo</li>
#<li class="element">Bar</li>
#<li class="element">Jay</li>
#</ul>
#<ul class="list list-small" id="list-2">
#<li class="element">Foo</li>
#<li class="element">Bar</li>
#</ul>
#</div>
#</div>
#'''
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html,'lxml')
#print(soup.find_all(name='ul'))
#print(type(soup.find_all(name='ul')[0]))
#for ul in soup.find_all(name='ul'):
#    print(ul.find_all(name='li'))
#    for li in ul.find_all(name='li'):
#        print(li.string)

# 因为每个元素都是bs4.element.Tag故可以进行嵌套循环
# 查询出所有的ul节点后，继续查询其内部的li节点

#    <2> attrs
#html = '''
#<div class="panel">
#<div class="panel-heading">
#<h4>Hello</h4>
#</div>
#<div class="panel-body">
#<ul class="list" id="list-1" name='elements'>
#<li class="element">Foo</li>
#<li class="element">Bar</li>
#<li class="element">Jay</li>
#</ul>
#<ul class="list list-small" id="list-2">
#<li class="element">Foo</li>
#<li class="element">Bar</li>
#</ul>
#</div>
#</div>
#'''
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html,'lxml')
#print(soup.find_all(attrs={'id':'list-1'}))
#print(soup.find_all(attrs={'name':'elements'}))

# 通过属性查询传入attrs={'id':'list-1'},参数的类型是字典类型
# 得到的是符合list-1的所有节点

#from bs4 import BeautifulSoup   
#soup = BeautifulSoup(html,'lxml')
#print(soup.find_all(attrs={id:'list-1'}))
#print(soup.find_all(class_='element'))

# 由于class来说为一个关键字，所以后面应加一个下划线

#    <3>text
#import re
#html = '''
#<div class="panel">
#<div class="panel-body">
#<a>Hello,this is a link</a>
#<a>Hello,this is a link, too</a>
#</div>
#</div>
#'''
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html,'lxml')
#print(soup.find_all(text=re.compile('link')))

# text参数，该参数为正则表达式对象，
# 结果返回所有匹配正则表达式的节点文本组成的列表

# 《2》find()
#html = '''
#<div class="panel">
#<div class="panel-heading">
#<h4>Hello</h4>
#</div>
#<div class="panel-body">
#<ul class="list" id="list-1">
#<li class="element">Foo</li>
#<li class="element">Bar</li>
#<li class="element">Jay</li>
#</ul>
#<ul class="list list-small" id="list-2">
#<li class="element">Foo</li>
#<li class="element">Bar</li>
#</ul>
#</div>
#</div>
#'''
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html,'lxml')
#print(soup.find(name='ul'))
#print(type(soup.find(name='ul')))
#print(soup.find(class_='list'))

# find方法只返回单个元素，第一个匹配的元素

# find_parents()和find_parent():前者返回所有祖先节点，后者返回直接父节点
# find_next_siblings()和find_next_sibling()前者返回后面所有的兄弟节点，
# find_previous_siblings()和find_previous_sibling()前者返回前面所有的兄弟节点
# 后者返回前面第一个兄弟节点
# find_all_next()和find_next()前者返回节点后所有符合条件的节点
# 后者返回第一个符合条件的节点
# find_all_previous()和find_previous()同理

#       5、CSS选择器
#html = '''
#<div class="panel">
#<div class="panel-heading">
#<h4>Hello</h4>
#</div>
#<div class="panel-body">
#<ul class="list" id="list-1">
#<li class="element">Foo</li>
#<li class="element">Bar</li>
#<li class="element">Jay</li>
#</ul>
#<ul class="list list-small" id="list-2">
#<li class="element">Foo</li>
#<li class="element">Bar</li>
#</ul>
#</div>
#</div>
#'''
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html,'lxml')
#print(soup.select('.panel .panel-heading'))
#print(soup.select('ul li'))
#print(soup.select('#list-2 .element'))
#print(type(soup.select('ul')[0]))

# select('ul li')选择所有ul节点下面的所有 li节点，类型依然是Tag类型

#   《1》嵌套选择
#from bs4 import BeautifulSoup   
#soup = BeautifulSoup(html,'lxml')
#for ul in soup.select('ul'):
#    print(ul.select('li'))

#   《2》获取属性
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html,'lxml')
#for ul in soup.select('ul'):
#    print(ul['id'])
#    print(ul.attrs['id'])

#   《3》获取文本
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html,'lxml')
#for li in soup.select('li'):
#    print('Get Text:',li.get_text())
#    print('String',li.string)
        


















