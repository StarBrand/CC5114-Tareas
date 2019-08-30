from abc import ABC, abstractmethod
import numpy as np
from neural_network import NeuralNetwork


class Trainer(ABC):

    @abstractmethod
    def train(self, neural_network: NeuralNetwork, epochs: int = 1, repeat: bool = False)\
            -> (NeuralNetwork, ([float], [float])):
        pass

    @abstractmethod
    def evaluate(self, neural_network: NeuralNetwork) -> np.ndarray:
        pass

    @abstractmethod
    def get_labels(self) -> np.ndarray:
        pass
