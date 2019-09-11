"""test_null_layer.py: unittest of NullLayer"""
from unittest import TestCase, main
import numpy as np
from neural_network.layers import NullLayer


class NullLayerTest(TestCase):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        self.layer = NullLayer()

    def test_get(self):
        assert self.layer is not None
        assert self.layer.w is None
        assert self.layer.b is None
        assert self.layer.delta is None
        assert self.layer.output is None

    def test_out(self):
        assert self.layer.out(np.array([])).shape == (0, )

    def test_feed(self):
        assert self.layer.feed(np.array([])).shape == (0,)

    def test_derivative(self):
        assert self.layer.transverse_derivative(np.array([])).shape == (0,)

    def test_propagate(self):
        self.layer.feed(np.array([]))
        self.layer.propagate(np.array([]))
        assert self.layer.w is None
        assert self.layer.b is None
        assert self.layer.delta is None
        assert self.layer.output is None
        self.layer.propagate(np.array([]), np.array([]), np.array([]))
        assert self.layer.w is None
        assert self.layer.b is None
        assert self.layer.delta is None
        assert self.layer.output is None

    def test_update_weights(self):
        self.layer.feed(np.array([]))
        self.layer.propagate(np.array([]))
        self.layer.update_weights(np.array([]), 0.1)
        assert self.layer.w is None
        assert self.layer.b is None
        assert self.layer.delta is None
        assert self.layer.output is None
        self.layer.propagate(np.array([]), np.array([]), np.array([]))
        self.layer.update_weights(np.array([]), 0.1)
        assert self.layer.w is None
        assert self.layer.b is None
        assert self.layer.delta is None
        assert self.layer.output is None


if __name__ == '__main__':
    main()
