import logging
import numpy as np
from neural_network import NeuronLayer


class NullLayer(NeuronLayer):

    def __init__(self):
        super(NullLayer, self).__init__(0, 0, None)
        self.W = None
        self.b = None

    def out(self, x_input: np.array) -> np.array:
        logging.warning("This a non functional layer")
        return np.array([])

    def feed(self, x_input: np.array, save: bool = True) -> np.array:
        logging.warning("This a non functional layer")
        return np.array([])

    def transverse_derivative(self, output: np.array) -> np.array:
        logging.warning("This a non functional layer")
        return np.array([])

    def propagate(self, output: np.array,
                  next_delta: np.array or None = None,
                  next_w: np.array or None = None) -> None:
        logging.warning("This a non functional layer")

    def update_weights(self, x_input: np.array, learning_rate: float):
        logging.warning("This a non functional layer")
