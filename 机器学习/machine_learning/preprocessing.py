import numpy as np


class StandardScaler:

    def __init__(self):
        self.mean_ = None
        self.scale_ = None

    def fit(self, x):
        """根据训练数据集x获得数据均值和方差"""
        assert x.ndim == 2, "The dimension of x must be 2"

        self.mean_ = np.array([np.mean(x[:, i]) for i in range(x.shape[1])])
        self.scale_ = np.array([np.array([np.std(x[:, i]) for i in range(x.shape[1])])])

        return self

    def transform(self, x):
        """将x根据这个StandardScaler进行均值方差归一化处理"""
        assert x.ndim == 2, "The dimension of x must be 2"
        assert self.mean_ is not None and self.scale_ is not None, \
            "must fit before transform"
        assert x.shape[1] == len(self.mean_), \
            "the feature number of x must be equal to mean_ and std_"
        mean_ = self.mean_
        for i in range(x.shape[0]):
            np.vstack(mean_, self.mean_)

        scale_ = self.scale_
        for i in range(x.shape[0]):
            np.vstack(scale_, self.scale_)
        for col in range(x.shape[1]):
            x[:, col] = ((x[:, col] - mean_[:, col]) / self.scale_[:, col])

        return x
