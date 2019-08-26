import matplotlib.pyplot as plt
import numpy as np
import logging
from random import seed
from neural_network import NeuralNetwork
from utils.math_functions import sigmoid, tanh
from utils.preprocess_dataset import import_data, split_set, one_hot_encoding
from utils.results import confusion_matrix, accuracy, precision, recall, f1_score

FIG_SIZE = (20, 20)
TRAIN_SIZE = 0.8
LR = 0.01
N = int(1e4)

np.random.seed(123)
seed(123)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    # Initialize neuron
    network = NeuralNetwork(4, [6], 3, [tanh, sigmoid], LR)

    # iris dataset
    dataset = import_data("../../data/iris.data")

    train_set, test_set = split_set(dataset, TRAIN_SIZE)

    labels, _ = one_hot_encoding(train_set[-1])

    learn, costs = network.train(train_set[0:-1], labels.T, epochs=N, repeat=True)

    fig, ax = plt.subplots(figsize=FIG_SIZE)
    ax.plot(learn)
    ax.plot(costs)

    labels, _ = one_hot_encoding(test_set[-1].reshape(-1))

    c_m = confusion_matrix(network.feed_forward(test_set[0:-1]), labels.T)
    print("Confusion matrix:\n{}".format(c_m))
    print("Accuracy:\t{}".format(accuracy(c_m)))
    print("Precision:\t{}".format(precision(c_m)))
    print("Recall:\t{}".format(recall(c_m)))
    print("f1-score:\t{}".format(f1_score(c_m)))

    plt.savefig("../results/network_on_iris.png")
