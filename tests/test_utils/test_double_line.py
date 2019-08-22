from unittest import TestCase, main
from neural_network.utils import DoubleLine

MIN_X = MIN_Y = -50
MAX_X = MAX_Y = 50
M = (-2, 2)
N = (-10, 10)
EPSILON = 1e-6


class TestDoubleLine(TestCase):

    def setUp(self) -> None:
        self.a_line = DoubleLine(M, N, (MIN_X, MAX_X), (MIN_Y, MAX_Y))
        self.m = self.a_line.m
        self.n1 = self.a_line.line1.n
        self.n2 = self.a_line.line2.n

    def test_x_to_y(self):
        x = 20
        expected1 = self.m * x + self.n1
        expected2 = self.m * x + self.n2
        actual = self.a_line.x_to_y(x)
        assert abs(actual[0] - expected1) < EPSILON
        assert abs(actual[1] - expected2) < EPSILON

    def test_y_to_x(self):
        y = 20
        expected1 = (y - self.n1) / self.m
        expected2 = (y - self.n2) / self.m
        actual = self.a_line.y_to_x(y)
        assert abs(actual[0] - expected1) < EPSILON
        assert abs(actual[1] - expected2) < EPSILON

    def test_is_above(self):
        x = 1
        y = self.a_line.x_to_y(x)[0]
        y1 = y - 0.5
        y2 = y + 0.5
        y3 = y + 20.5
        assert self.a_line.is_above(x, y1)
        assert not self.a_line.is_above(x, y2)
        assert self.a_line.is_above(x, y3)

    def test_graph(self):
        x, y = self.a_line.graph()
        assert len(x) == len(y)


if __name__ == "__main__":
    main()
