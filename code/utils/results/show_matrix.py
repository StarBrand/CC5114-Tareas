"""show_matrix.py: methods to show confusion matrix"""
import numpy as np
from matplotlib.axes import Axes


def annotate(ax: Axes, label_matrix: np.ndarray, font_size: int, add_label: np.ndarray or None = None) -> None:
    """
    Add names and data to confusion matrix graph

    :param ax: Axes of confusion matrix graph
    :param label_matrix: labels
    :param font_size: Size of letters
    :param add_label: (optional) labels (class names)
    :return: None, modify ax
    """
    for i, matrix in enumerate(label_matrix):
        for j, text in enumerate(matrix):
            text_to_show = text
            if add_label is not None:
                text_to_show = "{}{}".format(add_label[i, j], text)
            ax.text(j, i, text_to_show, ha="center", va="center", fontsize=font_size)


def show_matrix(ax: Axes, matrix: np.ndarray, ax_label: ([str], [str]), title: str, font_size: int, title_size: int,
                color_map: str or None = None, add_label: np.ndarray or None = None) -> None:
    """
    Show matrix adding it to ax

    :param ax: Axes in which matrix will be shown
    :param matrix: confusion matrix
    :param ax_label: Labels
    :param title: Title
    :param font_size: Size of test
    :param title_size: Size of title
    :param color_map: Colormap from matplotlib, if not provided, default colormap (viridis)
    :param add_label: Name of classes
    :return: None, modify ax
    """
    if color_map is not None:
        ax.matshow(matrix, cmap=color_map)
    else:
        ax.matshow(matrix)
    annotate(ax, matrix, title_size, add_label)
    ax.set_xticklabels([""] + ax_label[0], fontsize=font_size)
    ax.set_yticklabels([""] + ax_label[1], fontsize=font_size)
    ax.set_title(title, fontsize=title_size)
