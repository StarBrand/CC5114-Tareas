import numpy as np
import matplotlib.pyplot as plt
from utils.patterns import Circle
from utils.results import confusion_matrix
from utils.results import accuracy, precision, recall, f1_score
from useful import annotate

N = int(1e5)
X_MIN = Y_MIN = -50
X_MAX = Y_MAX = 50
FIG_SIZE = (12, 12)
MEASURE_SIZE = (4, 2)
np.random.seed(2)


if __name__ == '__main__':
    labels = Circle(30, (0, 0), (X_MIN, X_MAX), (Y_MIN, Y_MAX)).training_set(N)[2]
    prediction = np.abs(np.random.randn(N))
    matrix = confusion_matrix(prediction, labels)
    _, ax = plt.subplots(figsize=FIG_SIZE)
    ax.matshow(matrix)
    annotate(ax, matrix, 30, np.array([["TP: ", "FN: "], ["FP: ", "TN: "]]))
    ax.set_xticklabels(["", "Outside Circle", "Inside Circle"], fontsize=20)
    ax.set_yticklabels(["", "Predicted\nOutside", "Predicted\nInside"], fontsize=20)
    ax.set_title("Confusion matrix of a circle\n", fontsize=30)
    plt.savefig("../results/confusion_matrix_one_class")
    fig, ax = plt.subplots(figsize=MEASURE_SIZE)
    measures = np.zeros((2, 4))
    ax.matshow(measures, cmap="Greys")
    to_show = np.zeros((2, 4))
    to_show[0][0] = round(accuracy(matrix), 4)
    _precision = precision(matrix)
    to_show[0][1] = round(_precision[0], 4)
    to_show[1][1] = round(_precision[1], 4)
    _recall = recall(matrix)
    to_show[0][2] = round(_recall[0], 4)
    to_show[1][2] = round(_recall[1], 4)
    _f1_score = f1_score(matrix)
    to_show[0][3] = round(_f1_score[0], 4)
    to_show[1][3] = round(_f1_score[1], 4)
    annotate(ax, np.array(to_show), 8, np.array([["Accuracy:\n", "Precision\noutside:\n", "Recall\noutside:\n",
                                                  "f1-score\noutside:\n"],
                                                 ["", "Precision\ninside:\n", "Recall\ninside:\n",
                                                  "f1-score\ninside:\n"]]))
    ax.set_axis_off()
    plt.savefig("../results/measure_one_class")
