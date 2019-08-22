from perceptron import GatePerceptron


class PerceptronNand(GatePerceptron):

    def __init__(self):
        super(PerceptronNand, self).__init__("nand", -2, -2, 3)
