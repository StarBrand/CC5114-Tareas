import numpy as np
from neural_network import NeuralNetwork

N_L = 0.0
N_H = 1.0


class NormalizedNetwork(NeuralNetwork):

    def __init__(self, input_size: int, size: [int], output_size: int, func: [str or callable], lr: float):
        super(NormalizedNetwork, self).__init__(input_size, size, output_size, func, lr)
        self.d_h = 0.0
        self.d_l = 0.0

    def feed_forward(self, x_input: np.ndarray) -> np.ndarray:
        return super(NormalizedNetwork, self).feed_forward(
            self._normalize(x_input)
        )

    def _normalize(self, x_input: np.ndarray) -> np.ndarray:
        self.d_l = x_input.min()
        self.d_h = x_input.max()
        a = N_H - N_L
        b = self.d_h - self.d_l
        return (a / b) * (x_input - self.d_l) + N_L

    def _denormalize(self, x_input: np.ndarray) -> np.ndarray:
        a = self.d_l - self.d_h
        b = - (N_H * self.d_l) + self.d_h * N_L
        c = N_L - N_H
        return (a / c) * x_input + (b / c)
