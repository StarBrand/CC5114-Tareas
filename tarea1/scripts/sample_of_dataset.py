"""sample_of_dataset.py: show performance of set methods"""
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from utils.preprocess_dataset import import_data, split_set, one_hot_encoding

FIG_SIZE = (12, 9)
FONT_SIZE = 12
TITLE_SIZE = 20


def format_axes(title: str, scale: int, ax: Axes) -> None:
    """
    Format axes of a matplotlib graph

    :param title: Title
    :param scale: Scale
    :param ax: Axes of matplotlib
    :return: None, modify ax
    """
    ax.set_title("{}\n".format(title), fontsize=TITLE_SIZE)
    ax.set_aspect(aspect=str(6 * scale))
    ax.set_xlabel("Indexes", fontsize=FONT_SIZE)
    ax.grid()


if __name__ == '__main__':
    fig, axes = plt.subplots(3, 1, figsize=FIG_SIZE)
    dataset = import_data("../../data/iris.data")
    one_hot_dataset, encoding = one_hot_encoding(dataset[4])
    axes[0].imshow(one_hot_dataset.T, cmap='Greys')
    format_axes(
        "Labels of dataset, size: {}".format(one_hot_dataset.shape[0]),
        one_hot_dataset.shape[0] / 150,
        axes[0]
    )
    train_set, test_set = split_set(one_hot_dataset.T, 0.6)
    axes[1].imshow(train_set, cmap='Greys')
    format_axes(
        "Train set, size: {}".format(train_set.shape[1]),
        train_set.shape[1] / 150,
        axes[1]
    )
    axes[2].imshow(test_set, cmap='Greys')
    format_axes(
        "Test set, size: {}".format(test_set.shape[1]),
        test_set.shape[1] / 150,
        axes[2]
    )
    plt.savefig("../results/labels_of_dataset.png")
