"""p_and.py: PerceptronAnd Class"""
from perceptron import GatePerceptron


class PerceptronAnd(GatePerceptron):
    """GatePerceptron that simulated 'and' logical gate, for academic purpose"""

    def __init__(self):
        super(PerceptronAnd, self).__init__("and", 2, 2, -3)
