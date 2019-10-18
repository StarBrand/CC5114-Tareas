"""standard_trainer.py: StandardTrainer class"""
import numpy as np
from copy import deepcopy
from neural_network import NeuralNetwork
from useful.preprocess_dataset import split_set
from useful.results import Trainer


class StandardTrainer(Trainer):
    """StandardTrainer class, that train and evaluate splitting
    dataset in train and test set"""

    def __init__(self, train_set: np.ndarray, labels: np.ndarray, percentage: float):
        labels_shape = labels.shape
        data = np.concatenate((train_set, labels), axis=0)
        train_set, test_set = split_set(data, percentage)
        self.train_set = train_set[0:-labels_shape[0]]
        self.train_labels = train_set[-labels_shape[0]:data.shape[0]]
        self.test_set = test_set[0:-labels_shape[0]]
        self.test_labels = test_set[-labels_shape[0]:data.shape[0]]

    def train(self, neural_network: NeuralNetwork, epochs: int = 1, repeat: bool = False)\
            -> (NeuralNetwork, ([float], [float])):
        """
        Train Neural network

        :param neural_network: network to be trained
        :param epochs: Number of epochs of training
        :param repeat: Whether use the same dataset on each epoch
        :return: Trained neural network and tuple with learning data and cost data
        """
        to_train = deepcopy(neural_network)
        metrics = to_train.train(self.train_set, self.train_labels, epochs=epochs, repeat=repeat)
        return to_train, metrics

    def evaluate(self, neural_network: NeuralNetwork) -> np.ndarray:
        """
        Evaluate neural network on test set

        :param neural_network: Network to be evaluated
        :return: Prediction
        """
        return neural_network.feed_forward(self.test_set)

    def get_labels(self) -> np.ndarray:
        """
        Get labels of test set

        :return: labels of test set
        """
        return self.test_labels
