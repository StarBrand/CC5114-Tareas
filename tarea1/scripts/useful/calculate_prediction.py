import numpy as np
from learning_perceptron import LearningPerceptron


def do_prediction(a_perceptron: LearningPerceptron, a_set: np.ndarray) -> [float]:
    ans = []
    for xx, yy, _ in a_set.T.tolist():
        ans.append(a_perceptron.feed([xx, yy]))
    return ans
