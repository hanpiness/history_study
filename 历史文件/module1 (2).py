from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import bs4
import json
 
#共37页进行爬虫
driver = webdriver.Chrome()
driver.get('http://api.map.baidu.com/lbsapi/getpoint/index.html')
time.sleep(5)
element1 = driver.find_element_by_link_text("更换城市")
element1.click()
element2 = driver.find_element_by_link_text("太原")
element2.click()
time.sleep(5)
element3 = driver.find_element_by_id("localvalue")
element3.send_keys("旅馆")
element3.send_keys(Keys.RETURN)     #此步为关键格式！！！这样html内容才会改变
time.sleep(2)
for i in range(15):
    html = driver.page_source
    mysoup = bs4.BeautifulSoup(html,'lxml')
    element = {
        "店名":
        "坐标"
    }
    loc = driver.find_element_by_link_text("下一页")
    loc.click()
    time.sleep(5)
    i += 1
    #with open('商品.txt','a',encoding = 'utf-8') as f:         #'a'以追加模式打开 (从 EOF 开始, 必要时创建新文件)
    #    f.write(json.dumps(element,ensure_ascii=False) + '\n')
