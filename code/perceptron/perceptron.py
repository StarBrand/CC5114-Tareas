class Perceptron(object):

    def __init__(self, name: str, w1: float, w2: float, b: float):
        self.name = name
        self.w1 = w1
        self.w2 = w2
        self.b = b

    def output(self, x1: float, x2: float):
        return self.w1*x1 + self.w2*x2 + self.b > 0
