import logging
import numpy as np
from neural_network import NeuronLayer


class NullLayer(NeuronLayer):

    def __init__(self):
        super(NullLayer, self).__init__(0, 0, None)
        self.w = None
        self.b = None

    def out(self, x_input: np.ndarray) -> np.ndarray:
        logging.warning("This a non functional layer")
        return np.array([])

    def feed(self, x_input: np.ndarray, save: bool = True) -> np.ndarray:
        logging.warning("This a non functional layer")
        return np.array([])

    def transverse_derivative(self, output: np.ndarray) -> np.ndarray:
        logging.warning("This a non functional layer")
        return np.array([])

    def propagate(self, output: np.ndarray,
                  next_delta: np.ndarray or None = None,
                  next_w: np.ndarray or None = None) -> None:
        logging.warning("This a non functional layer")

    def update_weights(self, x_input: np.ndarray, learning_rate: float):
        logging.warning("This a non functional layer")
