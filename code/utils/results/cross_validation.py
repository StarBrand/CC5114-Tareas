import numpy as np
import logging
from copy import deepcopy
from sklearn.model_selection import KFold
from neural_network import NeuralNetwork
from utils.results import Trainer


class KFoldTrainer(Trainer, KFold):

    def __init__(self, k: int, seed: int, train_set: np.ndarray, labels: np.ndarray):
        super(KFoldTrainer, self).__init__(k, True, seed)
        self.data = train_set.copy()
        self.labels = labels.copy()
        self.indexes = [(train, test) for train, test in self.split(self.data.T)]
        self.i = 0
        self.k = k

    def train(self, neural_network: NeuralNetwork, epochs: int = 1, repeat: bool = False)\
            -> (NeuralNetwork, ([float], [float])):
        to_train = deepcopy(neural_network)
        if self.i >= self.k:
            logging.error("No more training iterations!!")
            return to_train, ([], [])
        logging.info("Iteration {}/{}".format(self.i + 1, self.k))
        train_set, _ = self.indexes[self.i]
        metrics = to_train.train(
            self.data.take(train_set, axis=-1),
            self.labels.take(train_set, axis=-1),
            epochs=epochs, repeat=repeat)
        self.i += 1
        return to_train, metrics

    def evaluate(self, neural_network: NeuralNetwork) -> np.ndarray:
        if self.i - 1 >= self.k:
            logging.error("No more training iterations!!")
            return np.array([])
        logging.info("Iteration {}/{}".format(self.i, self.k))
        _, test = self.indexes[self.i - 1]
        return neural_network.feed_forward(
            self.data.take(test, axis=-1)
        )

    def get_labels(self) -> np.ndarray:
        if self.i - 1 >= self.k:
            logging.error("No more training iterations!!")
            return np.array([])
        _, test = self.indexes[self.i - 1]
        return self.labels.take(test, axis=-1)
