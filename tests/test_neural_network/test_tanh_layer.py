"""test_tanh_layer.py: unittest of TanhLayer"""
from unittest import TestCase, main
import numpy as np
from neural_network.layers import TanhLayer


class TanhTest(TestCase):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        self.tanh_layer = TanhLayer(2, 1)
        self.w = self.tanh_layer.w
        self.b = self.tanh_layer.b
        self.simple_test = np.array([30, 40]).reshape((2, 1))
        self.batch_test = np.random.rand(2, 10000)

    def test_out_exception(self):
        test = False
        try:
            self.tanh_layer.out(np.random.rand(5, 1))
        except ValueError:
            test = True
        assert test

    def test_propagate_simple(self):
        output = np.array([1])
        self.tanh_layer.feed(self.simple_test)
        self.tanh_layer.propagate(output)
        self.tanh_layer.update_weights(self.simple_test, 1)
        assert self.tanh_layer.w.mean() >= self.w.mean()

    def test_propagate_batch_up(self):
        delta = np.random.uniform(-10.0, 0.0, 30000).reshape(3, 10000)
        next_w = np.random.rand(3, 1)
        self.tanh_layer.feed(self.batch_test)
        self.tanh_layer.propagate(np.array(1), delta, next_w)
        self.tanh_layer.update_weights(self.batch_test, 1)
        assert self.tanh_layer.w.mean() >= self.w.mean()

    def test_propagate_batch_down(self):
        delta = np.random.uniform(0.0, 10.0, 30000).reshape(3, 10000)
        next_w = np.random.rand(3, 1)
        self.tanh_layer.feed(self.batch_test)
        self.tanh_layer.propagate(np.array(1), delta, next_w)
        self.tanh_layer.update_weights(self.batch_test, 1)
        assert self.tanh_layer.w.mean() <= self.w.mean()


if __name__ == '__main__':
    main()
