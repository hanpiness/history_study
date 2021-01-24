from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
import json
from pymongo import MongoClient

browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
KeyWord ='键盘'

MONGO_URL = 'mongodb://localhost:27017/'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products1'
client = MongoClient(MONGO_URL)
db = client[MONGO_DB]

def add_cookies():
    with open('taobao.json','rb') as f:
        cookies = json.load(f)
        for item in cookies:
            browser.add_cookie(item)

def index_page(page):
    print('正在爬取第',page,'页')
    try:
        if page > 1:
            input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager div.form > input')))
            # 找到页面底部页面跳转框
            input.clear()
            input.send_keys(str(page))
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager div.form > span.btn.J_Submit')))
            # 输入页数后点击进行跳转
            submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager li.item.active > span'),str(page)))
        # 判断当前高亮的页码数是当前的页码数即可text_to_be_present_in_element，它会等待指定的文本出现在某一个节点里面是即返回成功
        # 这里我们将高亮的页码节点对应的CSS选择器和当前要跳转的页码通过参数传递给这个等待条件，这样它会检测当前的页码节点是不是我们传来的页码数
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.m-itemlist .items .item')))
        # 我们要等商品信息加载出来，presence_of_element_located
        get_products()
    except TimeoutException:
        index_page(page)
def get_products():
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'price':item.find('.price').text(),
            'deal':item.find('.deal-cnt').text(),
            'title':item.find('.title').text(),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text(),
            }
        print(product)
        save_to_mongo(product)

def save_to_mongo(result):
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('成功')
    except Exception as e:
        print('失败')

MAX_PAGE = 100
if __name__ == '__main__':
    print("淘宝模拟登录，搜索iPad物品")
    browser.get('https://www.taobao.com')
    add_cookies()
    input = browser.find_element_by_id('q')
    input.send_keys(KeyWord)
    button = browser.find_element_by_class_name('btn-search')
    button.click()
    print("淘宝模拟登录成功，查询完毕，现在开始爬取内容")
    for i in range(1,MAX_PAGE+1):
        index_page(i)
    browser.close()
