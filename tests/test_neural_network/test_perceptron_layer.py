from unittest import TestCase, main
import numpy as np
import logging
from neural_network.layers import PerceptronLayer


class PerceptronTest(TestCase):

    def setUp(self) -> None:
        self.layer = PerceptronLayer(2, 1)
        self.w = self.layer.w.copy()
        self.b = self.layer.b.copy()
        self.simple_test = np.array([40, 40]).reshape((2, 1))
        self.batch_test = np.random.rand(2, 10000)

    def test_out_exception(self):
        test = False
        try:
            self.layer.out(np.random.rand(5, 1))
        except ValueError:
            test = True
        assert test

    def test_propagate_simple(self):
        self.layer.feed(self.simple_test)
        test = False
        try:
            self.layer.propagate(np.array([1]))
        except AttributeError as e:
            logging.warning(e.__str__())
            test = True
        assert test
        self.layer.update_weights(self.simple_test, 1)
        assert (self.layer.w == self.w).all()

    def test_propagate(self):
        self.layer.feed(self.batch_test)
        test = False
        try:
            self.layer.propagate(np.array([1.0] * 10000))
        except AttributeError as e:
            logging.warning(e.__str__())
            test = True
        assert test
        self.layer.update_weights(self.batch_test, 1)
        assert (self.layer.w == self.w).all()


if __name__ == '__main__':
    main()
