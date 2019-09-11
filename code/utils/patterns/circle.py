"""circle.py: Circle Pattern class"""
import numpy as np
from math import sqrt, pow
from utils.patterns import Pattern


class Circle(Pattern):
    """Circle, define points inside and outside a circle"""

    def __init__(self, radius: float, center: (float, float), x_range: (float, float), y_range: (float, float)):
        radius = abs(radius)
        assert x_range[0] <= center[0] <= x_range[1]
        assert y_range[0] <= center[1] <= y_range[1]
        assert (x_range[1] - x_range[0]) >= radius
        assert (y_range[1] - y_range[0]) >= radius
        super(Circle, self).__init__(x_range, y_range, "Circle")
        self.r = radius
        self.k = center[0]
        self.h = center[1]

    def x_to_y(self, x: float) -> [float]:
        """
        Gives y values from x value

        :param x: abscissa coordinate
        :return: ordinate coordinate
        """
        aux = pow(self.r, 2) - pow(x - self.k, 2)
        if aux < 0:
            return []
        return [self.h - sqrt(aux), self.h + sqrt(aux)]

    def y_to_x(self, y: float) -> [float]:
        """
        Gives x values from y value

        :param y: ordinate coordinate
        :return: abscissa coordinate
        """
        aux = pow(self.r, 2) - pow(y - self.h, 2)
        if aux < 0:
            return []
        return [self.k - sqrt(aux), self.k + sqrt(aux)]

    # outside
    def is_above(self, x: float, y: float) -> bool:
        """
        Return if a given point is outside of circle

        :param x: x coordinate
        :param y: y coordinate
        :return: Whether the point is outside
        """
        ans = True
        for index, y_candid in enumerate(self.x_to_y(x)):
            if index == 0:
                ans = y < y_candid
            else:
                ans = ans or y > y_candid
        return ans

    def graph(self) -> ([float], [float]):
        """
        Gives values to be graph

        :return: Two arrays to be used for graphic pattern
        """
        start = max(self.x_range[0], self.k - self.r)
        end = min(self.x_range[1], self.k + self.r)
        x_in = list(np.linspace(start, end, int(1e6)))
        x_out = list(np.linspace(end, start, int(1e6)))
        y_aux = [(y[0], y[1]) for y in [self.x_to_y(x) for x in x_in]]
        y_in = [y for y, _ in y_aux]
        y_out = [y for _, y in y_aux]
        return x_in + x_out, y_in + y_out
