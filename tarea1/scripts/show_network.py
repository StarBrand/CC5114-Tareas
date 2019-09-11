"""show_network.py: Show Neural Network performance"""
import matplotlib.pyplot as plt
import numpy as np
import logging
from random import seed
from neural_network import NeuralNetwork
from utils.math_functions import sigmoid, tanh
from utils.patterns import DoubleLine
from useful import plot_result, do_prediction_net

FIG_SIZE = (12 * 3, 12)
X_MIN = Y_MIN = -50
X_MAX = Y_MAX = 50
SLOPE = (-2.0, 2.0)
INTERCEPT1 = (-40.0, -20.0)
INTERCEPT2 = (20.0, 40.0)
INTERCEPT = (INTERCEPT1, INTERCEPT2)
N1 = int(1e4)
N2 = int(1e6)
TO_SHOW = 1500

np.random.seed(3)
seed(3)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    # Predict a line
    double_line = DoubleLine(SLOPE, INTERCEPT, (X_MIN, X_MAX), (Y_MIN, Y_MAX))

    # Initialize perceptron
    network = NeuralNetwork(2, [4], 1, [tanh, sigmoid], 0.1)

    # Random dataset
    train_set = double_line.training_set(N1)
    test_set = double_line.training_set(TO_SHOW)

    # First plot
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=FIG_SIZE)
    prediction = do_prediction_net(network, test_set)
    logging.info("First Plot")
    plot_result(test_set, np.array(prediction), double_line, ax1, 0.5)
    ax1.set_title("Before training\n", fontsize=20)

    network.train(train_set[0: -1], train_set[-1], epochs=int(1e3))

    prediction = do_prediction_net(network, test_set)
    logging.info("Second Plot")
    plot_result(test_set, np.array(prediction), double_line, ax2, 0.5)
    ax2.set_title("After 1000 epoch (batch size = 10)\n", fontsize=20)

    # Random dataset
    train_set = double_line.training_set(N2)

    network.train(train_set[0: -1], train_set[-1], epochs=int(1e5))

    prediction = do_prediction_net(network, test_set)
    logging.info("Third Plot")
    plot_result(test_set, np.array(prediction), double_line, ax3, 0.5)
    ax3.set_title("After 1e5 epoch (batch size = 10)\n", fontsize=20)

    plt.savefig("../results/example_network.png")
