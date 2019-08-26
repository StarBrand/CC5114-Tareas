import numpy as np
import logging
from abc import ABC
from utils.math_functions import derivative, proper_name


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
        self.w = np.random.randn(output_size, input_size)
        self.b = np.zeros((output_size, 1))

    def out(self, x_input: np.ndarray) -> np.ndarray:
        if x_input.shape[0] != self.input_size:
            raise ValueError("Size of input do not match the input_size")
        return np.dot(self.w, x_input) + self.b

    def feed(self, x_input: np.ndarray, save: bool = True) -> np.ndarray:
        z = self.out(x_input)
        output = self.activation_function(z)
        if save:
            self.output = output.copy()
        return output

    def transverse_derivative(self, x: np.ndarray or None = None, output: np.ndarray or None = None) -> np.ndarray:
        return derivative[self.activation_function](x=x, output=output)

    def propagate(self, output: np.ndarray,
                  next_delta: np.ndarray or None = None,
                  next_w: np.ndarray or None = None) -> None:
        if next_delta is None or next_w is None:
            error = self.output - output
        else:
            error = np.dot(next_w.T, next_delta)
        self.delta = np.multiply(error, self.transverse_derivative(output=self.output))

    def update_weights(self, x_input: np.ndarray, learning_rate: float) -> None:
        m = x_input.shape[-1]
        self.w = self.w - learning_rate * np.dot(self.delta, x_input.T) / m
        self.b = self.b - learning_rate * np.sum(self.delta, axis=-1, keepdims=True) / m
