import numpy as np
from matplotlib.axes import Axes


def result(predict: callable,
           parameters: dict,
           x: [float], y: [float],
           ax: Axes or None) -> ([float], [float], [float], [float]):

    x1 = []
    y1 = []
    x2 = []
    y2 = []

    for i, _ in enumerate(x):
        x_test = np.array([[x[i]], [y[i]]])
        if predict(x_test, parameters) > 0.5:
            x1.append(x[i])
            y1.append(y[i])
        else:
            x2.append(x[i])
            y2.append(y[i])

    if ax is not None:
        ax.plot(x1, y1, '.')
        ax.plot(x2, y2, '.')

    return x1, y1, x2, y2
