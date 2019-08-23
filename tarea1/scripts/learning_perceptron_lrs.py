import matplotlib.pyplot as plt
import numpy as np
import logging
from random import seed
from learning_perceptron import LearningPerceptron
from utils.patterns import Line
from utils.visualization import plot_result

FIG_SIZE = (20, 15)
X_MIN = Y_MIN = -50
X_MAX = Y_MAX = 50
SLOPE = (-2.0, 2.0)
INTERCEPT = (-10.0, 10.0)
N = 100
TO_SHOW = 10000
LEARNING_RATE = np.linspace(0.01, 0.5, 11)

np.random.seed(3)
seed(3)


def do_prediction(a_perceptron: LearningPerceptron, a_set: np.ndarray) -> [float]:
    ans = []
    for xx, yy, _ in a_set.T.tolist():
        ans.append(a_perceptron.feed([xx, yy]))
    return ans


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    # Predict a line
    line = Line(SLOPE, INTERCEPT, (X_MIN, X_MAX), (Y_MIN, Y_MAX))

    # Random dataset
    train_set = line.training_set(N)
    test_set = line.training_set(TO_SHOW)

    fig, ax = plt.subplots(figsize=FIG_SIZE)

    for lr in LEARNING_RATE:
        epochs = []
        accuracy = []
        perceptron = LearningPerceptron(str(lr), 2, lr)

        for x, y, label in train_set.T.tolist():
            epochs.append(perceptron.train([x, y], label))
            prediction = do_prediction(perceptron, test_set)
            accuracy.append(plot_result(test_set, np.array(prediction), line))

        logging.info("Perceptron with lr: {}".format(lr))
        ax.plot(epochs, accuracy, label="Learning rate: {}".format(lr))

    ax.set_xlabel("Number of examples")
    ax.set_ylabel("Accuracy")
    ax.legend(fontsize=16)
    ax.grid()
    ax.set_title("Different learning rates\n", fontsize=20)

    plt.savefig("../results/perceptron_different_lr.png")
