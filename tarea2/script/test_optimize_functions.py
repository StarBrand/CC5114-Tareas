"""test_optimize_functions.py: Plot functions used on unit test GAEOptimized"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

EPSILON = 1e-2


def _first_fitness(x: np.ndarray or float) -> np.ndarray or float:
    return -(x**2) + (12 * x) + 3.5


def _second_fitness(x: np.ndarray or float) -> np.ndarray or float:
    return ((1/5) * x) + 1


def _first_pareto(x: np.ndarray) -> np.ndarray:
    return np.zeros(x.shape) + 2.0


def _second_pareto(x: np.ndarray) -> np.ndarray:
    bool_vector = np.abs(x - 4) <= EPSILON
    return bool_vector * 10.0


fig = plt.figure(figsize=(40, 20))
fig.subplots_adjust(wspace=0.3)


def main(axes1: Axes, axes2: Axes) -> None:
    """
    Main function

    :param axes1: An Axes (priority and none)
    :param axes2: An Axes (pareto)
    :return: plot
    """
    x = np.linspace(-1, 11, 500)
    axes1.plot(x, _first_fitness(x), label="Compare on priority", c="b", linewidth=3.5)
    axes1.plot(x, _second_fitness(x), label="Compare on minimum", c="r", linewidth=3.5)
    axes1.plot([0, 0], [_first_fitness(-1), _first_fitness(0)], c="k")
    axes1.plot([10, 10], [_first_fitness(-1), _first_fitness(10)], c="k")

    axes2.plot(x, _first_pareto(x), label="Constant", c="b", linewidth=3.5)
    axes2.plot(x, _second_pareto(x), label="With maximum", c="r", linewidth=3.5)
    axes2.plot([0, 0], [0, 2], c="k")
    axes2.plot([10, 10], [0, 2], c="k")


def add_stuff(axes: Axes) -> None:
    """
    Add labels, legend and grid to axes

    :param axes: Axes
    :return: None
    """
    axes.set_xlabel("x", fontsize=30)
    axes.set_ylabel("fitness", fontsize=30)
    axes.tick_params(labelsize=20)
    axes.legend(fontsize=30)
    axes.grid()


if __name__ == '__main__':
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    main(ax1, ax2)

    add_stuff(ax1)
    add_stuff(ax2)

    plt.savefig("../results/plot_for_unittest.png")
