from unittest import TestCase, main
import numpy as np
from random import randint, choice
from neural_network.utils import one_hot_encoding

NUMBER_OF_RANDOM_TEST = 5
ELEMENTS = ["Cat", "Dog", "Elephant", "Turtle", "Dragon",
            "Lizard", "Wolf", "Raven", "Tiger", "Red Panda"]
N_ELEMENTS = len(ELEMENTS)
EPSILON = 1e-6


class OneHotTest(TestCase):

    def setUp(self) -> None:
        self.one_dimension = _randomize_list(
            ELEMENTS.copy() * 1000
        )
        self.one_dimension_numpy = np.array(self.one_dimension.copy())
        self.multi_dimensional_numpy = self.one_dimension_numpy.copy().reshape(4, 5, 2, -1)
        self.multi_dimensional = self.multi_dimensional_numpy.copy().tolist()

    def test_one_dimension(self):
        actual = one_hot_encoding(self.one_dimension)
        assert len(self.one_dimension) == len(actual)
        assert type(actual) == list
        for _ in range(NUMBER_OF_RANDOM_TEST):
            element = choice(actual)
            assert type(element) == list
            assert len(element) == N_ELEMENTS
            assert abs(sum(element) - 1) < EPSILON

    def test_multi_dimensional(self):
        actual_encoded = one_hot_encoding(self.multi_dimensional)
        assert len(self.multi_dimensional) == len(actual_encoded)
        assert type(actual_encoded) == list
        actual = actual_encoded
        for _ in range(NUMBER_OF_RANDOM_TEST):
            actual = choice(actual_encoded)
            assert type(actual) == list
            assert len(actual) == 5
            actual = choice(actual)
            assert type(actual) == list
            assert len(actual) == 2
            actual = choice(actual)
            assert type(actual) == list
            assert len(actual) == (N_ELEMENTS * 1000 / (5 * 4 * 2))
        for _ in range(NUMBER_OF_RANDOM_TEST):
            element = choice(actual)
            assert type(element) == list
            assert len(element) == N_ELEMENTS
            assert abs(sum(element) - 1) < EPSILON

    def test_one_dimension_numpy(self):
        actual = one_hot_encoding(self.one_dimension_numpy)
        assert len(self.one_dimension_numpy) == len(actual)
        assert actual.shape == (len(actual), N_ELEMENTS)
        assert type(actual) == np.ndarray
        for _ in range(NUMBER_OF_RANDOM_TEST):
            assert type(choice(actual)) == np.ndarray
            element = choice(actual)
            assert len(element) == N_ELEMENTS
            assert abs(element.sum() - 1) < EPSILON

    def test_multi_dimensional_numpy(self):
        actual_encoded = one_hot_encoding(self.multi_dimensional_numpy)
        assert len(self.multi_dimensional_numpy) == len(actual_encoded)
        assert actual_encoded.shape == self.multi_dimensional_numpy.shape + (N_ELEMENTS, )
        assert type(actual_encoded) == np.ndarray
        actual = actual_encoded
        for _ in range(NUMBER_OF_RANDOM_TEST):
            actual = choice(actual_encoded)
            assert type(actual) == np.ndarray
            assert len(actual) == 5
            actual = choice(actual)
            assert type(actual) == np.ndarray
            assert len(actual) == 2
            actual = choice(actual)
            assert type(actual) == np.ndarray
            assert len(actual) == (N_ELEMENTS * 1000 / (5 * 4 * 2))
        for _ in range(NUMBER_OF_RANDOM_TEST):
            element = choice(actual)
            assert type(element) == np.ndarray
            assert len(element) == N_ELEMENTS
            assert abs(element.sum() - 1) < EPSILON


def _randomize_list(array: list) -> list:
    input_array = array.copy()
    output_array = []
    while len(input_array) != 0:
        output_array.append(
            input_array.pop(
                randint(0, len(input_array) - 1)
            )
        )
    return output_array


if __name__ == '__main__':
    main()
