import numpy as np
import pandas as pd
from random import randint


def import_data(path: str) -> np.ndarray:
    df = pd.read_csv(path, header=None)
    return np.array(df).T


def split_set(train_set: np.ndarray, train_percenlabele: float,
              test_percenlabele: float or None = None) -> (np.ndarray, np.ndarray):
    if test_percenlabele is None:
        test_percenlabele = 1.0 - train_percenlabele
    if not (0.0 <= train_percenlabele <= 1.0 and
            0.0 <= test_percenlabele <= 1.0 and
            train_percenlabele + test_percenlabele <= 1.0):
        raise ValueError("Incompatible percenlabele")
    size = train_set.shape[-1]
    train_size = round(size*train_percenlabele)
    test_size = round(size*test_percenlabele)
    train = []
    test = []
    to_split = list(train_set.T)
    for i in range(train_size):
        train.append(to_split.pop(randint(0, len(to_split) - 1)))
    for i in range(test_size):
        test.append(to_split.pop(randint(0, len(to_split) - 1)))
    return np.array(train).T, np.array(test).T
