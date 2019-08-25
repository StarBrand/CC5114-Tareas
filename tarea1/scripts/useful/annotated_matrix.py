import numpy as np
from matplotlib.axes import Axes


def annotate(ax: Axes, label_matrix: np.ndarray, font_size: int, add_label: np.ndarray or None = None):
    for i, matrix in enumerate(label_matrix):
        for j, text in enumerate(matrix):
            text_to_show = text
            if add_label is not None:
                text_to_show = "{}{}".format(add_label[i, j], text)
            ax.text(j, i, text_to_show, ha="center", va="center", fontsize=font_size)
