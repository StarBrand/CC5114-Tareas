"""test_layer_factory.py: unittest of LayerFactory"""
from unittest import TestCase, main
import numpy as np
from neural_network.layers import LayerFactory
from utils.math_functions import sigmoid, tanh, step, derivative

EPSILON = 1e-10


class TestFactory(TestCase):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        self.test_number = np.random.uniform(-1e3, 1e3, (2, 50))

    def test_create_sigmoid_from_str(self):
        actual = LayerFactory.create_layer("sigmoid", 2, 1)
        assert actual.name == "sigmoid layer"
        expected = sigmoid(self.test_number)
        assert abs(
            actual.feed(self.test_number, save=False) -
            expected).all() < EPSILON
        expected = derivative[sigmoid](self.test_number)
        assert abs(
            actual.transverse_derivative(self.test_number) -
            expected).all() < EPSILON

    def test_create_sigmoid_from_func(self):
        actual = LayerFactory.create_layer(sigmoid, 2, 1)
        assert actual.name == "sigmoid layer"
        expected = sigmoid(self.test_number)
        assert abs(
            actual.feed(self.test_number, save=False) -
            expected).all() < EPSILON
        expected = derivative[sigmoid](self.test_number)
        assert abs(
            actual.transverse_derivative(self.test_number) -
            expected).all() < EPSILON

    def test_create_step_from_str_1(self):
        actual = LayerFactory.create_layer("step", 2, 1)
        assert actual.name == "perceptron layer"
        expected = step(self.test_number)
        assert abs(
            actual.feed(self.test_number, save=False) -
            expected).all() < EPSILON
        expected = derivative[step](self.test_number)
        assert abs(
            actual.transverse_derivative(self.test_number) -
            expected).all() < EPSILON

    def test_create_step_from_str_2(self):
        actual = LayerFactory.create_layer("perceptron", 2, 1)
        assert actual.name == "perceptron layer"
        expected = step(self.test_number)
        assert abs(
            actual.feed(self.test_number, save=False) -
            expected).all() < EPSILON
        expected = derivative[step](self.test_number)
        assert abs(
            actual.transverse_derivative(self.test_number) -
            expected).all() < EPSILON

    def test_create_step_from_func(self):
        actual = LayerFactory.create_layer(step, 2, 1)
        assert actual.name == "perceptron layer"
        expected = step(self.test_number)
        assert abs(
            actual.feed(self.test_number, save=False) -
            expected).all() < EPSILON
        expected = derivative[step](self.test_number)
        assert abs(
            actual.transverse_derivative(self.test_number) -
            expected).all() < EPSILON

    def test_create_tanh_from_str(self):
        actual = LayerFactory.create_layer("tanh", 2, 1)
        assert actual.name == "tanh layer"
        expected = tanh(self.test_number)
        assert abs(
            actual.feed(self.test_number, save=False) -
            expected).all() < EPSILON
        expected = derivative[tanh](self.test_number)
        assert abs(
            actual.transverse_derivative(self.test_number) -
            expected).all() < EPSILON

    def test_create_tanh_from_func(self):
        actual = LayerFactory.create_layer(tanh, 2, 1)
        assert actual.name == "tanh layer"
        expected = tanh(self.test_number)
        assert abs(
            actual.feed(self.test_number, save=False) -
            expected).all() < EPSILON
        expected = derivative[tanh](self.test_number)
        assert abs(
            actual.transverse_derivative(self.test_number) -
            expected).all() < EPSILON

    def test_not_registered_func(self):
        test = False
        try:
            LayerFactory.create_layer("anything", 2, 1)
        except KeyError:
            test = True
        assert test
        actual = LayerFactory.create_layer(self.some_function, 2, 1)
        assert actual.feed(self.test_number).shape[-1] == self.test_number.shape[-1]
        test = False
        try:
            actual.transverse_derivative(self.test_number)
        except KeyError:
            test = True
        assert test

    @staticmethod
    def some_function(an_input: np.ndarray) -> np.ndarray:
        """
        An activation function for Exception test purpose

        :param an_input: An input
        :return: Random array of input shape (first two dimensions)
        """
        return np.random.rand(an_input.shape[0], an_input.shape[1])


if __name__ == '__main__':
    main()
