import numpy as np


def sigmoid(z: np.ndarray) -> np.ndarray:
    return np.array(1.0 / (1.0 + np.exp(-z)))


def tanh(z: np.ndarray) -> np.ndarray:
    return np.tanh(z)


def step(z: np.ndarray) -> np.ndarray:
    return np.multiply(z >= 0, 1.0)

#  Derivative


def d_sigmoid(output: np.ndarray) -> np.ndarray:
    ans = sigmoid(output)
    return np.multiply(ans, 1 - ans)


def d_tanh(output: np.ndarray) -> np.ndarray:
    ans = tanh(output)
    return 1 - np.power(ans, 2)


def d_step(output: np.ndarray) -> np.ndarray:
    ans = np.zeros(output.shape)
    ans[output == 0.0] = np.nan
    return ans


# Pairs


derivative = {
    sigmoid: d_sigmoid,
    tanh: d_tanh,
    step: d_step
}

proper_name = {
    sigmoid: "sigmoid layer",
    tanh: "tanh layer",
    step: "perceptron layer",
    None: "no name"
}
