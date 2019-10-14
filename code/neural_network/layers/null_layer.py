"""null_layer.py: NullLayer Class"""
import logging
import numpy as np
from neural_network.layers import NeuronLayer


class NullLayer(NeuronLayer):
    """NullLayer class, Null Object Patter. Needed in network to precede first layer"""

    def __init__(self):
        super().__init__(0, 0, None)
        self.w = None
        self.b = None

    def out(self, x_input: np.ndarray) -> np.ndarray:
        """
        Return an empty array

        :param x_input: To be ignored
        :return: numpy array empty
        """
        logging.warning("This a non functional layer")
        return np.array([])

    def feed(self, x_input: np.ndarray, save: bool = True) -> np.ndarray:
        """
        Return an empty array

        :param x_input: To be ignored
        :param save: To be ignored
        :return: numpy array empty
        """
        logging.warning("This a non functional layer")
        return np.array([])

    def transverse_derivative(self, x: np.ndarray or None = None, output: np.ndarray or None = None) -> np.ndarray:
        """
        Return an empty array

        :param x: To be ignored
        :param output: To be ignored
        :return: numpy array empty
        """
        logging.warning("This a non functional layer")
        return np.array([])

    def propagate(self, output: np.ndarray,
                  next_delta: np.ndarray or None = None,
                  next_w: np.ndarray or None = None) -> None:
        """
        Do nothing

        :param output: To be ignored
        :param next_delta: To be ignored
        :param next_w: To be ignored
        :return: None
        """
        logging.warning("This a non functional layer")

    def update_weights(self, x_input: np.ndarray, learning_rate: float):
        """
        Do nothing

        :param x_input: To be ignored
        :param learning_rate: To be ignored
        :return: None
        """
        logging.warning("This a non functional layer")
