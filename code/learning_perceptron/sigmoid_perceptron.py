import numpy as np
from perceptron import Perceptron
from learning_perceptron import LearningPerceptron
from utils.math_functions import sigmoid


class SigmoidNeuron(LearningPerceptron):

    class SigmoidPerceptron(Perceptron):

        def __init__(self, input_size: int):
            super(SigmoidNeuron.SigmoidPerceptron, self).__init__("sigmoid", input_size)

        def z_out(self, x: [float]) -> float:
            if len(x) != len(self.w):
                raise ValueError("Number of input do not match declared number of input")
            return sum([w * i for w, i in zip(self.w, x)]) + self.b

        def out(self, x: [float]) -> float:
            return float(sigmoid(np.array(self.z_out(x))))

    def __init__(self, input_size: int, lr: float):
        super(SigmoidNeuron, self).__init__("sigmoid neuron", input_size, lr)
        self.perceptron = self.SigmoidPerceptron(input_size)
