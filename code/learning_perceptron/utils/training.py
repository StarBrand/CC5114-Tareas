import matplotlib.pyplot as plt
from random import uniform
from matplotlib.axes import Axes
from learning_perceptron import LearningPerceptron
from learning_perceptron.utils import Line, results, confusion_matrix,\
    accuracy, precision, recall, f1_score


def training_set(size: int, line: Line) -> [(float, float, bool)]:
    out = []
    for i in range(size):
        x = uniform(line.MIN_X, line.MAX_X)
        y = uniform(line.MIN_Y, line.MAX_Y)
        datum = x, y, line.above_line(x, y)
        out.append(datum)
    return out


def train(perceptron: LearningPerceptron, n: int,
          size: int, line: Line, label: str or None = None,
          ax_acc: Axes or None = None,
          ax_pr: Axes or None = None,
          ax_rc: Axes or None = None,
          ax_f1: Axes or None = None,) -> ([int], [float], [float], [float], [float]):
    accuracy_data = []
    precision_data = []
    recall_data = []
    f1_score_data = []
    number_of_training = []
    training = training_set(size, line)

    range_x = (line.MIN_X, line.MAX_X)
    range_y = (line.MIN_Y, line.MAX_Y)

    for i in range(size + 1):
        if i != 0:
            perceptron.train([training[i - 1]])
        x1, y1, x2, y2 = results(perceptron, range_x, range_y, n)
        fp, tp, fn, tn = confusion_matrix(line, x1, y1, x2, y2)
        accuracy_data.append(accuracy(fp, tp, fn, tn))
        precision_data.append(precision(fp, tp))
        recall_data.append(recall(tp, fn))
        f1_score_data.append(f1_score(fp, tp, fn))
        number_of_training.append(perceptron.number_of_training)

    if label is None:
        label = ""
    if ax_acc is not None:
        ax_acc.plot(number_of_training, accuracy_data, label="{} accuracy".format(label))
    if ax_pr is not None:
        ax_pr.plot(number_of_training, precision_data, label="{} precision".format(label))
    if ax_rc is not None:
        ax_rc.plot(number_of_training, recall_data, label="{} recall".format(label))
    if ax_f1 is not None:
        ax_f1.plot(number_of_training, f1_score_data, label="{} f1-score".format(label))

    return training, accuracy_data, precision_data, recall_data, f1_score_data


def particular_train(perceptron: LearningPerceptron, size: int, n: int, line: Line) -> None:

    fig, ax = plt.subplots(figsize=(5, 5))

    _, acc, pr, rc, f1 = train(perceptron, n, size, line, ax_acc=ax, ax_pr=ax, ax_rc=ax, ax_f1=ax)

    ax.set_xlabel("number of training", fontsize=12)
    ax.set_ylabel("measure", fontsize=12)
    ax.set_title("training {} with {} trainings".format(perceptron.name, perceptron.number_of_training), fontsize=14)
    ax.grid()
    ax.legend(fontsize=12)

    print(
        "Measures:\n\taccuracy: {}\n\tprecision: {}\n\trecall: {}\n\tf1-score: {}".format(
            acc[-1], pr[-1], rc[-1], f1[-1]
        )
    )

    return
