"""test_oversample.py: unittest of oversample and undersample methods"""
import os
import numpy as np
from unittest import TestCase, main
from utils.preprocess_dataset import import_data, oversample, undersample

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
DATASET = os.path.join(FILE_PATH, "../../data/ecoli.data")
TO_SIZE_TEST = 100


class OversampleTest(TestCase):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        self.dataset = import_data(DATASET)
        self.classes = np.unique(self.dataset[-1])
        maximum = 0
        minimum = self.dataset.shape[-1]
        for a_class in self.classes:
            temp = (self.dataset[-1] == a_class).sum()
            maximum = max(maximum, temp)
            minimum = min(minimum, temp)
            del temp
        self.max_representation = maximum
        self.min_representation = minimum

    def test_oversample(self):
        actual = oversample(self.dataset)
        assert actual.shape[-1] == self.max_representation * 4
        for a_class in self.classes:
            assert (actual[-1] == a_class).sum() == self.max_representation

    def test_undersample(self):
        actual = undersample(self.dataset)
        assert actual.shape[-1] == self.min_representation * 4
        for a_class in self.classes:
            assert (actual[-1] == a_class).sum() == self.min_representation

    def test_fixed(self):
        actual1 = oversample(self.dataset, to_size=TO_SIZE_TEST)
        actual2 = undersample(self.dataset, to_size=TO_SIZE_TEST)
        assert actual1.shape[-1] == TO_SIZE_TEST * 4
        for a_class in self.classes:
            assert (actual1 == a_class).sum() == TO_SIZE_TEST
        assert actual2.shape[-1] == TO_SIZE_TEST * 4
        for a_class in self.classes:
            assert (actual2 == a_class).sum() == TO_SIZE_TEST


if __name__ == '__main__':
    main()
