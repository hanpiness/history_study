#from matplotlib import pyplot as plt
#import random

##解决中文显示问题，目前只知道黑体可行
#plt.rcParams['font.sans-serif']=['SimHei']


#y= [random.randint(20,35) for i in range(120)]
#x = range(0,120)
##设置图片大小,dpi为设置清晰度
#plt.figure(figsize=(20,8),dpi=100)
##-->通过实例化一个figure并且传递参数,能够在后台自动使用该figure实例
##-->在图像模糊时可以传入dpi参数，让图片清晰  

##绘图
#plt.plot(x,y)#还可以传入color和linestyle设置颜色和折线格式
              #linewidth线条粗细，alpha透明度

#plt.plot(x,y)如果要两个折线则调用两次

##设置x,y轴的刻度
#_x = list(x)
#_xtick_labels = ["10点{}分".format(i) for i in range(60)]
#_xtick_labels += ["11点{}分".format(i) for i in range(60)]

#plt.yticks(range(20,36))
#plt.xticks(_x[::5],_xtick_labels[::5],rotation=270)#rotation旋转的度数

##取步长，数字和字符串一一对应，数据的长度一样

##添加描述信息
#plt.xlabel("时间")
#plt.ylabel("温度 单位('c')")
#plt.title("十点到十二点每分钟的气温变化情况")

##绘制网格

#plt.grid(alpha = 0.4)
#alpha网格线的清晰程度

##图例

#plt.legend() loc='upper left'设置位置
 
##保存
##plt.savefig("./t1.png") #可以保存为 svg这种矢量图格式,放大不会有锯齿
##plt.savefig("./t2.svg")
##显示图形
#plt.show()

#from matplotlib import pyplot as plt

#x=range(11,31)
#y1=[1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
#y2=[1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]
#plt.rcParams['font.sans-serif'] = ['SimHei']

#plt.figure(figsize =(20,8),dpi = 80)

#_x = x
#x_lables = ["{}岁".format(i) for i in range(11,30)]

#plt.xticks(_x,x_lables,rotation=270)
#plt.yticks(range(0,6))

#plt.grid(alpha=0.4)

#plt.xlabel("岁数")
#plt.ylabel("个数")

#plt.plot(x,y1,label="自己",color='orange',linestyle=':')
#plt.plot(x,y2,label="同桌",color='blue',linestyle='-.')

##图例
#plt.legend(loc='upper left') 
#plt.savefig('.test2.svg' )
#plt.show();

#绘制散点图

#from matplotlib import pyplot as plt
#from matplotlib import font_manager

#a=[11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,10,21,13,33,4,33]
#b=[26,26,28,29,19,21,17,16,19,18,20,20,19,12,3,45,54,54,54,3,22,32,12,32,23,23,21,12,32,1,21]
#x = range(1,32)
#x_10 = range(51,82)
##设置图形大小
#plt.rcParams['font.sans-serif']=['SimHei']
#plt.figure(figsize=(20,8),dpi=80)

##绘制散点图
#plt.scatter(x,a,label="3月份")
#plt.scatter(x_10,b,label="10月份")
##设置x轴坐标
#_x=list(x)+list(x_10)
#_xtick_lables = ["3月{}日".format(i) for i in x]
#_xtick_lables +=["10月{}日".format(i) for i in x_10]
#plt.xticks(_x,_xtick_lables,rotation=270)

##添加图例
#plt.legend()

##绘制标题
#plt.xlabel("时间")
#plt.ylabel("温度")
#plt.title("标题")

#plt.show()

#绘制条形图
#from matplotlib import pyplot as plt
#import numpy as np


#plt.rcParams['font.sans-serif']=['SimHei']
#x = ["战狼2","哪吒之魔童降世","流浪地球","复仇者联盟4：终局之战","红海行动","美人鱼","唐人街探案2","我和我的祖国","我不是药神","中国机长","速度与激情8","西虹市首富","速度与激情7","捉妖记","复仇者联盟3：无限战争","捉妖记2","羞羞的铁拳","疯狂的外星人","海王","变形金刚4：绝迹重生"]
#y = np.array([56.39,49.34,46.18,42.05,36.22,33.9,33.71,31.46,30.75,28.84,26.49,25.27,24.26,24.21,23.7,22.19,21.9,21.83,19.97,19.79])
#plt.figure(figsize = (15,10),dpi = 80)
#plt.barh(range(len(x)),y,linewidth = 0.3,color = 'black')
#plt.yticks(range(len(x)),x)
#plt.grid(alpha = 0.4)
#plt.savefig('move.svg')
#plt.show()

#绘制多个条形图在同一个图上

#from matplotlib import pyplot as plt

#a = ["战狼2","哪吒之魔童降世","流浪地球","复仇者联盟4：终局之战"]

#plt.rcParams['font.sans-serif'] = ['SimHei']

#b_14 = [2358,399,2358,362]
#b_15 = [12357,156,2045,168]
#b_16 = [15746,312,4497,319]

#bar_width = 0.2

#x_14 = list(range(len(a)))
#x_15 = [i+bar_width for i in x_14]
#x_16 = [i+bar_width *2 for i in x_14]


#plt.figure(figsize = (20,8),dpi = 80)
#plt.bar(range(len(a)),b_14,width = bar_width,label ="9月14日")
#plt.bar(x_15,b_15,width = bar_width,label ="9月15日")
#plt.bar(x_16,b_16,width = bar_width,label ="9月16日")

#plt.xticks(x_15,a,rotation = 270)
#plt.legend()
#plt.show()

#绘制直方图
#from matplotlib import pyplot as plt
#import random
#a = [random.randint(80,150) for i in range(250)]

##计算组数
#d = 5 #组距
#num_bins = (max(a)-min(a))//d

#plt.figure(figsize = (20,8),dpi = 80)
#plt.hist(a,num_bins)
#plt.xticks(range(min(a),max(a)+d,d))
#plt.grid()
#plt.show()

#from matplotlib import pyplot as plt

#a = [0,5,10,15,20,25,30,35,40,45,60,90,150]
#width = [5,5,5,5,5,5,5,5,5,15,30,60]
#quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]
#plt.figure(figsize = (20,8),dpi= 80)
#_x = [i-0.5 for i in range(13)]
#plt.xticks(_x,a)
#plt.grid()
#plt.bar(range(len(quantity)),quantity,width = 1)
#plt.show()

import nltk