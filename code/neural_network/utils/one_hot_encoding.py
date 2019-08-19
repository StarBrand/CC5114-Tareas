import numpy as np


def one_hot_encoding(label_vector: np.ndarray or list) -> np.ndarray or list:
    vector = label_vector.copy()
    one_more = False
    if type(vector) == list:
        vector = np.array(vector)
        one_more = True
    if np.ndim(vector) != 1:
        shape = vector.shape + (-1, )
        vector = vector.reshape(-1)
        output = _one_hot_encoding_one_dim(vector).reshape(shape)
    else:
        output = _one_hot_encoding_one_dim(vector)
    if one_more:
        return output.tolist()
    return output


def _one_hot_encoding_one_dim(vector: np.ndarray) -> np.ndarray:
    elements = np.unique(vector)
    encoding = dict()
    for index, element in enumerate(elements):
        one_hot = np.zeros(elements.shape[0])
        one_hot[index] = 1.0
        encoding[element] = one_hot.copy()
    return np.array([encoding[element] for element in vector])
