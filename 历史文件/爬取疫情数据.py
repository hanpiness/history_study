from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
import json

browser = webdriver.Chrome()
browser.get("http://fms.news.cn/swf/2020_sjxw/2_1_xgyq/index.html")
html = browser.page_source
mysoup = BeautifulSoup(html,'lxml')
chinalist = mysoup.find(attrs={'id':'table'})
citylists = chinalist.find_all('div',class_="city")
for citylist in citylists:
    products={
        '省市(自治区，直辖市)': citylist.find('p',class_='cityName').get_text(),
        '确诊':citylist.find("p",class_='cityQZ').get_text(),
        '死亡':citylist.find("p",class_='citySW').get_text(),
        '治愈':citylist.find("p",class_='cityZY').get_text()
        }
    print(products)
    with open('疫情.txt','a',encoding= 'utf-8')as f:
        f.write(json.dumps(products,ensure_ascii=False)+'\n')

