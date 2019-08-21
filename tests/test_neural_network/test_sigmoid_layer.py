from unittest import TestCase, main
import numpy as np
from random import choice, seed
from neural_network import SigmoidLayer


class SigmoidTest(TestCase):

    def setUp(self) -> None:
        self.sigmoid = SigmoidLayer(2, 1)
        self.w = self.sigmoid.w
        self.b = self.sigmoid.b
        self.simple_test = np.array([40, 40]).reshape((2, 1))
        self.batch_test = np.random.rand(2, 10000)

    def test_out_exception(self):
        test = False
        try:
            self.sigmoid.out(np.random.rand(5, 1))
        except ValueError:
            test = True
        assert test

    def test_propagate_simple(self):
        output = np.array([1])
        self.sigmoid.feed(self.simple_test)
        self.sigmoid.propagate(output)
        self.sigmoid.update_weights(self.simple_test, 1)
        assert self.sigmoid.w.mean() >= self.w.mean()

    def test_propagate_batch_up(self):
        output = np.array([1.0]*10000)
        self.sigmoid.feed(self.batch_test)
        self.sigmoid.propagate(output)
        self.sigmoid.update_weights(self.batch_test, 1)
        assert self.sigmoid.w.mean() >= self.w.mean()

    def test_propagate_batch_down(self):
        output = np.array([0.0] * 10000)
        self.sigmoid.feed(self.batch_test)
        self.sigmoid.propagate(output)
        self.sigmoid.update_weights(self.batch_test, 1)
        assert self.sigmoid.w.mean() <= self.w.mean()

    def test_propagate_batch_random(self):
        np.random.seed(12345)
        seed(12345)
        out = []
        for i in range(10000):
            out.append(choice([0.0, 1.0]))
        output = np.array(out)
        self.sigmoid.feed(self.batch_test)
        self.sigmoid.propagate(output)
        self.sigmoid.update_weights(self.batch_test, 5)
        assert np.sum(output) < 5000
        assert self.sigmoid.w.mean() <= self.w.mean()


if __name__ == '__main__':
    main()
