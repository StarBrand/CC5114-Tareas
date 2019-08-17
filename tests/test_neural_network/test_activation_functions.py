from unittest import TestCase, main
import numpy as np
from random import uniform
from neural_network.utils import sigmoid, tanh, derivative

EPSILON = 1e-6


class ActivationFunctionTest(TestCase):

    def setUp(self) -> None:
        self.big = 1e2000000
        self.small = -1e2000000
        self.number = uniform(-10, 10)
        self.array = np.array([self.big, self.small, self.number])
        self.d_big = 1.0
        self.d_small1 = 0.0
        self.d_small2 = -1.0
        self.d_number = uniform(0, 1)
        self.d_array = np.array([self.d_big, self.d_number])

    def test_sigmoid(self):
        a = sigmoid(self.big)
        b = sigmoid(self.small)
        c = sigmoid(self.number)
        d = sigmoid(self.array)
        assert abs(a - 1.0) < EPSILON
        assert abs(b - 0.0) < EPSILON
        assert 0.0 <= c <= 1.0
        assert 0.0 <= np.mean(d) <= 1.0

    def test_tanh(self):
        a = tanh(self.big)
        b = tanh(self.small)
        c = tanh(self.number)
        d = tanh(self.array)
        assert abs(a - 1.0) < EPSILON
        assert abs(b - -1.0) < EPSILON
        assert -1.0 <= c <= 1.0
        assert -1.0 <= np.mean(d) <= 1.0

    def test_d_sigmoid(self):
        a = derivative[sigmoid](self.d_big)
        b = derivative[sigmoid](self.d_small1)
        c = derivative[sigmoid](self.d_number)
        d = derivative[sigmoid](self.d_array)
        assert abs(a - 0.0) < EPSILON
        assert abs(b - 0.0) < EPSILON
        assert 0.0 <= c <= 1.0
        assert 0.0 <= np.mean(d) <= 1.0

    def test_d_tanh(self):
        a = derivative[tanh](self.d_big)
        b = derivative[tanh](self.d_small2)
        c = derivative[tanh](self.d_number)
        d = derivative[tanh](self.d_array)
        assert abs(a - 0.0) < EPSILON
        assert abs(b - 0.0) < EPSILON
        assert 0.0 <= c <= 1.0
        assert 0.0 <= np.mean(d) <= 1.0


if __name__ == '__main__':
    main()