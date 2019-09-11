"""test_learning_perceptron.py: unittest of LearningPerceptron"""
from unittest import TestCase, main
import logging
import numpy as np
from learning_perceptron import LearningPerceptron

ARGUMENTS = 4
EPSILON = 1e-10


class TestLearningPerceptron(TestCase):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        self.perceptron = LearningPerceptron("test", 4, 0.5)
        self.x_input = list(range(ARGUMENTS))
        self.w = self.perceptron.get_weights()[0].copy()
        self.b = self.perceptron.get_weights()[1]

    def test_get_weights(self):
        self.assertEqual(len(self.perceptron.get_weights()[0]), ARGUMENTS)
        self.assertIsInstance(self.perceptron.get_weights()[1], float)

    def test_feed(self):
        logging.warning("Input: {}".format(self.x_input))
        logging.warning("Weights: {}".format(self.w))
        logging.warning("Weights: {}".format(self.perceptron.get_weights()))
        logging.warning("Bias: {}".format(self.b))
        expected = self.b
        for i, x in enumerate(self.x_input):
            expected += x * self.w[i]
        expected = (expected > 0) * 1.0
        actual = self.perceptron.feed(self.x_input)
        logging.warning("Expected: {} and Actual: {}".format(expected, actual))
        assert (np.abs(np.array(expected) - np.array(actual)) < EPSILON).all()

    def test_train_up(self):
        expected = 1.0
        train = self.perceptron.train(self.x_input, expected)
        new_w = self.perceptron.get_weights()[0].copy()
        new_b = self.perceptron.get_weights()[1]
        logging.warning("Weights pre-training: {}\tpost-training: {}".format(self.w, new_w))
        logging.warning("Bias pre-training: {}\tpost-training: {}".format(self.b, new_b))
        assert sum(self.w) <= sum(new_w)
        assert self.b <= new_b
        assert train == 1
        expected = 1.0
        train = self.perceptron.train(self.x_input, expected)
        logging.warning("Weights pre-training: {}\tpost-training: {}".format(new_w, self.perceptron.get_weights()[0]))
        logging.warning("Bias pre-training: {}\tpost-training: {}".format(new_b, self.perceptron.get_weights()[1]))
        assert sum(new_w) <= sum(self.perceptron.get_weights()[0])
        assert new_b <= self.perceptron.get_weights()[1]
        assert train == 2

    def test_train_down(self):
        expected = 0.0
        train = self.perceptron.train(self.x_input, expected)
        new_w = self.perceptron.get_weights()[0].copy()
        new_b = self.perceptron.get_weights()[1]
        logging.warning("Weights pre-training: {}\tpost-training: {}".format(self.w, new_w))
        logging.warning("Bias pre-training: {}\tpost-training: {}".format(self.b, new_b))
        assert sum(self.w) >= sum(new_w)
        assert self.b >= new_b
        assert train == 1
        expected = 0.0
        train = self.perceptron.train(self.x_input, expected)
        logging.warning("Weights pre-training: {}\tpost-training: {}".format(new_w, self.perceptron.get_weights()[0]))
        logging.warning("Bias pre-training: {}\tpost-training: {}".format(new_b, self.perceptron.get_weights()[1]))
        assert sum(new_w) >= sum(self.perceptron.get_weights()[0])
        assert new_b >= self.perceptron.get_weights()[1]
        assert train == 2


if __name__ == '__main__':
    main()
