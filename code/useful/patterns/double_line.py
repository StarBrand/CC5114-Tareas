"""double_line.py: Double Line Pattern class"""

from random import uniform
from matplotlib.axes import Axes
from useful.patterns import Pattern, Line


class DoubleLine(Pattern):
    """Double Line, define points inside and outside two line on plane"""

    def __init__(self, m_range: (float, float),
                 n_range: ((float, float), (float, float)),
                 x_range: (float, float),
                 y_range: (float, float)):
        super().__init__(x_range, y_range, "DoubleLine")
        self.m = uniform(m_range[0], m_range[1])
        n1 = uniform(n_range[0][0], n_range[0][1])
        n2 = uniform(n_range[1][0], n_range[1][1])
        self.line1 = Line((self.m, self.m), (n1, n1), x_range, y_range)
        self.line2 = Line((self.m, self.m), (n2, n2), x_range, y_range)
        return

    def x_to_y(self, x: float) -> [float]:
        """
        Gives y values from x value

        :param x: abscissa coordinate
        :return: ordinate coordinate
        """
        return [self.line1.x_to_y(x)[0], self.line2.x_to_y(x)[0]]

    def y_to_x(self, y: float) -> [float]:
        """
        Gives x values from y value

        :param y: ordinate coordinate
        :return: abscissa coordinate
        """
        return [self.line1.y_to_x(y)[0], self.line2.y_to_x(y)[0]]

    # outside
    def is_above(self, x: float, y: float) -> bool:
        """
        Return if a given point is above pattern

        :param x: x coordinate
        :param y: y coordinate
        :return: Whether the point is above
        """
        return not self.line1.is_above(x, y) or self.line2.is_above(x, y)

    def graph(self) -> ([float], [float]):
        """
        Gives values to be graph

        :return: Two arrays to be used for graphic pattern
        """
        x1, y1 = self.line1.graph()
        x2, y2 = self.line2.graph()
        return x1 + x2, y1 + y2

    def add_results(self, ax: Axes) -> None:
        """
        Add pattern to a Axes figure on matplotlib

        :param ax: Axes in which results will be inserted
        :return: None (update ax)
        """
        x, y = self.graph()
        x1 = x[0:2]
        x2 = x[2:4]
        y1 = y[0:2]
        y2 = y[2:4]
        ax.plot(x1, y1, "-", label="Line 1")
        ax.plot(x2, y2, "-", label="Line 2")
