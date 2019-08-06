from perceptron import Perceptron, PerceptronNand, PerceptronAnd


class PerceptronSum(Perceptron):

    def __init__(self):
        super().__init__("or", 3, 3, -2)
        self.nand = PerceptronNand()
        self.p_and = PerceptronAnd()

    def output(self, x1: int, x2: int):
        return self.sum(x1, x2), self.carry(x1, x2)

    def sum(self, x1: int, x2: int):
        return self.nand.output(x1, x2)

    def carry(self, x1: int, x2: int):
        return self.p_and.output(x1, x2)
