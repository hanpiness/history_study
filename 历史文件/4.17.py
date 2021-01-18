from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import json
import requests

broswer = webdriver.Chrome()
broswer.get('http://www.bjdcfy.com/qita/xljkxxth/2017-10/1035150.html')
html = broswer.page_source
mysoup = BeautifulSoup(html,'lxml')
items = mysoup.find(attrs = {'class':'artTxt'})
items = mysoup.find(attrs = {'id':'str_content'}).get_text()

print(items)