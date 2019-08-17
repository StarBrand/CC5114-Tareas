import numpy as np


def sigmoid(z: np.array) -> np.array:
    return np.array(1.0 / (1.0 + np.exp(-z)))


def tanh(z: np.array) -> np.array:
    return np.tanh(z)

#  Derivative


def d_sigmoid(output: np.array) -> np.array:
    return np.multiply(output, 1 - output)


def d_tanh(output: np.array) -> np.array:
    return 1 - np.power(output, 2)

# Pairs


derivative = {
    sigmoid: d_sigmoid,
    tanh: d_tanh
}

proper_name = {
    sigmoid: "sigmoid layer",
    tanh: "tanh layer"
}
