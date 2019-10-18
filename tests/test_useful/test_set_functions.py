"""test_set_functions.py: unittest of set methods"""
from unittest import TestCase, main
import numpy as np
from os import path
from useful.patterns import Line
from useful.preprocess_dataset import split_set, import_data


class FunctionTest(TestCase):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        a_line = Line((1, 1), (0, 0), (-1, 1), (-1, 1))
        self.train_set = a_line.training_set(1000)
        self.file_path = path.dirname(path.abspath(__file__))

    def test_split_set(self):
        train_set, test_set = split_set(self.train_set, 0.7)
        assert train_set.shape[-1] == 700
        assert test_set.shape[-1] == 300
        assert train_set.shape[0:-1] == train_set.shape[0:-1]
        train_set, test_set = split_set(self.train_set, 0.7, 0.2)
        assert train_set.shape[-1] == 700
        assert test_set.shape[-1] == 200
        assert train_set.shape[0:-1] == train_set.shape[0:-1]
        exception = False
        try:
            split_set(self.train_set, 10, 10)
        except ValueError:
            exception = True
        assert exception
        exception = False
        try:
            split_set(self.train_set, 1.1)
        except ValueError:
            exception = True
        assert exception
        exception = False
        try:
            split_set(self.train_set, 0.6, 0.7)
        except ValueError:
            exception = True
        assert exception

    def test_import_data(self):
        dataset_path = path.abspath("{}/../../data/iris.data".format(self.file_path))
        dataset_iris = import_data(dataset_path)
        assert type(dataset_iris) == np.ndarray
        assert dataset_iris.shape[0] == 5


if __name__ == '__main__':
    main()
