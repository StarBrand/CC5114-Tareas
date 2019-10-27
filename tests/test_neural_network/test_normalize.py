"""test_normalize.py: unittest of NormalizedNetwork"""

import numpy as np
from unittest import TestCase, main
from random import randint, seed
from neural_network import NormalizedNetwork, NeuralNetwork

N_H = 1.0
N_L = 0.0
D_H = 50
D_L = -50
EPSILON = 1e-10
RANDOM_TESTS = 5


class NormalizeTest(TestCase):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        seed(5)
        self.x_input = np.random.uniform(D_L, D_H, (50, 1000))
        self.network = NormalizedNetwork(50, [], 2, ["sigmoid"], 0.1)
        self.network_no_norm = NeuralNetwork(50, [], 2, ["sigmoid"], 0.1)
        self.network_no_norm.layers = self.network.layers.copy()

    def test_normalize(self):
        norm_input = self.network._normalize(self.x_input)
        assert (self.x_input.max(axis=-1) <= D_H).all()
        assert (self.x_input.min(axis=-1) >= D_L).all()
        assert (norm_input.max(axis=-1) <= N_H).all()
        assert (norm_input.min(axis=-1) >= N_L).all()
        assert norm_input.shape == self.x_input.shape
        expected = np.abs(self.x_input[..., -1] - self.x_input[..., 0]
                          ) / np.abs(norm_input[..., -1] - norm_input[..., 0])
        for _ in range(RANDOM_TESTS):
            i = randint(0, 50 - 1)
            j = randint(0, 50 - 1)
            actual = np.abs(self.x_input[..., i] - self.x_input[..., j]
                            ) / np.abs(norm_input[..., i] - norm_input[..., j])
            assert (np.abs(actual - expected) < EPSILON).all()

    def test_denormalize(self):
        norm_input = self.network._normalize(self.x_input)
        origin_input = self.network._denormalize(norm_input)
        assert (np.abs(origin_input - self.x_input) < EPSILON).all()
        assert (origin_input.max(axis=-1) <= D_H).all()
        assert (origin_input.min(axis=-1) >= D_L).all()
        assert (norm_input.max(axis=-1) <= N_H).all()
        assert (norm_input.min(axis=-1) >= N_L).all()
        assert norm_input.shape == self.x_input.shape
        expected = np.abs(origin_input[..., -1] - origin_input[..., 0]
                          ) / np.abs(norm_input[..., -1] - norm_input[..., 0])
        for _ in range(RANDOM_TESTS):
            i = randint(0, 50 - 1)
            j = randint(0, 50 - 1)
            actual = np.abs(origin_input[..., i] - origin_input[..., j]
                            ) / np.abs(norm_input[..., i] - norm_input[..., j])
            assert (np.abs(actual - expected) < EPSILON).all()

    def test_feed_forward(self):
        expected = self.network_no_norm.feed_forward(
            self.network._normalize(self.x_input)
        )
        actual = self.network.feed_forward(self.x_input)
        assert (abs(expected - actual) < EPSILON).all()


if __name__ == '__main__':
    main()
