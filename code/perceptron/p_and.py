from perceptron import Perceptron


class PerceptronAnd(Perceptron):

    def __init__(self):
        super().__init__("and", 2, 2, -3)
