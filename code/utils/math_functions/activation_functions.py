import numpy as np


def sigmoid(z: np.ndarray) -> np.ndarray:
    try:
        return np.array(1.0 / (1.0 + np.exp(-z)))
    except TypeError:
        out = _re_cast_to_numpy(z)
        return np.array(1.0 / (1.0 + np.exp(-out)))


def tanh(z: np.ndarray) -> np.ndarray:
    try:
        return np.tanh(z)
    except TypeError:
        out = _re_cast_to_numpy(z)
        return np.tanh(out)


def step(z: np.ndarray) -> np.ndarray:
    return np.multiply(z >= 0, 1.0)

#  Derivative


def d_sigmoid(x: np.ndarray or None = None, output: np.ndarray or None = None) -> np.ndarray:
    if (x is None and output is None) or (x is not None and output is not None):
        raise ValueError("d_sigmoid requires one, and just one, argument")
    if output is not None:
        ans = output
    else:
        ans = sigmoid(x)
    return np.multiply(ans, 1 - ans)


def d_tanh(x: np.ndarray or None = None, output: np.ndarray or None = None) -> np.ndarray:
    if (x is None and output is None) or (x is not None and output is not None):
        raise ValueError("d_tanh requires one, and just one, argument")
    if output is not None:
        ans = output
    else:
        ans = tanh(x)
    return 1 - np.power(ans, 2)


def d_step(x: np.ndarray or None = None, output: np.ndarray or None = None) -> np.ndarray:
    if (x is None and output is None) or (x is not None and output is not None):
        raise ValueError("d_step requires one, and just one, argument")
    if output is not None:
        ans = np.zeros(output.shape)
        ans[output == 0.0] = np.nan
    else:
        ans = np.zeros(x.shape)
        ans[x == 0.0] = np.nan
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


def _re_cast_to_numpy(x: np.ndarray or list) -> np.ndarray:
    return np.array(x.copy()).astype(float)
