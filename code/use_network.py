import matplotlib.pyplot as plt
import numpy as np
import logging
from argparse import ArgumentParser
from random import seed
from neural_network import NeuralNetwork, NormalizedNetwork
from utils import SHORT, LONG, BIG
from utils.preprocess_dataset import import_data, one_hot_encoding, oversample, undersample
from utils.results import StandardTrainer, KFoldTrainer
from utils.results import confusion_matrix, accuracy, precision, recall, f1_score, show_matrix

FIG_SIZE = (20 * 2, 20)
TITLE_SIZE = 40
FONT_SIZE = 25
TRAIN_SIZE = 0.7
EPOCHS = int(1e3)

np.random.seed(2)
seed(2)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    parser = ArgumentParser()
    parser.add_argument("-n", "--normalize", default=False, action="store_true")
    parser.add_argument("-o", "--oversample", default=False, action="store_true")
    parser.add_argument("-u", "--undersample", default=False, action="store_true")
    parser.add_argument("-x", "--cross_validation", type=int)
    parser.add_argument("-d", "--dataset", default="iris")
    parser.add_argument("-H", "--header", default=None, type=int)
    parser.add_argument("-s", "--sep", default=",")
    parser.add_argument("-c", "--categorical", nargs="+", default=[], type=int)
    parser.add_argument("-l", "--labels", default=-1, type=int)
    parser.add_argument("-e", "--exclude", nargs="+", default=[], type=int)
    parser.add_argument("-O", "--optional_name", default="")
    parser.add_argument("-a", "--architecture", type=str, required=True)

    args = parser.parse_args()

    if args.architecture == "short":
        architecture = SHORT
    elif args.architecture == "long":
        architecture = LONG
    elif args.architecture == "big":
        architecture = BIG
    else:
        raise AttributeError("Options: short, long, big")

    if args.dataset == "uci":
        path_dataset = "Data_for_UCI_named.csv"
    else:
        path_dataset = args.dataset + ".data"

    # import dataset
    dataset = import_data("../data/{}".format(path_dataset), sep=args.sep, header=args.header)

    more_info = ""

    if args.oversample:
        dataset = oversample(dataset, label=args.labels)
        more_info = "(oversampled)"
    if args.undersample:
        dataset = undersample(dataset, label=args.labels)
        more_info = "(undersampled)"

    labels, encoding = one_hot_encoding(dataset[args.labels])
    classes = list(encoding.keys())
    dataset = np.delete(dataset, args.labels, 0)

    encodings = list()

    first = True

    for index in reversed(args.categorical):
        temp1, temp2 = one_hot_encoding(dataset[index])
        dataset = np.concatenate((np.delete(dataset, index, 0), temp1.copy().T))
        encodings.append(temp2.copy())
        del temp1
        del temp2

    dataset = np.delete(dataset, args.exclude, 0)

    # Initialize network
    logging.info("Input size: {}\tOutput size: {}".format(dataset.shape[0], len(encoding)))
    network = NeuralNetwork(dataset.shape[0],
                            architecture["INTERNAL_LAYERS"],
                            len(encoding),
                            architecture["ACT_FUNCS"],
                            architecture["LR"])
    filename = "network"
    type_net = "Neural"
    k_fold = ""

    if args.normalize:
        network = NormalizedNetwork(dataset.shape[0],
                                    architecture["INTERNAL_LAYERS"],
                                    len(encoding),
                                    architecture["ACT_FUNCS"],
                                    architecture["LR"])
        type_net = "Normalized"
        filename = type_net.lower()

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
        trained, (learn, costs) = trainer.train(network, epochs=EPOCHS, repeat=True)

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
    ax.set_title("{} Network on {}\n".format(type_net, args.dataset), fontsize=TITLE_SIZE)
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

    plt.savefig("../tarea1/results/other_dataset/{}_{}_on_{}{}{}{}.png".format(args.architecture,
                                                                               filename, args.dataset, more_info,
                                                                               k_fold, args.optional_name))
