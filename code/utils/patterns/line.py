from random import uniform
from utils.patterns import Pattern


class Line(Pattern):

    def __init__(self, m_range: (float, float),
                 n_range: (float, float),
                 x_range: (float, float),
                 y_range: (float, float)):
        super(Line, self).__init__(x_range, y_range, "Line")
        self.m = uniform(m_range[0], m_range[1])
        self.n = uniform(n_range[0], n_range[1])
        return

    def x_to_y(self, x: float) -> [float]:
        return [(self.m * x) + self.n]

    def y_to_x(self, y: float) -> [float]:
        return [(y - self.n) / self.m]

    def _define_point(self, candid_x: float) -> (float, float):
        candid = self.x_to_y(candid_x)[0]
        if candid > 0:
            if candid < self.y_range[1]:
                point = (candid_x, candid)
            else:
                point = (self.y_to_x(self.y_range[1])[0], self.y_range[1])
        else:
            if candid > self.y_range[0]:
                point = (candid_x, candid)
            else:
                point = (self.y_to_x(self.y_range[0])[0], self.y_range[0])
        return point

    def is_above(self, x: float, y: float) -> bool:
        return y > ((x * self.m) + self.n)

    def graph(self) -> ([float], [float]):
        first_point = self._define_point(self.x_range[0])
        second_point = self._define_point(self.x_range[1])
        return [first_point[0], second_point[0]], [first_point[1], second_point[1]]
