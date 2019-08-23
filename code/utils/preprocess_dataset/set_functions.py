import numpy as np
import pandas as pd
from random import randint


def import_data(path: str) -> np.ndarray:
    df = pd.read_csv(path, header=None)
    return np.array(df).T


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
    to_split = np.random.permutation(train_set.T)
    return to_split[0:train_size].T, to_split[train_size:train_size + test_size].T
