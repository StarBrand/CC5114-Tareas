"""test_standard_trainer.py: unittest of StandardTrainer"""
import logging
from unittest import TestCase, main
from neural_network import NeuralNetwork
from useful.results import StandardTrainer, Trainer
from useful.patterns import Circle

SIZE = 10000
EPOCHS = 100
TRAIN_SIZE = 0.7
VARIABLES = 2
CLASSES = 1
EPSILON = 1e-10


class StandardTrainerTest(TestCase):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        dataset = Circle(10, (0, 0), (-50, 50), (-50, 50)).training_set(SIZE)
        self.dataset_shape = dataset.shape
        self.train_set = dataset[0:-1]
        self.labels = dataset[-1].reshape(1, -1)
        self.trainer = StandardTrainer(self.train_set, self.labels, TRAIN_SIZE)
        self.network = NeuralNetwork(VARIABLES, [6, 5], CLASSES, ["tanh", "tanh", "sigmoid"], 0.5)

    @staticmethod
    def test_exceptions():
        test = False
        try:
            Trainer()
        except TypeError as e:
            logging.warning(e.__str__())
            test = True
        assert test

    def test_init(self):
        assert self.trainer.train_set.shape == (VARIABLES, int(SIZE * TRAIN_SIZE))
        assert self.trainer.train_labels.shape == (CLASSES, int(SIZE * TRAIN_SIZE))
        assert self.trainer.test_set.shape == (VARIABLES, int(SIZE * (1 - TRAIN_SIZE)))
        assert self.trainer.test_labels.shape == (CLASSES, int(SIZE * (1 - TRAIN_SIZE)))

    def test_train(self):
        original_layers = []
        for layer in self.network.layers:
            w = layer.w.copy()
            b = layer.b.copy()
            original_layers.append((w, b))
        trained_network, metrics = self.trainer.train(self.network, epochs=EPOCHS)
        assert len(metrics[0]) == len(metrics[1])
        for index, layer in enumerate(self.network.layers):
            assert (layer.w == original_layers[index][0]).all()
            assert (layer.b == original_layers[index][1]).all()
        for index, layer in enumerate(self.network.layers):
            assert (layer.w != trained_network.layers[index].w).any()
            assert layer.w.shape == trained_network.layers[index].w.shape
            assert (layer.b != trained_network.layers[index].b).any()
            assert layer.b.shape == trained_network.layers[index].b.shape

    def test_evaluate(self):
        expected = self.network.feed_forward(self.trainer.test_set)
        actual = self.trainer.evaluate(self.network)
        assert (expected - actual < EPSILON).all()

    def test_get_labels(self):
        labels = self.trainer.get_labels()
        assert labels.shape == (CLASSES, int(SIZE * (1 - TRAIN_SIZE)))


if __name__ == '__main__':
    main()
