from collections import Counter
from math import sqrt
import numpy as np
from .mytrics import accuracy_score


class KNNClassifier:
    def __init__(self, k):
        """初始化KNN分类器"""
        assert k >= 1, "k must be valid"
        self.k = k
        self._x_train = None
        self._y_train = None

    def fit(self, x_train, y_train):
        """根据训练数据集x_train和y_train训练KNN分类器"""
        assert x_train.shape[0] == y_train.shape[0]
        assert self.k <= x_train.shape[0]
        self._x_train = x_train
        self._y_train = y_train
        return self

    def predict(self, x_predict):
        """给定待预测数据集x_predict，返回表示x_predict的结果向量"""
        assert self._x_train is not None and self._x_train is not None
        """must fit before predict"""
        assert x_predict.shape[1] == self._x_train.shape[1]
        """the feature number of x_predict must be equal to x_train"""

        y_predict = [self._predict(x) for x in x_predict]
        return np.array(y_predict)

    def _predict(self, x):
        assert x.shape[0] == self._x_train.shape[1]
        '''the feature number must be equal to x_train'''
        distances = [sqrt(np.sum((x_train - x) ** 2)) for x_train in self._x_train]
        nearest = np.argsort(distances)
        topK_y = [self._y_train[i] for i in nearest[:self.k]]
        votes = Counter(topK_y)
        return votes.most_common(1)[0][0]

    def score(self, x_test, y_test):
        """根据测试数据集x_test和y_test确定当前模型的准确度"""

        y_predict = self.predict(x_test)
        return accuracy_score(y_test, y_predict)
    
    def __repr__(self):
        return "KNN(k=%d)" % self.k