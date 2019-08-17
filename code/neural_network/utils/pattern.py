import numpy as np
from matplotlib.axes import Axes
from random import uniform
from abc import ABC, abstractmethod


class Pattern(ABC):

    def __init__(self, x_range: (float, float), y_range: (float, float), name: str):
        assert (x_range[1] - x_range[0]) > 0
        assert (y_range[1] - y_range[0]) > 0
        self.name = name
        self.x_range = x_range
        self.y_range = y_range

    @abstractmethod
    def x_to_y(self, x: float) -> [float]:
        return

    @abstractmethod
    def y_to_x(self, y: float) -> [float]:
        return

    @abstractmethod
    def is_above(self, x: float, y: float) -> bool:
        return

    @abstractmethod
    def graph(self) -> ([float], [float]):
        return

    def add_results(self, ax: Axes) -> None:
        x, y = self.graph()
        ax.plot(x, y, "-", label=self.name)

    def training_set(self, size: int) -> [(float, float, bool)]:
        out = []
        for i in range(size):
            x = uniform(self.x_range[0], self.x_range[1])
            y = uniform(self.y_range[0], self.y_range[1])
            datum = x, y, self.is_above(x, y)
            out.append(datum)
        return np.array(out).T
