"""set_functions.py: useful methods for dataset"""
import numpy as np
import pandas as pd


def import_data(path: str, sep: str = ",", header: int or None = None) -> np.ndarray:
    """
    Import dataset as numpy array from path

    :param path: Path of dataset
    :param sep: Character that separates columns ("," by default)
    :param header: If has a header, index of row, otherwise None
    :return: Dataset as numpy array
    """
    df = pd.read_csv(path, header=header, sep=sep)
    return np.array(df).T


def split_set(train_set: np.ndarray, train_percentage: float,
              test_percentage: float or None = None) -> (np.ndarray, np.ndarray):
    """
    Split dataset in train set and test set

    :param train_set: Set to be split
    :param train_percentage: Percentage of dataset size that will be on train set
    :param test_percentage: (Optional) Percentage of dataset size that will be on test set
                            if None given, calculated from train_percentage
    :return: Tuple of train and test set
    """
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
