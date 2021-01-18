#import numpy as np
#import random

## 生成数组
#a = np.array([1,2,3,4,5])
#print(a)
#print(type(a))
#b = np.array(range(10))
#print(b)
#print(type(b))

##生成一个数组作用和range一样
#c= np.arange(4,10,2)
#print(c)
#print(type(c))
##显示数据类型
#print(c.dtype)
##可以指定数据类型
#d = np.array(range(1,4),dtype = float)
#print(type(d))
#print(d.dtype)
#e = np.array([1,1,1,0,1],dtype = bool)
#print(e.dtype)

##调整数据类型
#e = d.astype("int8")
#print(e.dtype)

#f = np.array([random.random() for i in range(1,10)])
#print(f)
#print(f.dtype)

##保留小数
#g = np.round(f,2)
#print(g)

#import numpy as np
#t1 = np.arange(12)
#print(t1)
#t2 = np.array([[1,2,3],[4,5,6]])
#print(t2)
#print(t2.shape)
##(2,3)代表两行三列的形式
#t3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
#print(t3)
#print(t3.shape)
#t4 = np.arange(12)

#t4 = t4.reshape((3,4))

#t5 = np.arange(24).reshape(2,3,4)

#t5 = t5.reshape((4,6))

## 展开变为一维数组
#t5 = t5.flatten()

##t5 = t5 + 2
##print(t5)

#t5 = t5/2
#print(t5)

#t5 = t5/0
#nan代表不是一个数组，inf无穷大

#import numpy as np

#t5 = np.arange(24).reshape(4,6)
#print(t5)
#t6 = np.arange(100,124).reshape(4,6)
#print(t6)
##当两个数组形状相同的时候对应位置上相乘
#print(t5+t6)
#print(t5*t6)

#t7 = np.arange(0,6)
#print(t5-t7)

#t8 = np.arange(4).reshape(4,1)
#print(t5-t8)

#数组的拼接

#import numpy as np
#t1 = np.arange(1,11)
#t1 = t1.reshape(5,2)
#t2 = np.arange(11,21)
#t2 = t2.reshape(5,2)
#t3 = np.vstack((t1,t2)) #行拼接
#print(t3)
#t4 = np.hstack((t1,t2)) #列拼接
#print(t4)
#t1[[2,3],:] = t1[[3,2],:] #行交换
#print(t1)
#t1[:,[0,1]] = t1[:,[1,0]] #列交换
#print(t1)

#import numpy as np
#t1 = np.arange(1,11)
#t1 = t1.reshape(5,2)
#t2 = np.arange(11,21)
#t2 = t2.reshape(5,2)
#获取最大值最小值的位置
#print(np.argmin(t1,axis=0))#axis=0为列
#print(np.argmin(t1,axis=1))#axis=1为行
#创建一个全为0的数组
#t3 = np.zeros((3,4))
#print(t3)
#创建一个全为1的数组
#t4 = np.ones((3,4))
#print(t4)
#创建一个对角线为1的正方形数组（方阵）
#t5 = np.eye(3)
#print(t5)

#生成随机数
#从给定上下限范围选取随机数整数，范围是low,high,形状是shape
#randint(low,high,shape)
#t3 = np.random.randint(10,20,(4,5))
#print(t3)
#rand(d0,d1,dn)创建do-dn维度的均匀分布的随机数数组，浮点数，范围从0-1
#t4 = np.random.rand(3,10)
#print(t4)
#randn(d0,d1,..dn)创建d0-dn维度的标准正太分布随机数，浮点数，平均数为0，标准差为1
import numpy as np
t5 = np.random.randn(3,10)
print(t5)
#uniform(low,high,size)产生具有均匀分布的数组，low为起始值,high为结束值，size形状
#t6 = np.random.uniform(0,20,(3,4))
#print(t6)
#seed(s)随机种子，s是给定的种子值，通过设定相同的随机种子，可以生成相同的随机数
#np.random.seed(10)
#t = np.random.randint(0,20,(3,4))
#print(t)

#a=b[:],视图的操作，一种切片，会创建新的对象a，
#但是a的数据完全由b保管，他们的数据变化是一致的
#a = b.copy()a与b互不影响

#nan当读取本地的文件为float的时候，如果有缺失，就会出现nan
#当做了一个不合适的计算的时候（比如无穷大减无穷大）
#inf表示正无穷-inf表示负无穷
#比如一个数字除以0
#nan和inf都是浮点类型
#两个nan不相同
#nan和任何值计算都为nan
#np.meana(axis=0)均值
#np.median(t1,axis=0)中值
#np.ptp(t,axis=None)即最大值和最小值之差
#t.std(axis=None)

#import numpy as np

#def fill_ndarray(t1):
#        for i in range(t1.shape[1]):
#            temp_col = t1[:,i]
#            nan_num = np.count_nonzero(temp_col!=temp_col)
#            if nan_num !=0:
#                temp_not_nan_col = temp_col[temp_col==temp_col]
#                temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()
#        return t1

#if __name__ == '__main__':
#   t1 = np.arange(12).reshape((3,4)).astype("float")
#   t1[1,2:] = np.nan
#   print(t1)
#   t1 = fill_ndarray(t1)
#   print(t1)