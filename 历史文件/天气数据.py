import json
import requests as reqs
import re
import time
import random


def getCity():
  html = reqs.get('https://tianqi.2345.com/js/citySelectData.js').content
  text = html.decode('gbk')
  city = re.findall('([1-5]\d{4})\-[A-Z]\s(.*?)\-\d{5}',text)  #只提取了地级市及以上城市的名称和代码，5以上的是县级市  
  city = list(set(city))                    #去掉重复城市数据
  print('城市列表获取成功')
  return city


def write_to_txt(products):
    with open('天气预报.txt','a',encoding='utf-8')as f:
        f.write(json.dumps(products,ensure_ascii=False)+'\n')



def getHtml(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    request = reqs.get(url,headers = header)
    text = request.content.decode('gbk')  #经试解析，这里得用gbk模式
    time.sleep(0.3)       #随机暂停
    return text


def getDf(html):    
    pa = re.compile(r'{(ymd.+?)}')                     #用'{ymd'打头，把不是每日天气的其它数据忽略掉
    text = re.findall(pa,html)
    text1 = re.search("city:'(.*?)'",html)
    for item in text:
        s = item.split(',')                            #分割成每日数据
        d = [i.split(':') for i in s]                  #提取冒号前后的数据名称和数据值
        t = {k:v.strip("'").strip('℃') for k,v in d}  #用数据名称和数据值构造字典      
        t.update({"城市":text1.group(1)})
        t["日期"] = t.pop("ymd")
        t["最高气温"] = t.pop('bWendu')
        t["最低气温"] = t.pop('yWendu')
        t["天气"] = t.pop('tianqi')
        del t['fengxiang']
        del t['fengli']
        if 'aqi'in t.keys():
            t["空气质量指数"]=t.pop("aqi")
        else:
            t["空气质量指数"]="无"
        if 'aqiLevel'in t.keys():
            t["空气质量等级"]=t.pop("aqiLevel")
        else:
            t["空气质量等级"]="无"
        if 'aqiInfo'in t.keys():
            t["空气质量"]=t.pop("aqiInfo")
        else:
            t["空气质量"]="无"
        write_to_txt(t)

def getUrls(cityCode):
    urls = []
    for year in range(2011,2020):
        if year <= 2016:
            for month in range(1, 13):
                urls.append('https://tianqi.数字.com/t/wea_history/js/%s_%s%s.js' % (cityCode,year, month))
        else:
            for month in range(1,13):
                if month<10:
                    urls.append('https://tianqi.2345.com/t/wea_history/js/%s0%s/%s_%s0%s.js' %(year,month,cityCode,year,month))                    
                else:
                    urls.append('https://tianqi.2345.com/t/wea_history/js/%s%s/%s_%s%s.js' %(year,month,cityCode,year,month))
    write_to_txt(urls)

if __name__ =="__main__":
    citys = [('57865', '永州')]
    urls = []
    count = 0
    for city in citys:
        for year in range(2011,2021):
            if year <= 2016:
                for month in range(1, 13):
                    urls.append('https://tianqi.2345.com/t/wea_history/js/%s_%s%s.js' % (city[0],year, month))
                    count = count+1
            elif year==2020:
                for month in range(1,4):
                    urls.append('https://tianqi.2345.com/t/wea_history/js/%s0%s/%s_%s0%s.js' %(year,month,city[0],year,month))
                    count = count+1
            else:
                for month in range(1,13):
                    if month<10:
                        urls.append('https://tianqi.2345.com/t/wea_history/js/%s0%s/%s_%s0%s.js' %(year,month,city[0],year,month))
                        count = count+1
                    else:
                        urls.append('https://tianqi.2345.com/t/wea_history/js/%s%s/%s_%s%s.js' %(year,month,city[0],year,month))
                        count = count+1
    for i in range(0,111):
       html = getHtml(urls[i])
       print('开始爬取下一页')
       getDf(html)
