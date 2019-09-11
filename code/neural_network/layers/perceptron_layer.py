"""perceptron_layer.py: Layer with step activation function"""
import numpy as np
import logging
from neural_network.layers import NeuronLayer
from utils.math_functions import step


class PerceptronLayer(NeuronLayer):
    """PerceptronLayer defined by completeness, because step activation functions
    is not designed for learning"""

    def __init__(self, input_size: int, output_size: int):
        super(PerceptronLayer, self).__init__(input_size, output_size, step)

    def propagate(self, output: np.ndarray,
                  next_delta: np.ndarray or None = None,
                  next_w: np.ndarray or None = None) -> None:
        """
        Raise an error due to this layer is not designed to learn

        :param output: To be ignored
        :param next_delta: To be ignored
        :param next_w: To be ignored
        :return: None
        """
        raise AttributeError("Perceptron Layer cannot be used for learning")

    def update_weights(self, x_input: np.ndarray, learning_rate: float) -> None:
        """
        Do nothing, and report why

        :param x_input: To be ignored
        :param learning_rate: To be ignored
        :return: None
        """
        logging.warning("Perceptron Layer cannot be used for learning, weights will not be changed")
        return
