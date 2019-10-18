"""show_neuron.py: Show Neuron performance"""
import matplotlib.pyplot as plt
import numpy as np
import logging
from random import seed
from learning_perceptron import Neuron
from useful.math_functions import tanh
from useful.patterns import Line, DoubleLine
from useful1 import plot_result, do_prediction

FIG_SIZE = (12 * 3, 12 * 2)
X_MIN = Y_MIN = -50
X_MAX = Y_MAX = 50
SLOPE = (-2.0, 2.0)
INTERCEPT = (-10.0, 10.0)
INTERCEPT1 = (-40.0, -20.0)
INTERCEPT2 = (20.0, 40.0)
TWO_INTERCEPT = (INTERCEPT1, INTERCEPT2)
N = 100
TO_SHOW = 1500

np.random.seed(3)
seed(3)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    # Predict a line
    line = Line(SLOPE, INTERCEPT, (X_MIN, X_MAX), (Y_MIN, Y_MAX))
    double_line = DoubleLine(SLOPE, TWO_INTERCEPT, (X_MIN, X_MAX), (Y_MIN, Y_MAX))

    # Initialize perceptron
    neuron_line = Neuron("Learn line", 2, tanh, 0.1)
    neuron_double = Neuron("Learn two lines", 2, tanh, 0.1)

    # Random dataset
    train_set = line.training_set(N)
    test_set = line.training_set(TO_SHOW)
    train_set2 = double_line.training_set(N)
    test_set2 = double_line.training_set(TO_SHOW)

    # First plot
    fig, axes = plt.subplots(2, 3, figsize=FIG_SIZE)
    prediction1 = do_prediction(neuron_line, test_set)
    prediction2 = do_prediction(neuron_double, test_set2)
    logging.info("First Plot")
    plot_result(test_set, np.array(prediction1), line, axes[0, 0], 0.0)
    axes[0, 0].set_title("Before training\n", fontsize=20)
    logging.info("Second Plot")
    plot_result(test_set2, np.array(prediction2), double_line, axes[1, 0], 0.0)

    for (x, y, label), (x2, y2, label2) in zip(train_set.T.tolist(), train_set2.T.tolist()):
        i = neuron_line.train([x, y], label)
        j = neuron_double.train([x2, y2], label2)
        if i == 10:
            prediction1 = do_prediction(neuron_line, test_set)
            prediction2 = do_prediction(neuron_double, test_set2)
            logging.info("Third Plot")
            plot_result(test_set, np.array(prediction1), line, axes[0, 1], 0.0)
            axes[0, 1].set_title("After 10 examples\n", fontsize=20)
            logging.info("Forth Plot")
            plot_result(test_set2, np.array(prediction2), double_line, axes[1, 1], 0.0)

    prediction1 = do_prediction(neuron_line, test_set)
    prediction2 = do_prediction(neuron_double, test_set2)
    logging.info("Fifth Plot")
    plot_result(test_set, np.array(prediction1), line, axes[0, 2], 0.0)
    axes[0, 2].set_title("After training, 100 examples\n", fontsize=20)
    logging.info("Sixth Plot")
    plot_result(test_set2, np.array(prediction2), double_line, axes[1, 2], 0.0)

    plt.savefig("../results/example_neuron.png")
