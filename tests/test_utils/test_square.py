from random import uniform
from unittest import TestCase, main
from utils.patterns import Square

FACE = 60
MIN_X = MIN_Y = -50
MAX_X = MAX_Y = 50
CENTER = (uniform(-5, 5), uniform(-5, 5))
EPSILON = 1e-6


class TestSquare(TestCase):

    def setUp(self) -> None:
        self.a_square = Square(FACE, CENTER, (MIN_X, MAX_X), (MIN_Y, MAX_Y))
        self.x_min = self.a_square.x_min
        self.x_max = self.a_square.x_max
        self.y_min = self.a_square.y_min
        self.y_max = self.a_square.y_max

    def test_construct(self):
        ans1 = False
        ans2 = False
        try:
            c = Square(110, CENTER, (MIN_X, MAX_X), (MIN_Y, MAX_Y))
        except AssertionError:
            ans1 = True
        try:
            c = Square(10, (60, 0), (MIN_X, MAX_X), (MIN_Y, MAX_Y))
        except AssertionError:
            ans2 = True
        assert ans1
        assert ans2

    def test_x_to_y(self):
        x = 20
        actual = self.a_square.x_to_y(x)
        assert abs(actual[0] - self.y_min) < EPSILON
        assert abs(actual[1] - self.y_max) < EPSILON
        x = 40
        actual = self.a_square.x_to_y(x)
        assert len(actual) == 0

    def test_y_to_x(self):
        y = 20
        actual = self.a_square.y_to_x(y)
        assert abs(actual[0] - self.x_min) < EPSILON
        assert abs(actual[1] - self.x_max) < EPSILON
        y = 40
        actual = self.a_square.y_to_x(y)
        assert len(actual) == 0

    def test_is_above(self):
        x = 40
        y = uniform(MIN_Y, MAX_Y)
        assert self.a_square.is_above(x, y)
        x = 5
        y = 40
        assert self.a_square.is_above(x, y)
        x = 5
        y = 5
        assert not self.a_square.is_above(x, y)

    def test_graph(self):
        x, y = self.a_square.graph()
        assert len(x) == len(y)


if __name__ == "__main__":
    main()
