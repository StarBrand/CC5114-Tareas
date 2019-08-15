from math import sqrt
from random import uniform
from unittest import TestCase, main
from neural_network import Circle

RADIUS = 25
MIN_X = MIN_Y = -50
MAX_X = MAX_Y = 50
CENTER = (uniform(-5, 5), uniform(-5, 5))
EPSILON = 1e-6


class TestCircle(TestCase):

    def setUp(self) -> None:
        self.a_circle = Circle(RADIUS, CENTER, (MIN_X, MAX_X), (MIN_Y, MAX_Y))
        self.center_x = self.a_circle.k
        self.center_y = self.a_circle.h

    def test_construct(self):
        ans1 = False
        ans2 = False
        try:
            c = Circle(110, CENTER, (MIN_X, MAX_X), (MIN_Y, MAX_Y))
        except AssertionError:
            ans1 = True
        try:
            c = Circle(10, (60, 0), (MIN_X, MAX_X), (MIN_Y, MAX_Y))
        except AssertionError:
            ans2 = True
        assert ans1
        assert ans2

    def test_x_to_y(self):
        x = 20
        expected1 = self.center_y + sqrt(RADIUS ** 2 - (x - self.center_x) ** 2)
        expected2 = self.center_y - sqrt(RADIUS ** 2 - (x - self.center_x) ** 2)
        actual = self.a_circle.x_to_y(x)
        assert abs(actual[1] - expected1) < EPSILON
        assert abs(actual[0] - expected2) < EPSILON
        x = 40
        actual = self.a_circle.x_to_y(x)
        assert len(actual) == 0

    def test_y_to_x(self):
        y = 20
        expected1 = self.center_x + sqrt(RADIUS ** 2 - (y - self.center_y) ** 2)
        expected2 = self.center_x - sqrt(RADIUS ** 2 - (y - self.center_y) ** 2)
        actual = self.a_circle.y_to_x(y)
        assert abs(actual[1] - expected1) < EPSILON
        assert abs(actual[0] - expected2) < EPSILON
        y = 40
        actual = self.a_circle.y_to_x(y)
        assert len(actual) == 0

    def test_is_above(self):
        x = 40
        y = uniform(MIN_Y, MAX_Y)
        assert self.a_circle.is_above(x, y)
        x = 20
        y = 30
        assert self.a_circle.is_above(x, y)
        x = 10
        y = 5
        assert not self.a_circle.is_above(x, y)

    def test_graph(self):
        x, y = self.a_circle.graph()
        assert len(x) == len(y)


if __name__ == "__main__":
    main()
