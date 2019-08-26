import numpy as np
from learning_perceptron import LearningPerceptron
from neural_network import NeuralNetwork


def do_prediction(a_perceptron: LearningPerceptron, a_set: np.ndarray) -> [float]:
    ans = []
    for x, y, _ in a_set.T.tolist():
        ans.append(a_perceptron.feed([x, y]))
    return ans


def do_prediction_net(network: NeuralNetwork, a_set: np.ndarray) -> [float]:
    ans = []
    for x in a_set.T:
        ans.append(network.feed_forward(x[0:-1])[0][0])
    return ans
