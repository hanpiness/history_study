#import matplotlib.pyplot as plt
#import tensorflow as tf
#import numpy as np

#def model(x,w,b):
#    return tf.multiply(x,w) + b

#def loss(x,y,w,b):
#    err = model(x,w,b) - y   #计算模型预测值和标签值的差异
#    squared_err = tf.square(err)  #求平方，得出方差
#    return squared_err  #求均值,得出均方差

#def grad(x,y,w,b):
#    with tf.GradientTape() as tape:
#        loss_ = loss(x,y,w,b)
#    return tape.gradient(loss_,[w,b])   # 返回梯度向量

## 设置随机数种子
#np.random.seed(5)

## 直接采用np生成等差数列的方法，生成100个点，每个点的取值在-1~1之间
#x_data = np.linspace(-1,1,100)

## y=2x+1 +噪声 其中噪声的维度与x_data一致
#y_data = 2 * x_data + 1.0 + np.random.randn(*x_data.shape) * 0.4

## 构建线性函数的斜率，变量w
#w = tf.Variable(1.0,tf.float32)
## 构建线性函数的截距，变量b
#b = tf.Variable(0.0,tf.float32)

#training_epochs = 10  # 迭代次数(训练轮数)
#learning_rate = 0.01  # 学习率

#step = 0  #记录训练的步数
#loss_list = []  #用于保存loss值的列表
#display_step = 10 # 控制训练过程数据显示的频率，不是超参数

#for epoch in range(100):
#    for xs,ys in zip(x_data,y_data):
#        loss_ = loss(xs,ys,w, b)   #计算损失
#        loss_list.append(loss_)    #保存本次损失计算结果
        
#        delta_w,delta_b = grad(xs,ys,w,b)   #计算当前[w,b]点的梯度
#        change_w = delta_w * learning_rate  #计算变量w需要改变的量
#        change_b = delta_b * learning_rate  #计算变量b需要改变的量
#        w.assign_sub(change_w)              #变量w值变更为减去change_w后的值
#        b.assign_sub(change_b)              #变量b值变更为减去change_w后的值
        
#        step = step+1                       #训练步数加一
#    plt.plot(x_data,w.numpy() * x_data + b.numpy())    # 完成一轮训练后，画出图像
#plt.show()


#import matplotlib.pyplot as plt
#import tensorflow as tf
#import numpy as np

#def model(x,w,b):
#    return tf.multiply(x,w) + b

#def loss(x,y,w,b):
#    err = model(x,w,b) - y   #计算模型预测值和标签值的差异
#    squared_err = tf.square(err)  #求平方，得出方差
#    return tf.reduce_mean(squared_err)  #求均值,得出均方差

#def grad(x,y,w,b):
#    with tf.GradientTape() as tape:
#        loss_ = loss(x,y,w,b)
#    return tape.gradient(loss_,[w,b])   # 返回梯度向量

# 设置随机数种子
#np.random.seed(5)

# 直接采用np生成等差数列的方法，生成100个点，每个点的取值在-1~1之间
#x_data = np.linspace(-1,1,100)

# y=2x+1 +噪声 其中噪声的维度与x_data一致
#y_data = 2 * x_data + 1.0 + np.random.randn(*x_data.shape) * 0.4

## 构建线性函数的斜率，变量w
#w = tf.Variable(1.0,tf.float32)
## 构建线性函数的截距，变量b
#b = tf.Variable(0.0,tf.float32)

#training_epochs = 100  # 迭代次数(训练轮数)
#learning_rate = 0.05  # 学习率

#loss_list = []  #用于保存loss值的列表

#for epoch in range(training_epochs):
#    loss_ = loss(x_data,y_data,w, b)   #计算损失
#    loss_list.append(loss_)    #保存本次损失计算结果
        
#    delta_w,delta_b = grad(x_data,y_data,w,b)   #计算当前[w,b]点的梯度
#    change_w = delta_w * learning_rate  #计算变量w需要改变的量
#    change_b = delta_b * learning_rate  #计算变量b需要改变的量
#    w.assign_sub(change_w)              #变量w值变更为减去change_w后的值
#    b.assign_sub(change_b)              #变量b值变更为减去change_w后的值
    
#    print("Training Epoch：",'%02d'%(epoch+1),"loss=%.6f"%(loss_))
##    plt.plot(x_data,w.numpy() * x_data + b.numpy())    # 完成一轮训练后，画出图像
##plt.show()
#print(w.numpy(),b.numpy())


