"""test_cross_validation.py: unittest KFoldTrainer"""
from unittest import TestCase, main
from neural_network import NeuralNetwork
from useful.results import KFoldTrainer
from useful.patterns import Circle

SIZE = 10000
EPOCHS = 100
VARIABLES = 2
CLASSES = 1
EPSILON = 1e-10
K = 10


class KFoldTest(TestCase):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        dataset = Circle(10, (0, 0), (-50, 50), (-50, 50)).training_set(SIZE)
        self.train_set = dataset[0:-1]
        self.labels = dataset[-1].reshape(1, -1)
        self.trainer = KFoldTrainer(K, 2, self.train_set, self.labels)
        self.network = NeuralNetwork(VARIABLES, [6, 5], CLASSES, ["tanh", "tanh", "sigmoid"], 0.5)

    def test_init(self):
        assert self.trainer.k == K
        assert self.trainer.i == 0

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
        self.trainer.i = 1
        expected = self.network.feed_forward(self.trainer.data.take(self.trainer.indexes[0][1], axis=-1))
        actual = self.trainer.evaluate(self.network)
        assert (expected - actual < EPSILON).all()

    def test_get_labels(self):
        self.trainer.i = 1
        labels = self.trainer.get_labels()
        assert labels.shape == (CLASSES, int(SIZE / K))

    def test_no_more_iterations(self):
        self.trainer.i = K
        _, metrics = self.trainer.train(self.network)
        assert len(metrics[0]) == 0
        assert len(metrics[1]) == 0
        self.trainer.i = K + 1
        output = self.trainer.evaluate(self.network)
        assert output.shape == (0, )
        labels = self.trainer.get_labels()
        assert labels.shape == (0, )


if __name__ == '__main__':
    main()
