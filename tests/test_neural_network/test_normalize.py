import numpy as np
from unittest import TestCase, main
from random import randint
from neural_network import NormalizedNetwork, NeuralNetwork

N_H = 1.0
N_L = 0.0
D_H = 50
D_L = -50
EPSILON = 1e-10
RANDOM_TESTS = 5


class NormalizeTest(TestCase):

    def setUp(self) -> None:
        self.x_input = np.random.uniform(D_L, D_H, (50, 1000))
        self.network = NormalizedNetwork(50, [], 2, ["sigmoid"], 0.1)
        self.network_no_norm = NeuralNetwork(50, [], 2, ["sigmoid"], 0.1)
        self.network_no_norm.layers = self.network.layers

    def test_normalize(self):
        norm_input = self.network._normalize(self.x_input)
        assert self.x_input.max() <= D_H
        assert self.x_input.min() >= D_L
        assert norm_input.max() <= N_H
        assert norm_input.min() >= N_L
        assert norm_input.shape == self.x_input.shape
        expected = abs(
            self.x_input[-1, -1] - self.x_input[0, 0]
        ) / abs(
            norm_input[-1, -1] - norm_input[0, 0]
        )
        for _ in range(RANDOM_TESTS):
            i1 = randint(0, 50 - 1)
            j1 = randint(0, 1000 - 1)
            i2 = randint(0, 50 - 1)
            j2 = randint(0, 1000 - 1)
            actual = abs(
                self.x_input[i1, j1] - self.x_input[i2, j2]
            ) / abs(
                norm_input[i1, j1] - norm_input[i2, j2]
            )
            assert abs(actual - expected) < EPSILON

    def test_denormalize(self):
        norm_input = self.network._normalize(self.x_input)
        origin_input = self.network._denormalize(norm_input)
        assert (np.abs(origin_input - self.x_input) < EPSILON).all()
        assert origin_input.max() <= D_H
        assert origin_input.min() >= D_L
        assert norm_input.max() <= N_H
        assert norm_input.min() >= N_L
        assert norm_input.shape == self.x_input.shape
        expected = abs(
            origin_input[-1, -1] - origin_input[0, 0]
        ) / abs(
            norm_input[-1, -1] - norm_input[0, 0]
        )
        for _ in range(RANDOM_TESTS):
            i1 = randint(0, 50 - 1)
            j1 = randint(0, 1000 - 1)
            i2 = randint(0, 50 - 1)
            j2 = randint(0, 1000 - 1)
            actual = abs(
                origin_input[i1, j1] - origin_input[i2, j2]
            ) / abs(
                norm_input[i1, j1] - norm_input[i2, j2]
            )
            assert abs(actual - expected) < EPSILON

    def test_feed_forward(self):
        expected = self.network_no_norm.feed_forward(
            self.network._normalize(self.x_input)
        )
        actual = self.network.feed_forward(self.x_input)
        assert (abs(expected - actual) < EPSILON).all()


if __name__ == '__main__':
    main()
