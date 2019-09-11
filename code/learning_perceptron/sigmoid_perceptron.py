"""sigmoid_perceptron.py: A Learning Perceptron with sigmoid activation function"""

import numpy as np
from perceptron import Perceptron
from learning_perceptron import LearningPerceptron
from utils.math_functions import sigmoid


class SigmoidNeuron(LearningPerceptron):
    """Sigmoid Neuron Class, a kind of Learning Perceptron with sigmoid function"""

    class SigmoidPerceptron(Perceptron):
        """Sigmoid Perceptron, a kinf of perceptron with sigmoid function"""

        def __init__(self, input_size: int):
            super(SigmoidNeuron.SigmoidPerceptron, self).__init__("sigmoid", input_size)

        def z_out(self, x: [float]) -> float:
            """
            Output given a input (x), just linear function application

            :param x: Input
            :return: Output without activation function
            """
            if len(x) != len(self.w):
                raise ValueError("Number of input do not match declared number of input")
            return sum([w * i for w, i in zip(self.w, x)]) + self.b

        def out(self, x: [float]) -> float:
            """
            Output with activation function calculated

            :param x: Input
            :return: Output
            """
            return float(sigmoid(np.array(self.z_out(x))))

    def __init__(self, input_size: int, lr: float):
        super(SigmoidNeuron, self).__init__("sigmoid neuron", input_size, lr)
        self.perceptron = self.SigmoidPerceptron(input_size)
