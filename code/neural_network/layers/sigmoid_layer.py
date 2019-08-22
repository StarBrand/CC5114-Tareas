from neural_network.layers import NeuronLayer
from utils.math_functions import sigmoid


class SigmoidLayer(NeuronLayer):

    def __init__(self, input_size: int, output_size: int):
        super(SigmoidLayer, self).__init__(input_size, output_size, sigmoid)
