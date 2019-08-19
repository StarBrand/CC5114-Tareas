from unittest import TestCase, main
import numpy as np
from neural_network import LayerFactory
from neural_network.utils import sigmoid, tanh, derivative

EPSILON = 1e-6


class TestFactory(TestCase):

    def setUp(self) -> None:
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
        return np.random.rand(an_input.shape[0], an_input.shape[1])


if __name__ == '__main__':
    main()
