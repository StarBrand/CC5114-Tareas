from perceptron import Perceptron
from random import uniform


class LearningPerceptron(object):

    def __init__(self, lr: float, name: str):
        self.lr = lr
        self.perceptron = Perceptron(name,
                                     uniform(-2.0, 2.0),
                                     uniform(-2.0, 2.0),
                                     uniform(-2.0, 2.0))
        self.name = self.perceptron.name
        self.number_of_training = 0

    def train(self, train_set: [(float, float, bool)]) -> int:
        training = 0
        for x1, x2, result in train_set:
            desire_output = result
            real_output = self.perceptron.output(x1, x2)
            diff = (1.0 * desire_output) - (1.0 * real_output)
            self.perceptron.w1 += self.lr * x1 * diff
            self.perceptron.w2 += self.lr * x2 * diff
            self.perceptron.b += self.lr * diff
            training += 1
        self.number_of_training += training
        return training

    def output(self, x1: float, x2: float) -> bool:
        return self.perceptron.output(x1, x2)

    def get_weights(self) -> (float, float, float):
        return self.perceptron.w1, self.perceptron.w2, self.perceptron.b
