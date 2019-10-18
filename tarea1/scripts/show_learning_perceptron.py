"""show_learning_perceptron.py: Show Learning Perceptron performance"""

import matplotlib.pyplot as plt
import numpy as np
import logging
from random import seed
from learning_perceptron import LearningPerceptron
from useful.patterns import Line
from useful1 import plot_result, do_prediction

FIG_SIZE = (12 * 3, 12)
X_MIN = Y_MIN = -50
X_MAX = Y_MAX = 50
SLOPE = (-2.0, 2.0)
INTERCEPT = (-10.0, 10.0)
N = 100
TO_SHOW = 1500

np.random.seed(3)
seed(3)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    # Predict a line
    line = Line(SLOPE, INTERCEPT, (X_MIN, X_MAX), (Y_MIN, Y_MAX))

    # Initialize perceptron
    perceptron = LearningPerceptron("learning perceptron", 2, 0.1)

    # Random dataset
    train_set = line.training_set(N)
    test_set = line.training_set(TO_SHOW)

    # First plot
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=FIG_SIZE)
    prediction = do_prediction(perceptron, test_set)
    logging.info("First Plot")
    plot_result(test_set, np.array(prediction), line, ax1)
    ax1.set_title("Before training\n", fontsize=20)

    for x, y, label in train_set.T.tolist():
        i = perceptron.train([x, y], label)
        if i == 10:
            prediction = do_prediction(perceptron, test_set)
            logging.info("Second Plot")
            plot_result(test_set, np.array(prediction), line, ax2)
            ax2.set_title("After 10 examples\n", fontsize=20)

    prediction = do_prediction(perceptron, test_set)
    logging.info("Third Plot")
    plot_result(test_set, np.array(prediction), line, ax3)
    ax3.set_title("After training, 100 examples\n", fontsize=20)

    plt.savefig("../results/example_perceptron.png")
