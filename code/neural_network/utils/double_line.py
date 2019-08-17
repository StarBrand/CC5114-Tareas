from random import uniform

from matplotlib.axes import Axes

from neural_network.utils import Pattern, Line


class DoubleLine(Pattern):

    def __init__(self, m_range: (float, float),
                 n_range: (float, float),
                 x_range: (float, float),
                 y_range: (float, float)):
        super(DoubleLine, self).__init__(x_range, y_range, "DoubleLine")
        self.m = uniform(m_range[0], m_range[1])
        n1 = uniform(n_range[0], n_range[1])
        n2 = n1 + n_range[1] - n_range[0]
        self.line1 = Line((self.m, self.m), (n1, n1), x_range, y_range)
        self.line2 = Line((self.m, self.m), (n2, n2), x_range, y_range)
        return

    def x_to_y(self, x: float) -> [float]:
        return [self.line1.x_to_y(x)[0], self.line2.x_to_y(x)[0]]

    def y_to_x(self, y: float) -> [float]:
        return [self.line1.y_to_x(y)[0], self.line2.y_to_x(y)[0]]

    # outside
    def is_above(self, x: float, y: float) -> bool:
        return not self.line1.is_above(x, y) or self.line2.is_above(x, y)

    def graph(self) -> ([float], [float]):
        x1, y1 = self.line1.graph()
        x2, y2 = self.line2.graph()
        return x1 + x2, y1 + y2

    def add_results(self, ax: Axes) -> None:
        x, y = self.graph()
        x1 = x[0:2]
        x2 = x[2:4]
        y1 = y[0:2]
        y2 = y[2:4]
        ax.plot(x1, y1, "-", label="Line 1")
        ax.plot(x2, y2, "-", label="Line 2")
