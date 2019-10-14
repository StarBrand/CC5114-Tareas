"""p_nand.py: PerceptronNand class"""
from perceptron import GatePerceptron


class PerceptronNand(GatePerceptron):
    """GatePerceptron that simulated "nand' (not and) logical gate, for academic purpose"""

    def __init__(self):
        super().__init__("nand", -2, -2, 3)
