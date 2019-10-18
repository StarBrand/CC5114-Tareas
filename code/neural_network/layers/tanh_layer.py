"""tanh_layer: TanhLayer class"""
from neural_network.layers import NeuronLayer
from useful.math_functions import tanh


class TanhLayer(NeuronLayer):
    """Layer with tanh activation function"""

    def __init__(self, input_size: int, output_size: int):
        super().__init__(input_size, output_size, tanh)
