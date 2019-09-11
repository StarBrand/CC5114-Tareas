"""perceptron.py: Perceptron Class"""
from random import gauss


class Perceptron(object):
    """Perceptron: basic idea behind Neurons and Layers"""

    def __init__(self, name: str, input_size: int, w: [float] or None = None, b: float or None = None):
        if w is not None and len(w) != input_size:
            raise ValueError("Number of arguments do not match number of weights")
        self.name = name
        if w is None:
            self.w = []
            for _ in range(input_size):
                self.w.append(gauss(0, 1))
        else:
            self.w = w
        if b is None:
            self.b = 0.0
        else:
            self.b = b

    def out(self, x: [float]) -> float:
        """
        Output, predicted value

        :param x: Input
        :return: Prediction
        """
        if len(x) != len(self.w):
            raise ValueError("Number of input do not match declared number of input")
        return ((sum([w * i for w, i in zip(self.w, x)]) + self.b) > 0) * 1.0
