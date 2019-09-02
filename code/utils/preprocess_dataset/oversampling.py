import numpy as np
import logging


class Representation(object):

    def __init__(self, class_name: str, rows: np.ndarray, length: int):
        self.class_name = class_name
        self.rows = rows
        self.length = length
        return


def oversample(dataset: np.ndarray, to_size: int or None = None, label: int = -1) -> np.ndarray:
    logging.info("Oversampling...")
    return _sample(dataset, label, True, "most", to_size)


def undersample(dataset: np.ndarray, to_size: int or None = None, label: int = -1) -> np.ndarray:
    logging.info("Undersampling...")
    return _sample(dataset, label, False, "less", to_size)


def _sample(dataset: np.ndarray, label: int, reverse: bool, sample_type: str, to_size: int or None) -> np.ndarray:
    representation = list()
    classes = np.unique(dataset[label])
    for a_class in classes:
        temp = dataset[..., dataset[label] == a_class]
        representation.append(Representation(a_class,
                                             temp.copy(),
                                             temp.shape[-1]))
    first = True
    target = 0
    new_dataset = np.array([])
    for _, a_class in sorted([(a_class.length, a_class) for a_class in representation], reverse=reverse):
        if first:
            target = a_class.length
            logging.info("{}, {} representative class has {} rows".format(a_class.class_name, sample_type, target))
            if to_size is not None:
                target = to_size
                mask = np.random.choice(a_class.rows.shape[-1], target)
                new_dataset = np.take(a_class.rows, mask, axis=-1)
                logging.info(
                    "Class name: {}:\n\toriginal representation: {} rows\tactual representation: {} rows".format(
                        a_class.class_name, a_class.rows.shape[-1], mask.shape[0])
                )
            else:
                new_dataset = a_class.rows.copy()
            first = False
        else:
            mask = np.random.choice(a_class.rows.shape[-1], target)
            new_dataset = np.concatenate((new_dataset.copy(),
                                          np.take(a_class.rows, mask, axis=-1)), axis=-1)
            logging.info("Class name: {}:\n\toriginal representation: {} rows\tactual representation: {} rows".format(
                a_class.class_name, a_class.rows.shape[-1], mask.shape[0]))
    logging.info("Original dataset: {} rows\tActual dataset: {} rows".format(dataset.shape[-1], new_dataset.shape[-1]))
    return new_dataset
