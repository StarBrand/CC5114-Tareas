from unittest import TestCase, main
import numpy as np
import logging
from perceptron import Perceptron

ARGUMENTS = 4
EPSILON = 1e-13


class PerceptronTest(TestCase):

    def setUp(self) -> None:
        self.x = np.random.randint(0.0, 1.0, 4).tolist()
        self.perceptron = Perceptron("right perceptron", ARGUMENTS)

    def test_constructor(self):
        test = False
        try:
            Perceptron("fail perceptron", ARGUMENTS, [0, 0, 0])
        except ValueError as e:
            logging.warning(e.__str__())
            test = True
        assert test
        assert (abs(self.perceptron.out(self.x) - 1.0) < EPSILON) != (abs(self.perceptron.out(self.x) - 0.0) < EPSILON)

    def test_out(self):
        test = False
        try:
            self.perceptron.out([0, 0])
        except ValueError as e:
            logging.warning(e.__str__())
            test = True
        assert test
        assert (abs(self.perceptron.out(self.x) - 1.0) < EPSILON) != (abs(self.perceptron.out(self.x) - 0.0) < EPSILON)


if __name__ == '__main__':
    main()
