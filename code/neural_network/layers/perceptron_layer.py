import numpy as np
import logging
from neural_network.layers import NeuronLayer
from utils.math_functions import step


class PerceptronLayer(NeuronLayer):

    def __init__(self, input_size: int, output_size: int):
        super(PerceptronLayer, self).__init__(input_size, output_size, step)

    def propagate(self, output: np.ndarray,
                  next_delta: np.ndarray or None = None,
                  next_w: np.ndarray or None = None) -> None:
        raise AttributeError("Perceptron Layer cannot be used for learning")

    def update_weights(self, x_input: np.ndarray, learning_rate: float) -> None:
        logging.warning("Perceptron Layer cannot be used for learning, weights will not be changed")
        return
