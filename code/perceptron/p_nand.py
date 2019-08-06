from perceptron import Perceptron


class PerceptronNand(Perceptron):

    def __init__(self):
        super().__init__("nand", -2, -2, 3)
