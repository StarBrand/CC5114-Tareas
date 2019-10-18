"""neuron_on_iris.py: show performance of a neuron on iris dataset"""
import matplotlib.pyplot as plt
import numpy as np
import logging
from random import seed
from learning_perceptron import Neuron
from useful.math_functions import sigmoid
from useful.preprocess_dataset import import_data, split_set
from useful.results import confusion_matrix, accuracy, recall

FIG_SIZE = (20, 20)
TRAIN_SIZE = 0.8
LR = 0.5

np.random.seed(123)
seed(123)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    # Initialize neuron
    neuron = Neuron("On iris", 4, sigmoid, LR)

    # iris dataset
    dataset = import_data("../../data/iris.data").T[0:100].T

    dataset[4][0:50] = 1.0
    dataset[4][50:100] = 0.0

    train_set, test_set = split_set(dataset, TRAIN_SIZE)

    epochs = []
    accuracies = []
    recalls = []

    for x1, x2, x3, x4, label in train_set.T.tolist():
        epochs.append(
            neuron.train([x1, x2, x3, x4], label)
        )
        prediction = []
        labels = []
        for y1, y2, y3, y4, label2 in test_set.T.tolist():
            prediction.append(neuron.feed([y1, y2, y3, y4]))
            labels.append(label2)

        c_m = confusion_matrix(np.array(prediction), np.array(labels))
        accuracies.append(accuracy(c_m))
        recalls.append(recall(c_m)[0])

    fig, ax = plt.subplots(figsize=FIG_SIZE)
    ax.plot(epochs, accuracies, label="Accuracy", linewidth=3.5)
    ax.plot(epochs, recalls, "--", label="Recall", linewidth=2.0)
    ax.set_xlabel("Epochs", fontsize=20)
    ax.set_ylabel("Measure", fontsize=20)
    ax.set_title("Sigmoid neuron on Iris Dataset\n", fontsize=30)
    ax.legend(fontsize=20)
    ax.grid()

    plt.savefig("../results/neuron_on_iris.png")
