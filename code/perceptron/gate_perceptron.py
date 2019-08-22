from perceptron import Perceptron


class GatePerceptron(Perceptron):

    def __init__(self, name: str, w1: float, w2: float, b: float):
        super(GatePerceptron, self).__init__(name, 2, [w1, w2], b)
        self.w1 = self.w[0]
        self.w2 = self.w[1]

    def output(self, x1: float, x2: float) -> bool:
        return super(GatePerceptron, self).out([x1, x2]) > 0.5
