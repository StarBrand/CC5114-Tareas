"""trainer.py: Trainer ABC"""
from abc import ABC, abstractmethod
import numpy as np
from neural_network import NeuralNetwork


class Trainer(ABC):
    """Trainer abstract class that defines method for trainers. Cannot be initialized"""

    @abstractmethod
    def train(self, neural_network: NeuralNetwork, epochs: int = 1, repeat: bool = False)\
            -> (NeuralNetwork, ([float], [float])):
        """
        Train Neural network

        :param neural_network: network to be trained
        :param epochs: Number of epochs of training
        :param repeat: Whether use the same dataset on each epoch
        :return: Trained neural network and tuple with learning data and cost data
        """
        pass

    @abstractmethod
    def evaluate(self, neural_network: NeuralNetwork) -> np.ndarray:
        """
        Evaluate neural network on test set

        :param neural_network: Network to be evaluated
        :return: Prediction
        """
        pass

    @abstractmethod
    def get_labels(self) -> np.ndarray:
        """
        Get labels of test set

        :return: labels of test set
        """
        pass
