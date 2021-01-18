from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import json
from pyquery import PyQuery as pq
import requests

browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
browser.get('http://www.gkstk.com/wenku/art-200885.html')
input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#morebtn > a')))
input.click()
html = browser.page_source
mysoup = BeautifulSoup(html,'lxml')
items = mysoup.find(attrs = {'class':'article clearfix'})
items = items.find(attrs = {'class':'content clearfix'}).get_text()
print(items)
    
  #  with open('daan.txt','a',encoding='utf-8') as f:
   #     f.write(json.dumps(content,ensure_ascii=False) + '\n')