from perceptron import GatePerceptron


class PerceptronAnd(GatePerceptron):

    def __init__(self):
        super(PerceptronAnd, self).__init__("and", 2, 2, -3)
