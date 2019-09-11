"""test_sigmoid_neuron.py: unittest of SigmoidNeuron"""
from unittest import TestCase, main
import logging
import numpy as np
from learning_perceptron import SigmoidNeuron
from utils.math_functions import sigmoid

ARGUMENTS = 4
EPSILON = 1e-10


class SigmoidTest(TestCase):
    
    def setUp(self) -> None:
        """
        Sets up unittest
        """
        self.sigmoid = SigmoidNeuron(4, 0.5)
        self.x_input = list(range(ARGUMENTS))
        self.w = self.sigmoid.get_weights()[0].copy()
        self.b = self.sigmoid.get_weights()[1]

    def test_exception(self):
        test = False
        try:
            self.sigmoid.feed([0, 0])
        except ValueError as e:
            logging.warning(e.__str__())
            test = True
        assert test
    
    def test_get_weights(self):
        assert len(self.sigmoid.get_weights()[0]) == ARGUMENTS
        assert type(self.sigmoid.get_weights()[1]) == float

    def test_feed(self):
        logging.warning("Input: {}".format(self.x_input))
        logging.warning("Weights: {}".format(self.w))
        logging.warning("Weights: {}".format(self.sigmoid.get_weights()))
        logging.warning("Bias: {}".format(self.b))
        expected = self.b
        for i, x in enumerate(self.x_input):
            expected += x * self.w[i]
        expected = sigmoid(np.array(expected))
        actual = self.sigmoid.feed(self.x_input)
        logging.warning("Expected: {} and Actual: {}".format(expected, actual))
        assert (np.abs(np.array(expected) - np.array(actual)) < EPSILON).all()

    def test_train_up(self):
        expected = 1.0
        train = self.sigmoid.train(self.x_input, expected)
        new_w = self.sigmoid.get_weights()[0].copy()
        new_b = self.sigmoid.get_weights()[1]
        logging.warning("Weights pre-training: {}\tpost-training: {}".format(self.w, new_w))
        logging.warning("Bias pre-training: {}\tpost-training: {}".format(self.b, new_b))
        assert sum(self.w) <= sum(new_w)
        assert self.b <= new_b
        assert train == 1
        expected = 1.0
        train = self.sigmoid.train(self.x_input, expected)
        logging.warning("Weights pre-training: {}\tpost-training: {}".format(new_w, self.sigmoid.get_weights()[0]))
        logging.warning("Bias pre-training: {}\tpost-training: {}".format(new_b, self.sigmoid.get_weights()[1]))
        assert sum(new_w) <= sum(self.sigmoid.get_weights()[0])
        assert new_b <= self.sigmoid.get_weights()[1]
        assert train == 2

    def test_train_down(self):
        expected = 0.0
        train = self.sigmoid.train(self.x_input, expected)
        new_w = self.sigmoid.get_weights()[0].copy()
        new_b = self.sigmoid.get_weights()[1]
        logging.warning("Weights pre-training: {}\tpost-training: {}".format(self.w, new_w))
        logging.warning("Bias pre-training: {}\tpost-training: {}".format(self.b, new_b))
        assert sum(self.w) >= sum(new_w)
        assert self.b >= new_b
        assert train == 1
        expected = 0.0
        train = self.sigmoid.train(self.x_input, expected)
        logging.warning("Weights pre-training: {}\tpost-training: {}".format(new_w, self.sigmoid.get_weights()[0]))
        logging.warning("Bias pre-training: {}\tpost-training: {}".format(new_b, self.sigmoid.get_weights()[1]))
        assert sum(new_w) >= sum(self.sigmoid.get_weights()[0])
        assert new_b >= self.sigmoid.get_weights()[1]
        assert train == 2


if __name__ == '__main__':
    main()
