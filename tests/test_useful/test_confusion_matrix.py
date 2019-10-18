"""test_confusion_matrix.py: unittest of confusion matrix and evaluation functions"""
from unittest import TestCase, main
import numpy as np
from utils.results import confusion_matrix
from utils.results import accuracy, precision
from utils.results import recall, f1_score

# One dimension
CLASS_Y = CLASS_N = 500
Y_AS_Y = int(0.7 * CLASS_Y)  # 350
Y_AS_N = int(0.3 * CLASS_Y)  # 150
N_AS_Y = int(0.2 * CLASS_N)  # 400
N_AS_N = int(0.8 * CLASS_N)  # 100

# Multi dimension
CLASS_A = CLASS_B = CLASS_C = 400
A_AS_A = int(0.7 * CLASS_A)  # 280
A_AS_B = int(0.2 * CLASS_A)  # 80
A_AS_C = int(0.1 * CLASS_A)  # 40
B_AS_A = int(0.15 * CLASS_B)  # 60
B_AS_B = int(0.8 * CLASS_B)  # 320
B_AS_C = int(0.05 * CLASS_B)  # 20
C_AS_A = int(0.25 * CLASS_C)  # 100
C_AS_B = int(0.15 * CLASS_C)  # 60
C_AS_C = int(0.6 * CLASS_C)  # 240

EPSILON = 1e-10


class ConfusionMatrixTest(TestCase):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        expected = [1.0] * CLASS_Y + [0.0] * CLASS_N
        actual = np.random.uniform(0.5, 1.0, Y_AS_Y).tolist()
        actual += np.random.uniform(0.0, 0.5, Y_AS_N).tolist()
        actual += np.random.uniform(0.5, 1.0, N_AS_Y).tolist()
        actual += np.random.uniform(0.0, 0.5, N_AS_N).tolist()
        results = np.random.permutation(np.array([expected, actual]).T)
        self.one_dimensional_result = results[(..., 1)]
        self.one_dimensional_expected = results[(..., 0)]
        expected = [[1.0, 0.0, 0.0]] * CLASS_A + [[0.0, 1.0, 0.0]] * CLASS_B + [[0.0, 0.0, 1.0]] * CLASS_C
        actual = [[0.9, 0.05, 0.05]] * A_AS_A + [[0.1, 0.8, 0.1]] * A_AS_B + [[0.15, 0.15, 0.7]] * A_AS_C
        actual += [[0.9, 0.05, 0.05]] * B_AS_A + [[0.1, 0.8, 0.1]] * B_AS_B + [[0.15, 0.15, 0.7]] * B_AS_C
        actual += [[0.9, 0.05, 0.05]] * C_AS_A + [[0.1, 0.8, 0.1]] * C_AS_B + [[0.15, 0.15, 0.7]] * C_AS_C
        results = np.random.permutation(np.array([expected, actual]).transpose((1, 2, 0)))
        self.multi_dimensional_result = results[(..., 1)].T
        self.multi_dimensional_expected = results[(..., 0)].T

    def test_exception(self):
        test = False
        wrong_output = np.random.rand(2, 1000)
        try:
            confusion_matrix(
                wrong_output, self.one_dimensional_expected
            )
        except ValueError:
            test = True
        assert test
        test = False
        try:
            confusion_matrix(
                wrong_output, self.one_dimensional_expected
            )
        except ValueError:
            test = True
        assert test

    def test_confusion_matrix(self):
        actual = confusion_matrix(self.one_dimensional_result, self.one_dimensional_expected)
        expected = np.array([[Y_AS_Y, N_AS_Y], [Y_AS_N, N_AS_N]])
        assert ((actual - expected) < EPSILON).all()
        actual = confusion_matrix(self.multi_dimensional_result, self.multi_dimensional_expected)
        expected = np.array([[A_AS_A, B_AS_A, C_AS_A], [A_AS_B, B_AS_B, C_AS_B], [A_AS_C, B_AS_C, C_AS_C]])
        assert ((actual - expected) < EPSILON).all()

    def test_accuracy(self):
        matrix = confusion_matrix(self.one_dimensional_result, self.one_dimensional_expected)
        actual = accuracy(matrix)
        expected = (Y_AS_Y + N_AS_N) / (CLASS_Y + CLASS_N)
        assert abs(actual - expected) < EPSILON
        matrix = confusion_matrix(self.multi_dimensional_result, self.multi_dimensional_expected)
        actual = accuracy(matrix)
        expected = (A_AS_A + B_AS_B + C_AS_C) / (CLASS_A + CLASS_B + CLASS_C)
        assert abs(actual - expected) < EPSILON

    def test_precision(self):
        matrix = confusion_matrix(self.one_dimensional_result, self.one_dimensional_expected)
        actual = precision(matrix)
        expected = np.array([Y_AS_Y / (Y_AS_Y + N_AS_Y), N_AS_N / (Y_AS_N + N_AS_N)])
        assert (np.abs(actual - expected) < EPSILON).all()
        matrix = confusion_matrix(self.multi_dimensional_result, self.multi_dimensional_expected)
        actual = precision(matrix)
        expected = np.array([A_AS_A / (A_AS_A + B_AS_A + C_AS_A),
                             B_AS_B / (A_AS_B + B_AS_B + C_AS_B),
                             C_AS_C / (A_AS_C + B_AS_C + C_AS_C)])
        assert (np.abs(actual - expected) < EPSILON).all()

    def test_recall(self):
        matrix = confusion_matrix(self.one_dimensional_result, self.one_dimensional_expected)
        actual = recall(matrix)
        expected = np.array([Y_AS_Y / CLASS_Y, N_AS_N / CLASS_N])
        assert (np.abs(actual - expected) < EPSILON).all()
        matrix = confusion_matrix(self.multi_dimensional_result, self.multi_dimensional_expected)
        actual = recall(matrix)
        expected = np.array([A_AS_A / CLASS_A,
                             B_AS_B / CLASS_B,
                             C_AS_C / CLASS_C])
        assert (np.abs(actual - expected) < EPSILON).all()

    def test_f1_score(self):
        matrix = confusion_matrix(self.one_dimensional_result, self.one_dimensional_expected)
        actual = f1_score(matrix)
        a = np.array([Y_AS_Y / (Y_AS_Y + N_AS_Y), N_AS_N / (Y_AS_N + N_AS_N)])
        b = np.array([Y_AS_Y / CLASS_Y, N_AS_N / CLASS_N])
        expected = 2 * (a * b) / (a + b)
        assert (np.abs(actual - expected) < EPSILON).all()
        matrix = confusion_matrix(self.multi_dimensional_result, self.multi_dimensional_expected)
        actual = f1_score(matrix)
        a = np.array([A_AS_A / (A_AS_A + B_AS_A + C_AS_A),
                      B_AS_B / (A_AS_B + B_AS_B + C_AS_B),
                      C_AS_C / (A_AS_C + B_AS_C + C_AS_C)])
        b = np.array([A_AS_A / CLASS_A,
                      B_AS_B / CLASS_B,
                      C_AS_C / CLASS_C])
        expected = 2 * (a * b) / (a + b)
        assert (np.abs(actual - expected) < EPSILON).all()


if __name__ == '__main__':
    main()
