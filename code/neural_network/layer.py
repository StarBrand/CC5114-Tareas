import numpy as np
import logging
from abc import ABC
from neural_network.utils import derivative, proper_name


class NeuronLayer(ABC):

    def __init__(self, input_size: int, output_size: int, func: callable):
        try:
            self.name = proper_name[func]
        except KeyError:
            logging.warning("No name registered for that function")
            self.name = "no name"
        self.output = None
        self.delta = None
        self.input_size = input_size
        self.output_size = output_size
        self.activation_function = func
        self.W = np.random.randn(output_size, input_size)
        self.b = np.zeros((output_size, 1))

    def out(self, x_input: np.array) -> np.array:
        if x_input.shape[0] != self.input_size:
            raise ValueError("Size of input do not match the input_size")
        return np.dot(self.W, x_input) + self.b

    def feed(self, x_input: np.array, save: bool = True) -> np.array:
        z = self.out(x_input)
        output = self.activation_function(z)
        if save:
            self.output = output
        return output

    def transverse_derivative(self, output: np.array) -> np.array:
        return derivative[self.activation_function](output)

    def propagate(self, output: np.array,
                  next_delta: np.array or None = None,
                  next_w: np.array or None = None) -> None:
        if next_delta is None or next_w is None:
            error = self.output - output
        else:
            error = np.dot(next_w.T, next_delta)
        self.delta = np.multiply(error, self.transverse_derivative(self.output))

    def update_weights(self, x_input: np.array, learning_rate: float):
        m = x_input.shape[-1]
        self.W = self.W - learning_rate * np.dot(self.delta, x_input.T) / m
        self.b = self.b - learning_rate * np.sum(self.delta, axis=-1, keepdims=True) / m
