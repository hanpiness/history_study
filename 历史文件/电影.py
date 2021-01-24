from selenium import webdriver
from bs4 import BeautifulSoup

borwser = webdriver.Chrome()
borwser.get('http://58921.com/alltime')
html = borwser.page_source
mysoup = BeautifulSoup(html,'lxml')
item = mysoup.find(attrs={'class':'center_table movie_box_office_stats_table table table-bordered table-condensed'})
values = item.find_all('a')
for value in values:
    if value.get_text() != '数据纠错':
        print('"'+value.get_text()+'"'+',')
