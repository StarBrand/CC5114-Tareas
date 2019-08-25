import numpy as np
from matplotlib.axes import Axes
from utils.patterns import Pattern

FONT_SIZE = 14


def plot_result(x_input: np.ndarray, prediction: np.ndarray, pattern: Pattern,
                ax: Axes or None = None, up_to: float = 0.5) -> float:

    x1 = []
    y1 = []
    x2 = []
    y2 = []
    success = 0

    for index, up in enumerate(prediction):
        if up > up_to:
            x1.append(x_input[0][index])
            y1.append(x_input[1][index])
            if pattern.is_above(x1[-1], y1[-1]):
                success += 1
        else:
            x2.append(x_input[0][index])
            y2.append(x_input[1][index])
            if not pattern.is_above(x2[-1], y2[-1]):
                success += 1

    if ax is not None:
        ax.plot(x1, y1, '.', label="Above prediction")
        ax.plot(x2, y2, '.', label="Below prediction")
        pattern.add_results(ax)

        ax.set_xlabel("x", fontsize=FONT_SIZE)
        ax.set_ylabel("y", fontsize=FONT_SIZE)
        ax.grid()
        ax.legend(fontsize=FONT_SIZE)

    return success / len(prediction)
