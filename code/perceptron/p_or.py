"""p_or.py: PerceptronOr class"""
from perceptron import GatePerceptron


class PerceptronOr(GatePerceptron):
    """GatePerceptron that simulated 'or' logical gate, for academic purpose"""

    def __init__(self):
        super(PerceptronOr, self).__init__("or", 3, 3, -2)
