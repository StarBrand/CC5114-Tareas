import numpy as np
from matplotlib.axes import Axes


def annotate(ax: Axes, label_matrix: np.ndarray, font_size: int, add_label: np.ndarray or None = None) -> None:
    for i, matrix in enumerate(label_matrix):
        for j, text in enumerate(matrix):
            text_to_show = text
            if add_label is not None:
                text_to_show = "{}{}".format(add_label[i, j], text)
            ax.text(j, i, text_to_show, ha="center", va="center", fontsize=font_size)


def show_matrix(ax: Axes, matrix: np.ndarray, ax_label: ([str], [str]), title: str,
                font_size: int, title_size: int, add_label: np.ndarray or None = None) -> None:
    ax.matshow(matrix)
    annotate(ax, matrix, title_size, add_label)
    ax.set_xticklabels([""] + ax_label[0], fontsize=font_size)
    ax.set_yticklabels([""] + ax_label[1], fontsize=font_size)
    ax.set_title(title, fontsize=title_size)
