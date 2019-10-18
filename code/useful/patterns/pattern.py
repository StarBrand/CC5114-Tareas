"""pattern.py: Pattern ABC"""
import numpy as np
from matplotlib.axes import Axes
from random import uniform
from abc import ABC, abstractmethod


class Pattern(ABC):
    """Pattern ABC, defines needed methods"""

    def __init__(self, x_range: (float, float), y_range: (float, float), name: str):
        assert (x_range[1] - x_range[0]) > 0
        assert (y_range[1] - y_range[0]) > 0
        self.name = name
        self.x_range = x_range
        self.y_range = y_range

    @abstractmethod
    def x_to_y(self, x: float) -> [float]:
        """
        Gives y values from x value

        :param x: abscissa coordinate
        :return: ordinate coordinate
        """
        pass

    @abstractmethod
    def y_to_x(self, y: float) -> [float]:
        """
        Gives x values from y value

        :param y: ordinate coordinate
        :return: abscissa coordinate
        """
        pass

    @abstractmethod
    def is_above(self, x: float, y: float) -> bool:
        """
        Return if a given point is above pattern

        :param x: x coordinate
        :param y: y coordinate
        :return: Whether the point is above
        """
        pass

    @abstractmethod
    def graph(self) -> ([float], [float]):
        """
        Gives values to be graph

        :return: Two arrays to be used for graphic pattern
        """
        pass

    def add_results(self, ax: Axes) -> None:
        """
        Add pattern to a Axes figure on matplotlib

        :param ax: Axes in which results will be inserted
        :return: None (update ax)
        """
        x, y = self.graph()
        ax.plot(x, y, "-", label=self.name)

    def training_set(self, size: int) -> [(float, float, bool)]:
        """
        Generates training set with random points and labels of pattern

        :param size: Size of training set
        :return: Dataset of patter
        """
        out = []
        for i in range(size):
            x = uniform(self.x_range[0], self.x_range[1])
            y = uniform(self.y_range[0], self.y_range[1])
            datum = x, y, self.is_above(x, y)
            out.append(datum)
        return np.array(out).T
