from unittest import TestCase, main
from neural_network.utils import Line, split_set


class FunctionTest(TestCase):

    def setUp(self) -> None:
        a_line = Line((1, 1), (0, 0), (-1, 1), (-1, 1))
        self.train_set = a_line.training_set(1000)

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


if __name__ == '__main__':
    main()