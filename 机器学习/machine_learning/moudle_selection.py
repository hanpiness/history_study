import numpy as np


def train_test_split(x, y, test_radio=0.2, seed=None):
    """将数据x 和 y  按照test_radio分隔成x_train,x_test,y_train,y_test"""

    assert x.shape[0] == y.shape[0], \
        "the size of x must be equal to the size of y"
    assert 0.0 <= test_radio <= 1.0, \
        "test_ration must be valid"

    if seed:
        np.random.seed(seed)

    shuffle_indexes = np.random.permutation(len(x))

    test_size = int(len(x) * test_radio)
    train_indexes = shuffle_indexes[test_size:]
    test_indexes = shuffle_indexes[:test_size]

    x_test = x[test_indexes]
    y_test = y[test_indexes]

    x_train = x[train_indexes]
    y_train = y[train_indexes]

    return x_train, x_test, y_train, y_test

