from unittest import TestCase, main
from utils.patterns import Line

MIN_X = MIN_Y = -50
MAX_X = MAX_Y = 50
M = (-2, 2)
N = (-10, 10)
EPSILON = 1e-6


class TestLine(TestCase):

    def setUp(self) -> None:
        self.a_line = Line(M, N, (MIN_X, MAX_X), (MIN_Y, MAX_Y))
        self.m = self.a_line.m
        self.n = self.a_line.n

    def test_x_to_y(self):
        x = 20
        expected = self.m * x + self.n
        actual = self.a_line.x_to_y(x)
        assert abs(actual[0] - expected) < EPSILON

    def test_y_to_x(self):
        y = 20
        expected = (y - self.n) / self.m
        actual = self.a_line.y_to_x(y)
        assert abs(actual[0] - expected) < EPSILON

    def test_is_above(self):
        x = 0
        y = 40
        assert self.a_line.is_above(x, y)
        x = 1
        y = self.a_line.x_to_y(x)[0]
        y1 = y + 0.5
        y2 = y - 0.5
        assert self.a_line.is_above(x, y1)
        assert not self.a_line.is_above(x, y2)

    def test_graph(self):
        x, y = self.a_line.graph()
        assert len(x) == len(y)


if __name__ == "__main__":
    main()
