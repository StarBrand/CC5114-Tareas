"""learning.py: Learning Perceptron class"""

from perceptron import Perceptron


class LearningPerceptron(object):
    """Learning Perceptron: Compose of a Perceptron, train it and use it"""

    def __init__(self, name: str, input_size: int, lr: float):
        self.lr = lr
        self.perceptron = Perceptron(name, input_size)
        self.name = self.perceptron.name
        self.number_of_training = 0

    def train(self, x_input: [float], expected: float) -> int:
        """
        Train a perceptron

        :param x_input: An input to use for training
        :param expected: Expected value of x_input (aka label)
        :return: Number of epochs
        """
        real_output = self.perceptron.out(x_input)
        diff = expected - real_output
        for i, x in enumerate(x_input):
            self.perceptron.w[i] = self.perceptron.w[i] + self.lr * x_input[i] * diff
        self.perceptron.b += self.lr * diff
        self.number_of_training += 1
        return self.number_of_training

    def feed(self, x_input: [float]) -> float:
        """
        Feed the train with an input an give probability of belonging the class

        :param x_input: An input
        :return: Probability [0, 1]
        """
        return self.perceptron.out(x_input)

    def get_weights(self) -> ([float], float):
        """
        Get weights of the perceptron and the bias

        :return: Tuple of list of weight and bias value
        """
        return self.perceptron.w, self.perceptron.b
