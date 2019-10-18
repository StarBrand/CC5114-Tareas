"""layer.py: Layer ABC"""
import numpy as np
import logging
from abc import ABC
from useful.math_functions import derivative, proper_name


class NeuronLayer(ABC):
    """Neuron Layer abstract class (works as Type of Layer)"""

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
        """
        Calculates the output of layer (size of input and output given on constructor) (linear part)

        :param x_input: Input (Must be of size "input_size")
        :return: Output (Will be of size "output_size")
        """
        if x_input.shape[0] != self.input_size:
            raise ValueError("Size of input do not match the input_size")
        return np.dot(self.w, x_input) + self.b

    def feed(self, x_input: np.ndarray, save: bool = True) -> np.ndarray:
        """
        Calculates the output of layer (size of input and output given on constructor) (linear part and
        non linear part 'aka activation function')

        :param x_input: Input
        :param save: Whether the input is saved on layer
        :return: Output (could be the input of another layer or an array of probabilities)
        """
        z = self.out(x_input)
        output = self.activation_function(z)
        if save:
            self.output = output.copy()
        return output

    def transverse_derivative(self, x: np.ndarray or None = None, output: np.ndarray or None = None) -> np.ndarray:
        """
        Calculate the derivative of the activation function. It has two possible inputs, if both or none of them
        is given an Exception will be raised.

        :param x: Calculated transverse derivative with x, meaning f'(x) = h(x)
        :param output: Calculated transverse derivative with f(x), meaning f'(x) = h(f(x))
        :return: Transverse derivative
        """
        return derivative[self.activation_function](x=x, output=output)

    def propagate(self, output: np.ndarray,
                  next_delta: np.ndarray or None = None,
                  next_w: np.ndarray or None = None) -> None:
        """
        Calculate the propagated error given an output
        If this is the output layer calculated delta (d(error)/d(w, b)) in function of the error
        Otherwise (an internal layer) calculated in function of delta of next layer

        :param output: Output of network, if this is an internal layer this is ignored
        :param next_delta: Delta of next lawyer or None if this is the last one
        :param next_w: Weight of  next lawyer or None if this is the last one
        """
        if next_delta is None or next_w is None:
            error = self.output - output
        else:
            error = np.dot(next_w.T, next_delta)
        self.delta = np.multiply(error, self.transverse_derivative(output=self.output))

    def update_weights(self, x_input: np.ndarray, learning_rate: float) -> None:
        """
        Update weights of layer

        :param x_input: Input
        :param learning_rate: Learning rate in which weights are updated
        """
        m = x_input.shape[-1]
        self.w = self.w - learning_rate * np.dot(self.delta, x_input.T) / m
        self.b = self.b - learning_rate * np.sum(self.delta, axis=-1, keepdims=True) / m
