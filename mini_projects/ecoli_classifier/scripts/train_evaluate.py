"""train_evaluate.py: Train and evaluate dataset"""
import matplotlib.pyplot as plt
import numpy as np
import logging
from random import seed
from neural_network import NeuralNetwork
from utils.preprocess_dataset import import_data, one_hot_encoding, oversample
from utils.results import StandardTrainer
from utils.results import confusion_matrix, accuracy, precision, recall, f1_score, show_matrix

FIG_SIZE = (20 * 2, 20)
TITLE_SIZE = 40
FONT_SIZE = 25
TRAIN_SIZE = 0.7
EPOCHS = int(1e3)

ARCHITECTURE_CYTOPLASM = {
    "INTERNAL_LAYERS": [6],
    "ACT_FUNCS": ["tanh", "sigmoid"],
    "LR": 0.05
}

ARCHITECTURE_MEMBRANE = {
    "INTERNAL_LAYERS": [6],
    "ACT_FUNCS": ["tanh", "sigmoid"],
    "LR": 0.05
}

ARCHITECTURE_INNER_MEMBRANE = {
    "INTERNAL_LAYERS": [6],
    "ACT_FUNCS": ["tanh", "sigmoid"],
    "LR": 0.05
}

ARCHITECTURE_OUTER_MEMBRANE = {
    "INTERNAL_LAYERS": [],
    "ACT_FUNCS": ["tanh"],
    "LR": 0.05
}

np.random.seed(2)
seed(2)


def train_evaluate(architecture: dict, dataset_name: str) -> NeuralNetwork:
    """
    Train and evaluate a Network

    :param architecture: Architecture of NeuralNetwork (above)
    :param dataset_name: Dataset to use
    :return: Trained Neural Network
    """
    # import dataset
    dataset = import_data("../data/{}.data".format(dataset_name))

    dataset = oversample(dataset)
    more_info = "(oversample)"

    labels, encoding = one_hot_encoding(dataset[-1])
    classes = list(encoding.keys())
    dataset = np.delete(dataset, -1, 0)

    dataset = np.delete(dataset, [0], 0)

    # Initialize network
    logging.info("Input size: {}\tOutput size: {}".format(dataset.shape[0], len(encoding)))
    network = NeuralNetwork(dataset.shape[0],
                            architecture["INTERNAL_LAYERS"],
                            len(encoding),
                            architecture["ACT_FUNCS"],
                            architecture["LR"])

    # Define Trainer
    trainer = StandardTrainer(dataset, labels.T, TRAIN_SIZE)

    fig = plt.figure(figsize=FIG_SIZE)
    fig.subplots_adjust(wspace=0.3)
    ax = fig.add_subplot(121)
    ax2 = ax.twinx()
    ax3 = fig.add_subplot(122)

    trained, (learn, costs) = trainer.train(network, epochs=EPOCHS, repeat=True)

    prediction = trainer.evaluate(trained)

    c_m = confusion_matrix(prediction, trainer.get_labels())

    line = ax.plot(learn, label="Learning Curve", linewidth=2.5, c="b")

    line2 = ax2.plot(costs, label="MSE", linestyle="--", linewidth=2.5, c="r")
    lines = line + line2

    ax.set_ylabel("Learning Curve", fontsize=FONT_SIZE)
    ax.set_xlabel("Epochs", fontsize=FONT_SIZE)
    ax.set_title("Network on {}\n".format(dataset_name), fontsize=TITLE_SIZE)
    ax.grid()

    ax2.set_ylabel("Cost", fontsize=FONT_SIZE)
    ax2.grid()

    labels = [l.get_label() for l in lines]
    ax2.legend(lines, labels, fontsize=FONT_SIZE, loc="center right")

    show_matrix(ax3, c_m, (classes, ["Predicted\n{}".format(a_class) for a_class in classes]),
                "Confusion Matrix of Test Set\n", FONT_SIZE, TITLE_SIZE)

    measures = {
        "accuracy": accuracy(c_m),
        "precision": precision(c_m),
        "recall": recall(c_m),
        "f1_score": f1_score(c_m)
    }

    print("Summary on {}:\n".format(dataset))
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

    plt.savefig("../results/Network_on_{}{}.png".format(dataset_name, more_info))

    return trained


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    # Cytoplasm
    logging.info("Train network to separate on cytoplasm and membrane")
    network_cytoplasm = train_evaluate(ARCHITECTURE_CYTOPLASM, "ecoli_dual")

    # Membrane
    logging.info("Train network to separate membrane proteins")
    network_membrane = train_evaluate(ARCHITECTURE_MEMBRANE, "ecoli_membrane")

    # Inner Membrane
    logging.info("Train network to separate inner membrane proteins")
    network_inner = train_evaluate(ARCHITECTURE_INNER_MEMBRANE, "ecoli_inner")

    # Outer Membrane
    logging.info("Train network to separate outer membrane proteins")
    network_outer = train_evaluate(ARCHITECTURE_OUTER_MEMBRANE, "ecoli_outer")
