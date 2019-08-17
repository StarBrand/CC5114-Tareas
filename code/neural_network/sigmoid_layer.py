from neural_network import NeuronLayer
from neural_network.utils import sigmoid


class SigmoidLayer(NeuronLayer):

    def __init__(self, input_size: int, output_size: int):
        super(SigmoidLayer, self).__init__(input_size, output_size, sigmoid)
