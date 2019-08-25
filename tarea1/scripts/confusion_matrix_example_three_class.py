import numpy as np
import matplotlib.pyplot as plt
from utils.preprocess_dataset import import_data, one_hot_encoding
from utils.results import confusion_matrix
from utils.results import accuracy, precision, recall, f1_score
from useful import annotate

N = int(1e5)
X_MIN = Y_MIN = -50
X_MAX = Y_MAX = 50
FIG_SIZE = (28, 12)
np.random.seed(2)


if __name__ == '__main__':
    dataset = import_data("../../data/iris.data")[4]
    classes = np.unique(dataset)
    labels, _ = one_hot_encoding(dataset)
    prediction, _ = one_hot_encoding(np.random.choice(["a", "b", "c"], size=labels.shape[0], replace=True))
    matrix = confusion_matrix(prediction.T, labels.T)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FIG_SIZE)
    ax1.matshow(matrix)
    annotate(ax1, matrix, 30)
    ax1.set_xticklabels(["", classes[0], classes[1], classes[2]], fontsize=20)
    ax1.set_yticklabels(["", "Predicted\n" + classes[0], "Predicted\n" + classes[1], "Predicted\n" + classes[2]],
                        fontsize=20)
    ax1.set_title("Confusion matrix of a iris dataset\n", fontsize=30)
    measures = np.zeros((3, 4))
    ax2.matshow(measures, cmap="Greys")
    to_show = np.zeros((3, 4))
    to_show[0][0] = round(accuracy(matrix), 4)
    to_show[1][0] = np.nan
    to_show[2][0] = np.nan
    _precision = precision(matrix)
    to_show[0][1] = round(_precision[0], 4)
    to_show[1][1] = round(_precision[1], 4)
    to_show[2][1] = round(_precision[2], 4)
    _recall = recall(matrix)
    to_show[0][2] = round(_recall[0], 4)
    to_show[1][2] = round(_recall[1], 4)
    to_show[2][2] = round(_recall[2], 4)
    _f1_score = f1_score(matrix)
    to_show[0][3] = round(_f1_score[0], 4)
    to_show[1][3] = round(_f1_score[1], 4)
    to_show[2][3] = round(_f1_score[2], 4)
    annotate(ax2, np.array(to_show), 25, np.array([["Accuracy:\n", "Precision\n{}:\n".format(classes[0]),
                                                    "Recall\n{}:\n".format(classes[0]),
                                                    "f1-score\n{}:\n".format(classes[0])],
                                                   ["{}:\n".format(classes[1]), "Precision:\n",
                                                    "Recall:\n", "f1-score:\n"],
                                                   ["{}:\n".format(classes[2]), "Precision:\n",
                                                    "Recall:\n", "f1-score:\n"]]))
    ax2.set_axis_off()
    plt.savefig("../results/confusion_matrix_three_class")
