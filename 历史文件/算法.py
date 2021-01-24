import numpy as np
import matplotlib.pyplot as plt

np.random.seed(272)
data_size_1 = 300
x1_1 = np.random.normal(loc = 5.0, scale = 1.0, size = data_size_1)
x2_1 = np.random.normal(loc = 4.0, scale = 1.0, size = data_size_1)
y_1 = [0 for _ in range(data_size_1)]

data_size_2 = 400
x1_2 = np.random.normal(loc = 10.0, scale = 2.0, size = data_size_2)
x2_2 = np.random.normal(loc = 8.0, scale = 2.0, size = data_size_2)
y_2 = [1 for _ in range(data_size_1)]

x1 = np.concatenate((x1_1,x1_2),axis = 0)
x2 = np.concatenate((x2_1,x2_2),axis = 0)
x = np.hstack((x1.reshape(-1,1),x2.reshape(-1,1)))#让z变成只有一列，行数不知道多少
y = np.concatenate((y_1,y_2),axis = 0)

data_size_all = data_size_1+data_size_2
shuffled_index = np.random.permutation(data_size_all)
x = x[shuffled_index]
y = y[shuffled_index]

split_index = int(data_size_all *0.7)
x_train = x[:split_index]
y_train = y[:split_index]
x_test = x[split_index:]
y_test = y[split_index:]

plt.scatter(x_train[:,0],x_train[:,1],c=y_train,marker='.')
plt.show()
plt.scatter(x_test[:,0],x_test[:,1],c=y_test,marker='.')
plt.show()