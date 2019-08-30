from unittest import TestCase, main
import numpy as np
import logging
from neural_network import NeuralNetwork
from utils.math_functions import tanh, sigmoid, derivative

SIZE = 10000
EPOCHS = 100


class NetworkTest(TestCase):

    def setUp(self) -> None:
        self.network = NeuralNetwork(2, [5, 4], 1, [tanh, tanh, sigmoid], 0.1)
        self.x_input = np.array([40, 40])
        self.output = np.array([1.0])
        self.batch_input = np.random.uniform(-50, 50, (2, SIZE))
        self.batch_output = np.random.choice([0.0, 1.0], (1, SIZE))

    def test_constructor_exception(self):
        test = False
        try:
            NeuralNetwork(2, [1, 1], 1, [sigmoid], 0.1)
        except IndexError:
            test = True
        assert test
        net = None
        try:
            net = NeuralNetwork(2, [1, 1], 1, [sigmoid, tanh, tanh, sigmoid], 0.1)
        except IndexError:
            test = False
        assert test
        actual = net.feed_forward(self.x_input)
        assert actual.shape == (1, 1)

    def test_layers(self):
        assert len(self.network.layers) == 3
        a_network = NeuralNetwork(2, [], 1, [sigmoid], 0)
        assert len(a_network.layers) == 1
        assert a_network.layers[0].w.shape == (1, 2)
        assert a_network.layers[0].activation_function == sigmoid

    def test_feed_forward(self):
        #  As network:
        actual = self.network.feed_forward(self.x_input)
        #  As layers
        expected = self.network.layers[0].feed(self.x_input.reshape(-1, 1), save=False)
        assert np.equal(expected, self.network.layers[0].output).all()
        expected = self.network.layers[1].feed(expected, save=False)
        assert np.equal(expected, self.network.layers[1].output).all()
        expected = self.network.layers[2].feed(expected, save=False)
        assert np.equal(expected, self.network.layers[2].output).all()
        assert np.equal(expected, actual).all()

    def test_back_propagation(self):
        #  As layers
        hidden_output1 = self.network.layers[-3].feed(self.x_input.reshape(-1, 1), save=False)
        hidden_output2 = self.network.layers[-2].feed(hidden_output1, save=False)
        actual_output = self.network.layers[-1].feed(hidden_output2, save=False)
        error = actual_output - self.output
        expected1 = np.multiply(error, derivative[sigmoid](output=actual_output))
        error = np.dot(self.network.layers[-1].w.T, expected1)
        expected2 = np.multiply(error, derivative[tanh](output=hidden_output2))
        error = np.dot(self.network.layers[-2].w.T, expected2)
        expected3 = np.multiply(error, derivative[tanh](output=hidden_output1))
        #  As network
        self.network.feed_forward(self.x_input)
        self.network.back_propagation(self.output)
        assert np.equal(expected1, self.network.layers[-1].delta).all()
        assert np.equal(expected2, self.network.layers[-2].delta).all()
        assert np.equal(expected3, self.network.layers[-3].delta).all()

    def test_update_weight(self):
        self.network.feed_forward(self.x_input)
        self.network.back_propagation(self.output)
        #  Old weights
        w1 = self.network.layers[0].w
        b1 = self.network.layers[0].b
        w2 = self.network.layers[1].w
        b2 = self.network.layers[1].b
        w3 = self.network.layers[2].w
        b3 = self.network.layers[2].b
        self.network.layers[0].update_weights(self.x_input.reshape(-1, 1), 0.1)
        self.network.layers[1].update_weights(
            self.network.layers[0].output,
            0.1
        )
        self.network.layers[2].update_weights(
            self.network.layers[1].output,
            0.1
        )
        expected_list = [self.network.layers[0].w,
                         self.network.layers[0].b,
                         self.network.layers[1].w,
                         self.network.layers[1].b,
                         self.network.layers[2].w,
                         self.network.layers[2].b]
        #  Return to old weights
        self.network.layers[0].w = w1
        self.network.layers[0].b = b1
        self.network.layers[1].w = w2
        self.network.layers[1].b = b2
        self.network.layers[2].w = w3
        self.network.layers[2].b = b3
        self.network.update_weight(self.x_input)
        actual = [self.network.layers[0].w,
                  self.network.layers[0].b,
                  self.network.layers[1].w,
                  self.network.layers[1].b,
                  self.network.layers[2].w,
                  self.network.layers[2].b]
        for index, expected in enumerate(expected_list):
            assert np.equal(actual[index], expected).all()
    
    def test_feed_forward_batch(self):
        #  As network:
        actual = self.network.feed_forward(self.batch_input)
        #  As layers
        expected = self.network.layers[0].feed(self.batch_input, save=False)
        assert np.equal(expected, self.network.layers[0].output).all()
        expected = self.network.layers[1].feed(expected, save=False)
        assert np.equal(expected, self.network.layers[1].output).all()
        expected = self.network.layers[2].feed(expected, save=False)
        assert np.equal(expected, self.network.layers[2].output).all()
        assert np.equal(expected, actual).all()

    def test_back_propagation_batch(self):
        #  As layers
        hidden_output1 = self.network.layers[-3].feed(self.batch_input, save=False)
        hidden_output2 = self.network.layers[-2].feed(hidden_output1, save=False)
        actual_output = self.network.layers[-1].feed(hidden_output2, save=False)
        error = actual_output - self.batch_output
        expected1 = np.multiply(error, derivative[sigmoid](output=actual_output))
        error = np.dot(self.network.layers[-1].w.T, expected1)
        expected2 = np.multiply(error, derivative[tanh](output=hidden_output2))
        error = np.dot(self.network.layers[-2].w.T, expected2)
        expected3 = np.multiply(error, derivative[tanh](output=hidden_output1))
        #  As network
        self.network.feed_forward(self.batch_input)
        self.network.back_propagation(self.batch_output)
        assert np.equal(expected1, self.network.layers[-1].delta).all()
        assert np.equal(expected2, self.network.layers[-2].delta).all()
        assert np.equal(expected3, self.network.layers[-3].delta).all()

    def test_update_weight_batch(self):
        self.network.feed_forward(self.batch_input)
        self.network.back_propagation(self.batch_output)
        #  Old weights
        w1 = self.network.layers[0].w
        b1 = self.network.layers[0].b
        w2 = self.network.layers[1].w
        b2 = self.network.layers[1].b
        w3 = self.network.layers[2].w
        b3 = self.network.layers[2].b
        self.network.layers[0].update_weights(self.batch_input, 0.1)
        self.network.layers[1].update_weights(
            self.network.layers[0].output,
            0.1
        )
        self.network.layers[2].update_weights(
            self.network.layers[1].output,
            0.1
        )
        expected_list = [self.network.layers[0].w,
                         self.network.layers[0].b,
                         self.network.layers[1].w,
                         self.network.layers[1].b,
                         self.network.layers[2].w,
                         self.network.layers[2].b]
        #  Return to old weights
        self.network.layers[0].w = w1
        self.network.layers[0].b = b1
        self.network.layers[1].w = w2
        self.network.layers[1].b = b2
        self.network.layers[2].w = w3
        self.network.layers[2].b = b3
        self.network.update_weight(self.batch_input)
        actual = [self.network.layers[0].w,
                  self.network.layers[0].b,
                  self.network.layers[1].w,
                  self.network.layers[1].b,
                  self.network.layers[2].w,
                  self.network.layers[2].b]
        for index, expected in enumerate(expected_list):
            assert np.equal(actual[index], expected).all()

    def test_exception_train(self):
        test = False
        try:
            self.network.train(self.batch_input, self.output)
        except ValueError as e:
            logging.info(e.__str__())
            test = True
        assert test
        test = False
        try:
            self.network.update_weight(self.batch_input)
        except ValueError as e:
            logging.info(e.__str__())
            test = True
        assert test

    def test_train_repeat(self):
        learning, costs = self.network.train(self.batch_input, self.batch_output, epochs=EPOCHS, repeat=True)
        assert len(learning) == len(costs)
        assert len(learning) == EPOCHS

    def test_train_split(self):
        learning, costs = self.network.train(self.batch_input, self.batch_output, epochs=EPOCHS)
        assert len(learning) == len(costs)
        assert len(learning) == EPOCHS
        learning, costs = self.network.train(self.batch_input, self.batch_output, epochs=70)
        assert len(learning) == len(costs)
        assert len(learning) == 70


if __name__ == '__main__':
    main()
