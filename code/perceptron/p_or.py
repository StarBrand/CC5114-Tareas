from perceptron import GatePerceptron


class PerceptronOr(GatePerceptron):

    def __init__(self):
        super(PerceptronOr, self).__init__("or", 3, 3, -2)
