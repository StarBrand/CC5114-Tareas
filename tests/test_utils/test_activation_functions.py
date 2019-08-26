from unittest import TestCase, main
import numpy as np
import logging
from random import uniform
from utils.math_functions import sigmoid, tanh, step, derivative

EPSILON = 1e-10


class ActivationFunctionTest(TestCase):

    def setUp(self) -> None:
        self.big = 1e2000000
        self.small = -1e2000000
        self.number = uniform(-10, 10)
        self.array = np.array([self.big, self.small, self.number])
        self.d_big = 2.0
        self.d_small = -2.0
        self.d_number = uniform(0, 1)
        self.d_array = np.array([-1, 0, 1, self.d_number])

    @staticmethod
    def expect_exception(func: callable, x: np.ndarray or None, output: np.ndarray or None):
        test = False
        try:
            derivative[func](x=x, output=output)
        except ValueError as e:
            logging.warning(e.__str__())
            test = True
        assert test

    def test_exception_two_arguments(self):
        self.expect_exception(sigmoid, self.big, self.small)
        self.expect_exception(tanh, self.big, self.small)
        self.expect_exception(step, self.big, self.small)

    def test_exception_none_arguments(self):
        self.expect_exception(sigmoid, None, None)
        self.expect_exception(tanh, None, None)
        self.expect_exception(step, None, None)

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

    def test_step(self):
        a = step(self.big)
        b = step(self.small)
        c = step(self.number)
        d = step(self.array)
        assert abs(a - 1.0) < EPSILON
        assert abs(b - 0.0) < EPSILON
        assert 0.0 <= c <= 1.0
        assert 0.0 <= np.mean(d) <= 1.0

    def test_d_sigmoid(self):
        a = derivative[sigmoid](x=self.array)
        b = derivative[sigmoid](output=self.d_big)
        c = derivative[sigmoid](output=self.d_small)
        d = derivative[sigmoid](output=self.d_number)
        e = derivative[sigmoid](output=self.d_array)
        assert abs(a[0] - 0.0) < EPSILON
        assert abs(a[1] - 0.0) < EPSILON
        assert 0 <= a[2] <= 1.0
        assert b < 0 and c < 0
        assert d >= 0
        assert (e[1: len(e)] >= 0).all()

    def test_d_tanh(self):
        a = derivative[tanh](x=self.array)
        b = derivative[tanh](output=self.d_big)
        c = derivative[tanh](output=self.d_small)
        d = derivative[tanh](output=self.d_number)
        e = derivative[tanh](output=self.d_array)
        assert abs(a[0] - 0.0) < EPSILON
        assert abs(a[1] - 0.0) < EPSILON
        assert 0 <= a[2] <= 1.0
        assert b < 0 and c < 0
        assert d >= 0
        assert (e >= 0).all()

    def test_d_step(self):
        test1 = False
        test2 = False
        test3 = False
        try:
            derivative[step](output=self.d_big)
        except AttributeError:
            test1 = True
        try:
            derivative[step](output=self.d_small)
        except AttributeError:
            test2 = True
        try:
            derivative[step](output=self.d_number)
        except AttributeError:
            test3 = True
        assert test1 and test2 and test3
        a = derivative[step](x=self.array)
        b = derivative[step](output=self.d_array)
        assert abs(a[0] - 0.0) < EPSILON
        assert abs(a[1] - 0.0) < EPSILON
        assert 0 <= a[2] <= 1.0
        c = np.array([b[0], b[2], b[3]])
        assert (c - 0.0 < EPSILON).all()


if __name__ == '__main__':
    main()
