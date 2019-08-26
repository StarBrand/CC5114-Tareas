import matplotlib.pyplot as plt
import numpy as np
import logging
from argparse import ArgumentParser
from random import seed
from neural_network import NeuralNetwork, NormalizedNetwork
from useful import show_matrix
from utils.math_functions import sigmoid, tanh
from utils.preprocess_dataset import import_data, split_set, one_hot_encoding
from utils.results import confusion_matrix, accuracy, precision, recall, f1_score

FIG_SIZE = (20 * 2, 20)
TITLE_SIZE = 40
FONT_SIZE = 25
TRAIN_SIZE = 0.7
LR = 0.01
N = int(1e4)

np.random.seed(2)
seed(2)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    parser = ArgumentParser()
    parser.add_argument("-n", "--normalize", default=False, action="store_true")

    args = parser.parse_args()
    # Initialize network
    network = NeuralNetwork(4, [6], 3, [tanh, sigmoid], LR)
    filename = "network"
    type_net = "Neural"

    if args.normalize:
        network = NormalizedNetwork(4, [6], 3, [tanh, sigmoid], LR)
        type_net = "Normalized"
        filename = type_net.lower()

    # iris dataset
    dataset = import_data("../../data/iris.data")

    train_set, test_set = split_set(dataset, TRAIN_SIZE)

    labels, encoding = one_hot_encoding(train_set[-1])
    classes = list(encoding.keys())

    learn, costs = network.train(train_set[0:-1], labels.T, epochs=N, repeat=True)

    fig = plt.figure(figsize=FIG_SIZE)
    fig.subplots_adjust(wspace=0.3)
    ax = fig.add_subplot(121)
    ax3 = fig.add_subplot(122)

    line = ax.plot(learn, label="Learning Curve", c="b", linewidth=2.5)
    ax.set_ylabel("Learning Curve", fontsize=FONT_SIZE)
    ax.set_xlabel("Epochs", fontsize=FONT_SIZE)
    ax.set_title("{} Network on Iris\n".format(type_net), fontsize=TITLE_SIZE)
    ax.grid()

    ax2 = ax.twinx()
    line2 = ax2.plot(costs, label="MSE", c="r", linewidth=2.5)
    ax2.set_ylabel("Cost", fontsize=FONT_SIZE)
    ax2.grid()

    lines = line + line2
    labels = [l.get_label() for l in lines]
    ax2.legend(lines, labels, fontsize=FONT_SIZE)

    labels, _ = one_hot_encoding(test_set[-1].reshape(-1))

    c_m = confusion_matrix(network.feed_forward(test_set[0:-1]), labels.T)

    show_matrix(ax3, c_m, (classes, ["Predicted\n{}".format(iris) for iris in classes]),
                "Confusion Matrix of Test Set\n", FONT_SIZE, TITLE_SIZE)

    print("Accuracy:\t{}".format(accuracy(c_m)))
    print("Precision:\t{}".format(precision(c_m)))
    print("Recall:\t{}".format(recall(c_m)))
    print("f1-score:\t{}".format(f1_score(c_m)))

    plt.savefig("../results/{}_on_iris.png".format(filename))
