from perceptron import Perceptron


class PerceptronOr(Perceptron):

    def __init__(self):
        super(PerceptronOr, self).__init__("or", 3, 3, -2)
