from unittest import TestCase, main
import logging
import numpy as np
from learning_perceptron import Neuron
from utils.math_functions import sigmoid, tanh, step

ARGUMENT = 4
EPSILON = 1e-10


class NeuronTest(TestCase):

    def setUp(self) -> None:
        self.input = np.random.uniform(-10.0, 10.0, ARGUMENT).tolist()
        self.sigmoid = Neuron("sigmoid neuron", ARGUMENT, sigmoid, 0.5)
        self.tanh = Neuron("tanh neuron", ARGUMENT, tanh, 0.5)
        self.perceptron = Neuron("perceptron", ARGUMENT, step, 0.5)

    def test_exception(self):
        test = False
        try:
            Neuron("wrong", ARGUMENT, sigmoid, 0.5, [0, 0, 0])
        except ValueError as e:
            logging.warning(e.__str__())
            test = True
        assert test
        test = False
        try:
            self.sigmoid.feed([0, 0, 0])
        except ValueError as e:
            logging.warning(e.__str__())
            test = True
        assert test

    def test_sigmoid(self):
        expected = self.get_expected(sigmoid, self.sigmoid.get_weights())
        actual = self.sigmoid.feed(self.input)
        assert (np.abs(np.array(expected) - np.array(actual)) < EPSILON).all()

    def test_tanh(self):
        expected = self.get_expected(tanh, self.tanh.get_weights())
        actual = self.tanh.feed(self.input)
        assert (np.abs(np.array(expected) - np.array(actual)) < EPSILON).all()

    def test_step(self):
        expected = self.get_expected(step, self.perceptron.get_weights())
        actual = self.perceptron.feed(self.input)
        assert (np.abs(np.array(expected) - np.array(actual)) < EPSILON).all()

    def test_define_weights(self):
        w = [20, 10, 20, 10]
        b = 40
        expected = self.get_expected(sigmoid, (w, b))
        fixed_neuron = Neuron("fixed", ARGUMENT, sigmoid, 0.5, w, b)
        actual = fixed_neuron.feed(self.input)
        fail = self.sigmoid.feed(self.input)
        assert abs(expected - actual) < EPSILON
        assert not abs(fail - actual) < EPSILON

    def get_expected(self, function: callable, weights: ([float], float)):
        ans = weights[1]
        for i, x in enumerate(self.input):
            ans += weights[0][i] * x
        return function(ans)


if __name__ == '__main__':
    main()
