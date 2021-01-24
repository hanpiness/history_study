#   Selenium


#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.wait import WebDriverWait

#browser = webdriver.Chrome()
#try:
#    browser.get('https://www.baidu.com')
#    input = browser.find_element_by_id('kw')
#    input.send_keys('Python')
#    input.send_keys(Keys.ENTER)
#    wait = WebDriverWait(browser,10)
#    wait.until(EC.presence_of_element_located((By.ID,'content_left')))
#    print(browser.current_url)
#    print(browser.get_cookies())
#    print(browser.page_source)
#finally:
#    browser.close()

#   1、声明浏览器对象
#from selenium import webdriver

#browser = webdriver.Chrome()

# 这样就完成了浏览器对象的初始化并将其赋值为browser对象

#   2、访问页面
#from selenium import webdriver

#browser = webdriver.Chrome()
#browser.get('https://www.taobao.com')
#print(browser.page_source)
#browser.close()

# 用get的方法请求网页，参数传入链接URL即可。
# page_source网页的源代码

#   3、查找节点
#   《1》单个节点
#from selenium import webdriver

#browser = webdriver.Chrome()
#browser.get('https://www.taobao.com')
#input_first = browser.find_element_by_id('q')
#input_second = browser.find_element_by_css_selector('#q')
#input_third = browser.find_element_by_xpath('//*[@id="q"]')
#print(input_first,input_second,input_third)
#browser.close()

# find_element_by_name()是根据name的值获取
# find_element_by_id()是根据id的值获取
# 还有根据Xpath、CSS选择器等获取的方式

#from selenium import webdriver
#from selenium.webdriver.common.by import By

#broswer = webdriver.Chrome()
#broswer.get('https://www.taobao.com')
#input_first = broswer.find_element(By.ID,'q')
#print(input_first)
#broswer.close()

# find_element()需要传入两个参数:查找方式(By)和值

#   《2》多个节点
#from selenium import webdriver
#from selenium.webdriver.common.by import By

#browser = webdriver.Chrome()
#browser.get('https://www.taobao.com')
#lis = browser.find_elements(By.CSS_SELECTOR,'.service-bd li')
#print(lis)
#browser.close()

# 如果有多个节点，需要用find_elements()这样的方法

#   《3》节点交互
#from selenium import webdriver
#import time
#from selenium.webdriver.common.by import By

#browser = webdriver.Chrome()
#browser.get('https://www.taobao.com')
#input = browser.find_element(By.ID,'q')
#input.send_keys('iphone')
#time.sleep(1)
#input.clear()
#input.send_keys('iPad')
#button = browser.find_element(By.CLASS_NAME,'btn-search')
#button.click()

# 输入文字时用send_keys()方法
# 清空文字用clear()方法
# 点击按钮时用click()方法

#   《4》动作链
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver import ActionChains

#browser = webdriver.Chrome()
#url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
#browser.get(url)
#browser.switch_to_frame('iframeResult')
#source = browser.find_element(By.CSS_SELECTOR,'#draggable')
#target = browser.find_element(By.CSS_SELECTOR,'#droppable')
#actions = ActionChains(browser)
#actions.drag_and_drop(source,target)
#actions.perform()

# 声明ActionChains对象并将其赋值为actions变量
# 然后通过调用drag_and_drop(第一个参数要拖拽的节点，第二个参数目标节点)方法
# 再调用perform()方法执行动作

#   《5》执行JavaScript
# 下拉进度条selenium并没有提供，它可以直接模拟运行JavaScript
#from selenium import webdriver

#browser = webdriver.Chrome()
#browser.get('https://www.zhihu.com/explore')
#browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#browser.execute_script('alert("To Bottom")')

# 使用execute_script()方法将进度条下拉到最底部，然后弹出alert提示框
