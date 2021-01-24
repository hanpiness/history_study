import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from sklearn.preprocessing  import scale
def loss(x,y,w,b):
    err = model(x,w,b) - y
    squared_err = tf.square(err)
    return tf.reduce_mean(squared_err)

def grad(x,y,w,b):
    with tf.GradientTape() as tape:
        loss_ = loss(x,y,w,b)
    return tape.gradient(loss_,[w,b])

def model(x,w,b):
    return tf.matmul(x,w) + b

df = pd.read_csv("C:/Users/92149/Desktop/data/boston.csv",header = 0)
ds = df.values # df.values以np.array形式返回数据集的值
# x_data 为前12列特征数据
x_data = ds[:,:12]

# y_data 为最后1列标签数据
y_data = ds[:,12]
for i in range(12):
    x_data[:,i] = ((x_data[:,i]-x_data[:,i].min())/(x_data[:,i].max()-x_data[:,i].min()))

train_num = 300 # 训练集的数目
valid_num = 100 # 验证集的数目
test_num = len(x_data) - train_num - valid_num  # 测试集的数目

# 训练集划分
x_train = x_data[:train_num]
y_train = y_data[:train_num]

# 验证集划分
x_valid = x_data[train_num:train_num + valid_num]
y_valid = y_data[train_num:train_num + valid_num]

# 测试机划分
x_test = x_data[train_num + valid_num:train_num + valid_num + test_num]
y_test = x_data[train_num + valid_num:train_num + valid_num + test_num]

x_train = tf.cast(x_train, dtype=tf.float32)
x_valid = tf.cast(x_valid, dtype=tf.float32)
x_test = tf.cast(x_test, dtype=tf.float32)

W = tf.Variable(tf.random.normal([12,1],mean=0.0,stddev=1.0,dtype=tf.float32))
B = tf.Variable(tf.zeros(1),dtype=tf.float32)

training_epochs = 50 # 迭代次数
learning_rate = 0.001 #学习率
batch_size = 10 # 批量训练一次的样本数
optimizer = tf.keras.optimizers.SGD(learning_rate)   #创建优化器，指定学习率
loss_list_train = []   # 用于保存训练集loss值的列表
loss_list_valid = []   # 用于保存验证集loss值的列表
total_step = int(train_num/batch_size)

for epoch in range(training_epochs):
    for step in range(total_step):
        xs = x_train[step*batch_size:(step+1)*batch_size,:]
        ys = y_train[step*batch_size:(step+1)*batch_size]
        grads = grad(xs,ys,W,B)   #计算梯度
        optimizer.apply_gradients(zip(grads,[W,B]))
        
    loss_train = loss(x_train,y_train,W,B).numpy()   #计算当前轮训练损失
    loss_valid = loss(x_valid,y_valid,W,B).numpy()   #计算当前轮验证损失
    loss_list_train.append(loss_train)
    loss_list_valid.append(loss_valid)
    print("epoch={:3d},train_loss={:.4f},vaild_loss={:4f}".format((epoch+1),loss_train,loss_valid))
