import numpy as np
from random import randint


def split_set(train_set: np.ndarray, train_percentage: float,
              test_percentage: float or None = None) -> (np.ndarray, np.ndarray):
    if test_percentage is None:
        test_percentage = 1.0 - train_percentage
    if not (0.0 <= train_percentage <= 1.0 and
            0.0 <= test_percentage <= 1.0 and
            train_percentage + test_percentage <= 1.0):
        raise ValueError("Incompatible percentage")
    size = train_set.shape[-1]
    train_size = round(size*train_percentage)
    test_size = round(size*test_percentage)
    train = []
    test = []
    to_split = list(train_set.T)
    for i in range(train_size):
        train.append(to_split.pop(randint(0, len(to_split) - 1)))
    for i in range(test_size):
        test.append(to_split.pop(randint(0, len(to_split) - 1)))
    return np.array(train).T, np.array(test).T
