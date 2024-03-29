"""network.py: NeuralNetwork Class"""

import numpy as np
import logging
from neural_network.layers import LayerFactory, NullLayer

#  To show: 10 epochs
TO_SHOW = 10


class NeuralNetwork(object):
    """NeuralNetwork implementation, using standard learning algorithm and stochastic initialization of weight"""

    def __init__(self, input_size: int, size: [int], output_size: int, func: [str or callable], lr: float):
        if len(size) + 1 > len(func):
            raise IndexError("Number of function do not align with sizes")
        layers = []
        if len(size) == 0:
            layers.append(LayerFactory.create_layer(func[0], input_size, output_size))
        else:
            layers.append(LayerFactory.create_layer(func[0], input_size, size[0]))
        for i, s in enumerate(size[0:-1]):
            layers.append(LayerFactory.create_layer(func[i + 1], s, size[i + 1]))
        if len(size) != 0:
            layers.append(LayerFactory.create_layer(func[-1], size[-1], output_size))
        self.layers = layers
        self.learning_rate = lr
        return

    def feed_forward(self, x_input: np.ndarray) -> np.ndarray:
        """
        Gives a predicted output

        :param x_input: Input
        :return: Prediction array
        """
        output = x_input.copy()
        if np.ndim(x_input) == 1:
            output = output.reshape(-1, 1)
        for layer in self.layers:
            output = layer.feed(output)
        return output

    def back_propagation(self, y_output: np.ndarray) -> None:
        """
        Propagate error, generating delta of every layer

        :param y_output: expected output (aka labels)
        :return: None
        """
        next_layer = NullLayer()
        for layer in reversed(self.layers):
            layer.propagate(y_output, next_layer.delta, next_layer.w)
            next_layer = layer

    def update_weight(self, x_input: np.ndarray) -> None:
        """
        Update weights, if error was propagated,
        Otherwise raise an Exception

        :param x_input: Input
        :return: None
        """
        if self.layers[-1].delta is None:
            raise ValueError("No derivative calculated yet")
        layer_input = x_input.copy()
        if np.ndim(x_input) == 1:
            layer_input = layer_input.reshape(-1, 1)
        for layer in self.layers:
            layer.update_weights(layer_input, self.learning_rate)
            layer_input = layer.output

    # Modification of provided code method
    @staticmethod
    def calculate_cost(output: np.ndarray, y_output: np.ndarray, m: int) -> float:
        """
        Static method for give cost of every epoch

        :param output: Output
        :param y_output: Expected output
        :param m: Size of batch
        :return: Cost (difference of a batch of predictions and labels)
        """
        cost = np.sum((0.5 * (output - y_output) ** 2).mean(axis=-1)) / m
        return cost

    def train(self, training_set: np.ndarray, labels: np.ndarray, epochs: int = 1, repeat: bool = False)\
            -> ([float], [float]):
        """
        Train a network (propagate and update weights)

        :param training_set: A batch of inputs
        :param labels: A batch of labels (aka expected outputs)
        :param epochs: Times of training
        :param repeat: Whether the input is going to be used on each epoch. If not, split the training set in batches
        :return: Tuple of list of leaning and list of costs
        """
        if training_set.shape[-1] != labels.shape[-1]:
            raise ValueError("Tags and training set don't match")
        batch_size = 0
        if not repeat:
            try:
                x_inputs = np.split(training_set, epochs, axis=-1)
                e_labels = np.split(labels, epochs, axis=-1)
                batch_size = e_labels[0].shape[-1]
            except ValueError:
                logging.warning("Some train data maybe be not used")
                batch_size = int(labels.shape[-1] / epochs)
                new_size = batch_size * epochs
                x_inputs = np.split(training_set.take(range(new_size), axis=-1), epochs, axis=-1)
                e_labels = np.split(labels.take(range(new_size), axis=-1), epochs, axis=-1)
            logging.info("Epochs of training: {}\tSize of the batches: {}".format(epochs, batch_size))
        else:
            x_inputs = e_labels = None
            logging.info("Epochs of training: {}\tSize of the batches: {}".format(epochs, labels.shape[-1]))

        learning = []
        costs = []

        for epoch in range(epochs):
            if repeat:
                output = self.feed_forward(training_set)
                self.back_propagation(labels)
                self.update_weight(training_set)
                cost = self.calculate_cost(output, labels, labels.shape[-1])
                costs.append(cost)
                expected_classes = labels.argmax(axis=0)
            else:
                output = self.feed_forward(x_inputs[epoch])
                self.back_propagation(e_labels[epoch])
                self.update_weight(x_inputs[epoch])
                cost = self.calculate_cost(output, e_labels[epoch], batch_size)
                costs.append(cost)
                expected_classes = e_labels[epoch].argmax(axis=0)
            learning.append(np.sum(output.argmax(axis=0) == expected_classes) / output.shape[-1])
            if epochs / TO_SHOW < 1 or (epoch + 1) % int(epochs / TO_SHOW) == 0:
                logging.info("Epoch {}/{}: ".format(epoch + 1, epochs))
                logging.info("\tCost after update: {}".format(cost))

        return learning, costs
