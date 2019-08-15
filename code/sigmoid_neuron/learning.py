from learning_perceptron import LearningPerceptron
from sigmoid_neuron import SigmoidNeuron


class LearningNeuron(LearningPerceptron):

    def __init__(self, lr: float, name: str):
        super(LearningNeuron, self).__init__(lr, name)
        w = self.get_weights()
        self.perceptron = SigmoidNeuron(name, w[0], w[1], w[2])
