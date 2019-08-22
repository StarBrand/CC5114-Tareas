import numpy as np
import matplotlib.pyplot as plt
from utils.patterns import Pattern

FIG_SIZE = (12, 12)
FONT_SIZE = 14


def plot_result(x_input: np.ndarray, prediction: np.ndarray, pattern: Pattern, path: str) -> None:

    fig, ax = plt.subplots(figsize=FIG_SIZE)

    x1 = []
    y1 = []
    x2 = []
    y2 = []

    for index, up in enumerate(prediction):
        if up > 0.5:
            x1.append(x_input[0][index])
            y1.append(x_input[1][index])
        else:
            x2.append(x_input[0][index])
            y2.append(x_input[1][index])

    ax.plot(x1, y1, '*', label="Above prediction")
    ax.plot(x2, y2, '*', label="Below prediction")
    pattern.add_results(ax)

    ax.set_xlabel("x", fontsize=FONT_SIZE)
    ax.set_ylabel("y", fontsize=FONT_SIZE)
    ax.grid()
    ax.legend(fontsize=FONT_SIZE)
    plt.savefig(path)

    return
