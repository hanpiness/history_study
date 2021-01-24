import json
from urllib.request import urlopen,quote
import requests,csv
import time


# 构造经纬度获取函数
def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoding/v3/'
    output = 'json'
    ak = 'txrm69lvmWHa66jgClsR1F8yuVfhKNkK'
    add = quote(address)  # 由于本文城市变量为中文
    uri = url+'?'+'address='+add+'&output='+output +'&ak='+ak
    req = urlopen(uri)
    res = req.read().decode()
    temp = json.loads(res)
    return temp
# 批量获取城市经纬度坐标
file = open(r'.\\point.txt','w') # 建立json数据文件
with open(r'C:\\Users\\92149\\Desktop\\BaiduMap_cityCode_1102.csv','r',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        b = line[1].strip()
        c = getlnglat(b)
        if(c['status']!=1):
            lng = c['result']['location']['lng']
            lat = c['result']['location']['lat']
        time.sleep(0.1)
        str_temp = '{"lat":' + str(lat) + ',"lng":' + str(lng) + "loc:" + b + '},' + '\n'
        print(str_temp)

        file.write(str_temp) # 写入文档
file.close
