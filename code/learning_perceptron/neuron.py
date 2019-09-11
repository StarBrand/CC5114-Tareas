"""neuron.py: A generalization of the Learning Perceptron for any activation function"""
from learning_perceptron import LearningPerceptron


class Neuron(LearningPerceptron):
    """Neuron Class: A learning perceptron with a given activation function"""

    def __init__(self, name: str, input_size: int,
                 activation_function: callable,
                 learning_rate: float,
                 w: [float] or None = None,
                 b: float or None = None):
        super(Neuron, self).__init__(name, input_size, learning_rate)
        if w is not None:
            if len(w) != input_size:
                raise ValueError("Number of arguments do not match number of weights")
            self.perceptron.w = w
        if b is not None:
            self.perceptron.b = b
        self.activation_function = activation_function

    def feed(self, x_input: [float]) -> float:
        """
        Gives probability of probability of belong to a class

        :param x_input: Input (aka attributes)
        :return: Probability
        """
        if len(x_input) != len(self.perceptron.w):
            raise ValueError("Number of input do not match declared number of input")
        ans = sum([w * x for w, x in zip(self.perceptron.w, x_input)]) + self.perceptron.b
        return self.activation_function(ans)
