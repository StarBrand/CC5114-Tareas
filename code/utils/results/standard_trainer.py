import numpy as np
from copy import deepcopy
from neural_network import NeuralNetwork
from utils.preprocess_dataset import split_set
from utils.results import Trainer


class StandardTrainer(Trainer):

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
        to_train = deepcopy(neural_network)
        metrics = to_train.train(self.train_set, self.train_labels, epochs=epochs, repeat=repeat)
        return to_train, metrics

    def evaluate(self, neural_network: NeuralNetwork) -> np.ndarray:
        return neural_network.feed_forward(self.test_set)

    def get_labels(self) -> np.ndarray:
        return self.test_labels
