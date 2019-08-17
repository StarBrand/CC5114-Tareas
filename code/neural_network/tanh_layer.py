from neural_network import NeuronLayer
from neural_network.utils import tanh


class TanhLayer(NeuronLayer):

    def __init__(self, input_size: int, output_size: int):
        super(TanhLayer, self).__init__(input_size, output_size, tanh)
