"""one_hot_encoding.py: one_hot_encoding method"""
import numpy as np


def one_hot_encoding(label_vector: np.ndarray or list) -> (np.ndarray or list, dict):
    """
    Receive a vector (or a multi-array) and generate a one hot encoding array
    One hot encoding array: array with shape: (original shape, unique class)
    that has a 1.0 if original data is from class or 0.0 otherwise

    :param label_vector: Vector to be encoded (as array or list)
    :return: Tuple of encoded vector (as array or list respectively) and code as dictionary
    """
    vector = label_vector.copy()
    one_more = False
    if type(vector) == list:
        vector = np.array(vector)
        one_more = True
    if np.ndim(vector) != 1:
        shape = vector.shape + (-1, )
        vector = vector.reshape(-1)
        output, encoding = _one_hot_encoding_one_dim(vector)
        output = output.reshape(shape)
    else:
        output, encoding = _one_hot_encoding_one_dim(vector)
    if one_more:
        return output.tolist(), encoding
    return output, encoding


def _one_hot_encoding_one_dim(vector: np.ndarray) -> (np.ndarray, dict):
    elements = np.unique(vector)
    encoding = dict()
    for index, element in enumerate(elements):
        one_hot = np.zeros(elements.shape[0])
        one_hot[index] = 1.0
        encoding[element] = one_hot.copy()
    return np.array([encoding[element] for element in vector]), encoding
