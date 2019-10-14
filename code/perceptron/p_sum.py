"""p_sum.py: PerceptronSum class"""
from perceptron import GatePerceptron, PerceptronNand, PerceptronAnd


class PerceptronSum(GatePerceptron):
    """GatePerceptron that simulated 'sum' of two int using logical gates, for academic purpose"""

    def __init__(self):
        super().__init__("or", 3, 3, -2)
        self.nand = PerceptronNand()
        self.p_and = PerceptronAnd()

    def output(self, x1: int, x2: int) -> (int, int):
        """
        Sum expressed as binary

        :param x1: Boolean as integer (0 -> False, 1 -> True)
        :param x2: Boolean as integer (0 -> False, 1 -> True)
        :return: Sum as binary
        """
        return self.sum(x1, x2), self.carry(x1, x2)

    def sum(self, x1: int, x2: int) -> int:
        """
        Sum of x1 and x2, less important bit

        :param x1: Boolean as integer (0 -> False, 1 -> True)
        :param x2: Boolean as integer (0 -> False, 1 -> True)
        :return: Less important bit
        """
        return self.nand.output(x1, x2)

    def carry(self, x1: int, x2: int) -> int:
        """
        Carry (most important bit)

        :param x1:  Boolean as integer (0 -> False, 1 -> True)
        :param x2:  Boolean as integer (0 -> False, 1 -> True)
        :return: Most important bit
        """
        return self.p_and.output(x1, x2)
