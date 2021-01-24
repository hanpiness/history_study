from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json
import requests


# 获取url
#def get_products():
#    html = browser.page_source
#    mysoup=BeautifulSoup(html,'lxml')
#    item = mysoup.find(attrs={'class':'bk_7'})
#    lists = item.find_all(attrs = {'class':'link03'})
#    for list in lists:
#        product = str(list['href'])
#        product = 'http://www.agri.cn/kj/syjs/zzjs'+product[1:] 
#        with open('url.txt','a',encoding= 'utf-8')as f:
#            f.write(json.dumps(product,ensure_ascii=False)+'\n')

#browser = webdriver.Chrome()
#wait = WebDriverWait(browser,10)
#browser.get('http://www.agri.cn/kj/syjs/zzjs/index.htm')
#for i in range(1,68):
#    print("正在爬取第",i,'页')
#    input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#pageBar span#next > a')))
#    input.click()
#    get_products()

f = open('url.txt','r')
line = f.readline()
line = line[:-1]
tables = []
while line:
    line = f.readline()
    line = line[:-1]
    print(line)
    browser = webdriver.Chrome()
    browser.get(line)
    print(browser.page_source)
    #table_bf = BeautifulSoup(html)
    #print(table_bf.find('table',width=500,align='center'))
f.close()