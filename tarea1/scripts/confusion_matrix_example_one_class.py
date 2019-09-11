"""confusion_matrix_example_one_class.py: show and test confusion matrix methods"""
import numpy as np
import matplotlib.pyplot as plt
from utils.patterns import Circle
from utils.results import confusion_matrix, accuracy, precision, recall, f1_score
from utils.results import show_matrix, annotate

N = int(1e5)
X_MIN = Y_MIN = -50
X_MAX = Y_MAX = 50
FIG_SIZE = (24, 12)
FONT_SIZE = 20
TITLE_SIZE = 30
np.random.seed(2)


if __name__ == '__main__':
    labels = Circle(30, (0, 0), (X_MIN, X_MAX), (Y_MIN, Y_MAX)).training_set(N)[2]
    prediction = np.abs(np.random.randn(N))
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FIG_SIZE)
    matrix = confusion_matrix(prediction, labels)
    show_matrix(ax1, matrix, (["Outside Circle", "Inside Circle"],
                ["Predicted\nOutside", "Predicted\nInside"]), "Confusion matrix of a circle\n",
                FONT_SIZE, TITLE_SIZE, add_label=np.array([["TP: ", "FN: "], ["FP: ", "TN: "]]))
    measures = np.zeros((2, 4))
    ax2.matshow(measures, cmap="Greys")
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
    annotate(ax2, np.array(to_show), 25, np.array([["Accuracy:\n", "Precision\noutside:\n", "Recall\noutside:\n",
                                                    "f1-score\noutside:\n"],
                                                   ["", "Precision\ninside:\n", "Recall\ninside:\n",
                                                    "f1-score\ninside:\n"]]))
    ax2.set_axis_off()
    plt.savefig("../results/confusion_matrix_one_class")
