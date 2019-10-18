"""network_on_iris.py: show performance of a neural network on iris dataset"""
import matplotlib.pyplot as plt
import numpy as np
import logging
from argparse import ArgumentParser
from random import seed
from neural_network import NeuralNetwork, NormalizedNetwork
from useful.math_functions import sigmoid, tanh
from useful.preprocess_dataset import import_data, one_hot_encoding
from useful.results import StandardTrainer, KFoldTrainer
from useful.results import confusion_matrix, accuracy, precision, recall, f1_score, show_matrix

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
    parser.add_argument("-x", "--cross_validation", type=int)

    args = parser.parse_args()

    # Initialize network
    network = NeuralNetwork(4, [6], 3, [tanh, sigmoid], LR)
    filename = "network"
    type_net = "Neural"
    k_fold = ""

    if args.normalize:
        network = NormalizedNetwork(4, [6], 3, [tanh, sigmoid], LR)
        type_net = "Normalized"
        filename = type_net.lower()

    # iris dataset
    dataset = import_data("../../data/iris.data")

    labels, encoding = one_hot_encoding(dataset[-1])
    classes = list(encoding.keys())
    dataset = dataset[0:-1]

    # Define Trainer
    trainer = StandardTrainer(dataset, labels.T, TRAIN_SIZE)
    k = 1

    if args.cross_validation is not None:
        k = args.cross_validation
        k_fold = "_{}fold".format(k)
        trainer = KFoldTrainer(k, 2, dataset, labels.T)

    fig = plt.figure(figsize=FIG_SIZE)
    fig.subplots_adjust(wspace=0.3)
    ax = fig.add_subplot(121)
    ax2 = ax.twinx()
    ax3 = fig.add_subplot(122)
    lines = []
    c_m = np.array([])
    iteration = ""

    for i in range(k):
        trained, (learn, costs) = trainer.train(network, epochs=N, repeat=True)

        prediction = trainer.evaluate(trained)

        if c_m.shape != (0, ):
            c_m = c_m + confusion_matrix(prediction, trainer.get_labels())
        else:
            c_m = confusion_matrix(prediction, trainer.get_labels())

        line = ax.plot(learn, label="Learning Curve", linewidth=2.5)

        if k != 1:
            iteration = " iteration: {}".format(i + 1)
            c = line[0].get_color()
        else:
            c = "r"

        line2 = ax2.plot(costs, label="MSE{}".format(iteration), linestyle="--", linewidth=2.5, c=c)
        lines = lines + line + line2

    ax.set_ylabel("Learning Curve", fontsize=FONT_SIZE)
    ax.set_xlabel("Epochs", fontsize=FONT_SIZE)
    ax.set_title("{} Network on Iris\n".format(type_net), fontsize=TITLE_SIZE)
    ax.grid()

    ax2.set_ylabel("Cost", fontsize=FONT_SIZE)
    ax2.grid()

    labels = [l.get_label() for l in lines]
    ax2.legend(lines, labels, fontsize=FONT_SIZE, loc="center right")

    show_matrix(ax3, c_m, (classes, ["Predicted\n{}".format(iris) for iris in classes]),
                "Confusion Matrix of Test Set\n", FONT_SIZE, TITLE_SIZE)

    print("Accuracy:\t{}".format(accuracy(c_m)))
    print("Precision:\t{}".format(precision(c_m)))
    print("Recall:\t{}".format(recall(c_m)))
    print("f1-score:\t{}".format(f1_score(c_m)))

    plt.savefig("../results/{}_on_iris{}.png".format(filename, k_fold))
