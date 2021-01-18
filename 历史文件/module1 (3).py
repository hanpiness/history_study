import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(4)

x_data = np.linspace(0,100,500)

y_data = x_data * 3.1234 + 2.98 + np.random.randn(*x_data.shape)*0.4

x_data_1 = x_data

y_data_1 = y_data

x_data = (x_data - x_data.min())/(x_data.max()-x_data.min())

y_data = x_data * 3.1234 + 2.98 + np.random.randn(*x_data.shape)*0.4
# 构建回归模型
def model(x,w,b):
    return tf.multiply(x,w) + b

def loss(x,y,w,b):
    err = model(x,w,b) - y
    square_err = tf.square(err)
    return tf.reduce_mean(square_err)

def grad(x,y,w,b):
    with tf.GradientTape() as tape:
        loss_ = loss(x,y,w,b)
    return tape.gradient(loss_,[w,b])

w = tf.Variable(1.0,tf.float32)
b = tf.Variable(0.0,tf.float32)

training_epochs = 10
learning_rate = 0.001

step = 0
loss_list = []
display_step = 20

for epoch in range(100):
    for xs,ys in zip(x_data,y_data):
        loss_ = loss(xs,ys,w,b)
        loss_list.append(loss_)

        delta_w,delta_b = grad(xs,ys,w,b)
        change_w = delta_w * learning_rate
        change_b = delta_b * learning_rate
        w.assign_sub(change_w)
        b.assign_sub(change_b)

        step = step+1
        #if step % display_step == 0:
        #    print("Training Epoch:",'%02d'%(epoch+1),"Step: %03d"%(step),"loss:%.6f" %(loss_))
    plt.plot(x_data,w.numpy() * x_data + b.numpy())
print("w:%f"%w.numpy())
print("b:%f"%b.numpy())
x = 5.79
y = w*x+b
print("preduct:",y)
print("real:",(x * 3.1234 + 2.98))
plt.show()
plt.scatter(x_data_1,y_data_1,10)
plt.plot(x_data_1,x_data_1 * 3.1234 + 2.98,linewidth=0.3,color='g')
plt.plot(x_data_1,x_data_1 * w.numpy() + b.numpy(),color='g',linewidth = 0.3)
plt.show()