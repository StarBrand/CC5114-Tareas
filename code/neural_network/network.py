import numpy as np
import logging
from neural_network import LayerFactory, NullLayer

#  To show: 10 epochs
TO_SHOW = 10


class NeuralNetwork(object):

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

    def feed_forward(self, x_input: np.ndarray):
        output = x_input.copy()
        if np.ndim(x_input) == 1:
            output = output.reshape(-1, 1)
        for layer in self.layers:
            output = layer.feed(output)
        return output

    def back_propagation(self, y_output: np.ndarray) -> None:
        next_layer = NullLayer()
        for layer in reversed(self.layers):
            layer.propagate(y_output, next_layer.delta, next_layer.w)
            next_layer = layer

    def update_weight(self, x_input: np.ndarray):
        if self.layers[-1].delta is None:
            raise ValueError("No derivative calculated yet")
        layer_input = x_input.copy()
        if np.ndim(x_input) == 1:
            layer_input = layer_input.reshape(-1, 1)
        for layer in self.layers:
            layer.update_weights(layer_input, self.learning_rate)
            layer_input = layer.output

    # Modification of provided code method
    def calculate_cost(self, y_output: np.ndarray, m: int):
        cost = np.sum((0.5 * (self.layers[-1].output - y_output) ** 2).mean(axis=-1)) / m
        return cost

    def train(self, training_set: np.ndarray, labels: np.ndarray, epochs: int = 1, batch_size: int = 0):
        if training_set.shape[-1] != labels.shape[-1]:
            raise ValueError("Tags and training set don't match")
        if batch_size < 0 or epochs < 0:
            raise ValueError("Invalid value, it has to be a positive integer")
        if epochs == 1 and batch_size > 0:
            epochs = int(labels.shape[-1] / batch_size)
        try:
            x_inputs = np.split(training_set, epochs, axis=-1)
            e_labels = np.split(labels, epochs, axis=-1)
            batch_size = e_labels[0].shape[-1]
        except ValueError:
            logging.warning("Some train data maybe be not used")
            batch_size = int(labels.shape[-1] / epochs)
            epochs = int(labels.shape[-1] / batch_size)
            x_inputs = np.split(training_set, epochs, axis=-1)
            e_labels = np.split(labels, epochs, axis=-1)
        logging.info("Epochs of training: {}\tSize of the batches: {}".format(epochs, batch_size))
        for epoch in range(epochs):
            self.feed_forward(x_inputs[epoch])
            self.back_propagation(e_labels[epoch])
            self.update_weight(x_inputs[epoch])
            if epochs / TO_SHOW < 1 or (epoch + 1) % int(epochs / TO_SHOW) == 0:
                logging.info("Epoch {}/{}: ".format(epoch + 1, epochs))
                logging.info("\tCost after update: {}".format(self.calculate_cost(e_labels[epoch], batch_size)))
