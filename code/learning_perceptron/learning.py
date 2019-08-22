from perceptron import Perceptron


class LearningPerceptron(object):

    def __init__(self, name: str, input_size: int, lr: float):
        self.lr = lr
        self.perceptron = Perceptron(name, input_size)
        self.name = self.perceptron.name
        self.number_of_training = 0

    def train(self, x_input: [float], expected: float) -> int:
        real_output = self.perceptron.out(x_input)
        diff = expected - real_output
        for i, x in enumerate(x_input):
            self.perceptron.w[i] = self.perceptron.w[i] + self.lr * x_input[i] * diff
        self.perceptron.b += self.lr * diff
        self.number_of_training += 1
        return self.number_of_training

    def feed(self, x_input: [float]) -> float:
        return self.perceptron.out(x_input)

    def get_weights(self) -> ([float], float):
        return self.perceptron.w, self.perceptron.b
