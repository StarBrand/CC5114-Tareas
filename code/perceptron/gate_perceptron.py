"""gate_perceptron.py: GatePerceptron class"""
from perceptron import Perceptron


class GatePerceptron(Perceptron):
    """A Perceptron that simulate logical gates"""

    def __init__(self, name: str, w1: float, w2: float, b: float):
        super().__init__(name, 2, [w1, w2], b)
        self.w1 = self.w[0]
        self.w2 = self.w[1]

    def output(self, x1: float, x2: float) -> bool:
        """
        Prediction of simulated gate

        :param x1: Logical value as float, whether 0.0 (false) or 1.0 (true)
        :param x2: Logical value as float, whether 0.0 (false) or 1.0 (true)
        :return: Predicted output (True or False)
        """
        return super().out([x1, x2]) > 0.5
