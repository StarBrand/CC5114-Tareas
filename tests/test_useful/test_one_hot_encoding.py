"""test_one_hot_encoding.py: unittest of one_hot_encoding"""
from unittest import TestCase, main
import numpy as np
from random import randint
from useful.preprocess_dataset import one_hot_encoding

NUMBER_OF_RANDOM_TEST = 5
ELEMENTS = ["Cat", "Dog", "Elephant", "Turtle", "Dragon",
            "Lizard", "Wolf", "Raven", "Tiger", "Red Panda"]
N_ELEMENTS = len(ELEMENTS)
EPSILON = 1e-6


class OneHotTest(TestCase):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        self.one_dimension = _randomize_list(
            ELEMENTS.copy() * 1000
        )
        self.one_dimension_numpy = np.array(self.one_dimension.copy())
        self.multi_dimensional_numpy = self.one_dimension_numpy.copy().reshape(4, 5, 2, -1)
        self.multi_dimensional = self.multi_dimensional_numpy.copy().tolist()

    def test_one_dimension(self):
        actual, encoding = one_hot_encoding(self.one_dimension)
        assert len(self.one_dimension) == len(actual)
        assert type(actual) == list
        for _ in range(NUMBER_OF_RANDOM_TEST):
            index = randint(0, len(actual) - 1)
            actual_element = actual[index]
            expected = encoding[self.one_dimension[index]]
            assert type(actual_element) == list
            assert len(actual_element) == N_ELEMENTS
            assert abs(sum(actual_element) - 1) < EPSILON
            assert (expected == actual_element).all()

    def test_multi_dimensional(self):
        actual_encoded, encoding = one_hot_encoding(self.multi_dimensional)
        assert len(self.multi_dimensional) == len(actual_encoded)
        assert type(actual_encoded) == list
        actual = actual_encoded
        expected = None
        for _ in range(NUMBER_OF_RANDOM_TEST):
            index = randint(0, len(actual_encoded) - 1)
            actual = actual_encoded[index]
            expected = self.multi_dimensional[index]
            assert type(actual) == list
            assert len(actual) == 5
            index = randint(0, len(actual) - 1)
            actual = actual[index]
            expected = expected[index]
            assert type(actual) == list
            assert len(actual) == 2
            index = randint(0, len(actual) - 1)
            actual = actual[index]
            expected = expected[index]
            assert type(actual) == list
            assert len(actual) == (N_ELEMENTS * 1000 / (5 * 4 * 2))
        for _ in range(NUMBER_OF_RANDOM_TEST):
            index = randint(0, len(actual) - 1)
            actual_element = actual[index]
            expected_element = encoding[expected[index]]
            assert type(actual_element) == list
            assert len(actual_element) == N_ELEMENTS
            assert abs(sum(actual_element) - 1) < EPSILON
            assert (actual_element == expected_element).all()

    def test_one_dimension_numpy(self):
        actual, encoding = one_hot_encoding(self.one_dimension_numpy)
        assert len(self.one_dimension_numpy) == len(actual)
        assert actual.shape == (len(actual), N_ELEMENTS)
        assert type(actual) == np.ndarray
        for _ in range(NUMBER_OF_RANDOM_TEST):
            index = randint(0, len(actual) - 1)
            actual_element = actual[index]
            expected = encoding[self.one_dimension_numpy[index]]
            assert type(actual_element) == np.ndarray
            assert len(actual_element) == N_ELEMENTS
            assert abs(actual_element.sum() - 1) < EPSILON
            assert (expected == actual_element).all()

    def test_multi_dimensional_numpy(self):
        actual_encoded, encoding = one_hot_encoding(self.multi_dimensional_numpy)
        assert len(self.multi_dimensional) == len(actual_encoded)
        assert type(actual_encoded) == np.ndarray
        actual = actual_encoded
        expected = None
        for _ in range(NUMBER_OF_RANDOM_TEST):
            index = randint(0, len(actual_encoded) - 1)
            actual = actual_encoded[index]
            expected = self.multi_dimensional[index]
            assert type(actual) == np.ndarray
            assert len(actual) == 5
            index = randint(0, len(actual) - 1)
            actual = actual[index]
            expected = expected[index]
            assert type(actual) == np.ndarray
            assert len(actual) == 2
            index = randint(0, len(actual) - 1)
            actual = actual[index]
            expected = expected[index]
            assert type(actual) == np.ndarray
            assert len(actual) == (N_ELEMENTS * 1000 / (5 * 4 * 2))
        for _ in range(NUMBER_OF_RANDOM_TEST):
            index = randint(0, len(actual) - 1)
            actual_element = actual[index]
            expected_element = encoding[expected[index]]
            assert type(actual_element) == np.ndarray
            assert len(actual_element) == N_ELEMENTS
            assert abs(sum(actual_element) - 1) < EPSILON
            assert (actual_element == expected_element).all()


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
