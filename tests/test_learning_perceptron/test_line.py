from unittest import TestCase, main
from learning_perceptron.utils import Line

M_positive = 2
M_negative = -2
X = [-10, 0, 10]
Y = [-10, 0, 10]
X_MIN = Y_MIN = -20
X_MAX = Y_MAX = 20


class LineTest(TestCase):

    def setUp(self) -> None:
        self.positive_line = Line((M_positive, M_positive),
                                  (-1, 1), (X_MIN, X_MAX), (Y_MIN, Y_MAX))
        self.negative_line = Line((M_negative, M_negative),
                                  (-1, 1), (X_MIN, X_MAX), (Y_MIN, Y_MAX))
        self.n_positive = self.positive_line.n
        self.n_negative = self.negative_line.n

    def test_line_xtoy(self):
        for x in X:
            expected = x*M_positive + self.n_positive
            actual = self.positive_line.line_xtoy(x)
            assert expected == actual
            expected = x * M_negative + self.n_negative
            actual = self.negative_line.line_xtoy(x)
            assert expected == actual

    def test_line_ytox(self):
        for y in Y:
            expected = (y - self.n_positive) / M_positive
            actual = self.positive_line.line_ytox(y)
            assert expected == actual
            expected = (y - self.n_negative) / M_negative
            actual = self.negative_line.line_ytox(y)
            assert expected == actual

    def test_line(self):
        expected = ((self.positive_line.line_ytox(Y_MIN), Y_MIN),
                    (self.positive_line.line_ytox(Y_MAX), Y_MAX))
        actual = self.positive_line.line()
        assert expected == actual
        expected = ((self.negative_line.line_ytox(Y_MAX), Y_MAX),
                    (self.negative_line.line_ytox(Y_MIN), Y_MIN))
        actual = self.negative_line.line()
        assert expected == actual

    def test_above_line(self):
        expected_positive = [[True, True, True], [False, True, True], [False, False, False]]
        expected_negative = [[False, False, False], [False, True, True], [True, True, True]]
        if self.positive_line.n > 0:
            expected_positive[1][1] = False
        if self.negative_line.n > 0:
            expected_negative[1][1] = False
        for i, x in enumerate(X):
            for j, y in enumerate(Y):
                actual_positive = self.positive_line.above_line(x, y)
                actual_negative = self.negative_line.above_line(x, y)
                assert expected_positive[i][j] == actual_positive
                assert expected_negative[i][j] == actual_negative


if __name__ == "__main__":
    main()
