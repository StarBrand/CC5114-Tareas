from random import uniform


class Line(object):

    def __init__(self, m_range: (int, int), n_range: (int, int),
                 x_range: (int, int), y_range: (int, int)):
        self.m = uniform(m_range[0], m_range[1])
        self.n = uniform(n_range[0], n_range[1])
        self.MIN_X = x_range[0]
        self.MAX_X = x_range[1]
        self.MIN_Y = y_range[0]
        self.MAX_Y = y_range[1]

    def line_xtoy(self, x: float) -> float:
        return (self.m * x) + self.n

    def line_ytox(self, y: float) -> float:
        return (y - self.n) / self.m

    def _define_point(self, candid_x: float) -> (float, float):
        candid = self.line_xtoy(candid_x)
        if candid > 0:
            if candid < self.MAX_Y:
                point = (candid_x, candid)
            else:
                point = (self.line_ytox(self.MAX_Y), self.MAX_Y)
        else:
            if candid > self.MIN_Y:
                point = (candid_x, candid)
            else:
                point = (self.line_ytox(self.MIN_Y), self.MIN_Y)
        return point

    def line(self) -> ((float, float), (float, float)):
        first_point = self._define_point(self.MIN_X)
        second_point = self._define_point(self.MAX_X)
        return first_point, second_point

    def above_line(self, x: float, y: float) -> bool:
        return y > ((x * self.m) + self.n)
