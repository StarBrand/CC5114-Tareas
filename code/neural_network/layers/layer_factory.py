"""layer_factory.py: LayerFactory Class"""

import logging
from neural_network.layers import NeuronLayer, SigmoidLayer, TanhLayer, PerceptronLayer
from utils.math_functions import derivative


class LayerFactory(object):
    """Layer Factory, as factory pattern"""

    @staticmethod
    def create_layer(parameter: str or callable, input_size: int, output_size: int) -> NeuronLayer:
        """
        Create layer with activation function given, as string or function itself
        If function not registered, layer is not going to have transverse derivative
        This could raise an Exception unless transverse derivative is given after initialization

        :param parameter: Activate function as string or function itself
        :param input_size: Size of input
        :param output_size: Size of output (aka number of neurons)
        :return: A concrete NeuronLayer
        """
        if type(parameter) == str:
            return LayerFactory._from_str(parameter, input_size, output_size)
        else:
            return LayerFactory._from_func(parameter, input_size, output_size)

    @staticmethod
    def _from_str(parameter: str, input_size: int, output_size: int) -> NeuronLayer:
        if parameter == "sigmoid":
            return SigmoidLayer(input_size, output_size)
        elif parameter == "tanh":
            return TanhLayer(input_size, output_size)
        elif parameter == "perceptron" or parameter == "step":
            return PerceptronLayer(input_size, output_size)
        else:
            raise KeyError("No neuron layer registered with that name")

    @staticmethod
    def _from_func(func: callable, input_size: int, output_size: int) -> NeuronLayer:
        if func not in derivative.keys():
            logging.warning("No derivative registered for that function, "
                            "this is going to raise an exception in back propagation, "
                            "to avoid this, define a function in the respective layer on "
                            "method transitive_derivative")
        return NeuronLayer(input_size, output_size, func)
