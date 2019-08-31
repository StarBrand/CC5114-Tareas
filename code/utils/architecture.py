from utils.math_functions import tanh, sigmoid


SHORT = {
    "LR": 0.05,
    "INTERNAL_LAYERS": [6],
    "ACT_FUNCS": [tanh, sigmoid]
}

LONG = {
    "LR": 0.05,
    "INTERNAL_LAYERS": [10, 6, 5, 6, 4],
    "ACT_FUNCS": [sigmoid, tanh, tanh, tanh, tanh, sigmoid]
}

BIG = {
    "LR": 0.05,
    "INTERNAL_LAYERS": [50, 20, 8],
    "ACT_FUNCS": [tanh, tanh, tanh, sigmoid]
}
