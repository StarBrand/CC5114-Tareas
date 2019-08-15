from math import exp
from perceptron import Perceptron


class SigmoidNeuron(Perceptron):

    def __init__(self, name: str, w1: float, w2: float, b: float):
        super(SigmoidNeuron, self).__init__(name, w1, w2, b)
        return

    def output(self, x1: float, x2: float) -> bool:
        z = self.w1 * x1 + self.w2 * x2 + self.b
        try:
            return self._sigmoid(z) < 0.5
        except OverflowError:
            return z < 0

    @staticmethod
    def _sigmoid(z: float) -> float:
        return 1 / (1 + exp(z))
