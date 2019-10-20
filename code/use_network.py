"""use_network.py: use a network (normalized or not) on a dataset"""

import matplotlib.pyplot as plt
import numpy as np
import logging
from argparse import ArgumentParser
from random import seed
from neural_network import NeuralNetwork, NormalizedNetwork
from useful import SHORT, LONG, BIG
from useful.preprocess_dataset import import_data, one_hot_encoding, oversample, undersample
from useful.results import StandardTrainer, KFoldTrainer
from useful.results import confusion_matrix, accuracy, precision, recall, f1_score, show_matrix

FIG_SIZE = (20 * 2, 20)
TITLE_SIZE = 40
FONT_SIZE = 25
TRAIN_SIZE = 0.7
EPOCHS = int(1e3)

np.random.seed(2)
seed(2)


def report_results(confusion: np.ndarray) -> None:
    """
    Report results of a training process

    :param confusion: Confusion matrix with result of training
    :return: None (print results measures)
    """
    measures = {
        "accuracy": accuracy(confusion),
        "precision": precision(confusion),
        "recall": recall(confusion),
        "f1_score": f1_score(confusion)
    }

    print("| Clases\t| *Accuracy* | *Precision* | *Recall* | *f1-score* |")
    print("| --------------- | ---------- | ----------- | -------- | ---------- |")
    accuracy_measure = round(measures["accuracy"], 4)
    for index, a_class in enumerate(classes):
        print("| **{name}** | {accuracy} | {precision} | {recall} | {f1_score} |".format(
            name=a_class, accuracy=accuracy_measure,
            precision=round(measures["precision"][index], 4),
            recall=round(measures["recall"][index], 4),
            f1_score=round(measures["f1_score"][index], 4))
        )
        accuracy_measure = ""
    print("\n")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    parser = ArgumentParser()
    parser.add_argument("-n", "--normalize", default=False, action="store_true",
                        help="Normalize the input")
    parser.add_argument("-o", "--oversample", default=False, action="store_true",
                        help="Oversample the dataset using the most representative class")
    parser.add_argument("-u", "--undersample", default=False, action="store_true",
                        help="Undersample the dataset using the less representative class")
    parser.add_argument("-x", "--cross_validation", type=int,
                        help="Select k value for kFold cross validation, "
                             "if not specify, split dataset 70-30 train-test set")
    parser.add_argument("-H", "--header", default=None, type=int,
                        help="If needed, specify indicate in which row is the header of the dataset")
    parser.add_argument("-s", "--sep", default=",",
                        help="Character that indicates column delimiter (',' by default)")
    parser.add_argument("-c", "--categorical", nargs="+", default=[], type=int,
                        help="Indicates categorical attributes on dataset")
    parser.add_argument("-l", "--labels", default=-1, type=int,
                        help="Indicates which attribute contains the labels of class (last one by default)")
    parser.add_argument("-e", "--exclude", nargs="+", default=[], type=int,
                        help="Indicates attributes (columns) to exclude for classification")
    parser.add_argument("-O", "--optional_name", default="",
                        help="Add an optional string to the name of the output graphs")
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument("-d", "--dataset", required=True,
                               help="Dataset name on data folder (without file name extension)")
    required_args.add_argument("-a", "--architecture", type=str, required=True,
                               help="Architecture to use, available: short, long and big")

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

    for i in reversed(args.categorical):
        temp1, temp2 = one_hot_encoding(dataset[i])
        dataset = np.concatenate((np.delete(dataset, i, 0), temp1.copy().T))
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

    show_matrix(ax3, c_m, (classes, ["Predicted\n{}".format(a_class) for a_class in classes]),
                "Confusion Matrix of Test Set\n", FONT_SIZE, TITLE_SIZE)

    print("{}\n".format(args))
    report_results(c_m)

    plt.savefig("../tarea1/results/other_dataset/{}_{}_on_{}{}{}{}.png".format(args.architecture,
                                                                               filename, args.dataset, more_info,
                                                                               k_fold, args.optional_name))
