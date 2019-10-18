"""confusion_matrix.py: confusion matrix and related methods"""
import numpy as np


def confusion_matrix(prediction: np.ndarray, labels: np.ndarray) -> np.ndarray:
    """
    Confusion matrix

    :param prediction: Prediction given from Neural Network
    :param labels: Expected result
    :return: Confusion matrix (shape: #class, #class)
    """
    if prediction.ndim == 1:
        output = np.array([prediction, 1 - prediction])
    else:
        output = prediction.copy()
    if labels.ndim == 1:
        expected = np.array([labels, 1 - labels])
    else:
        expected = labels.copy()
    if prediction.shape != labels.shape:
        raise ValueError("Predictions and labels do not match dimensions")
    n = output.shape[0]
    m = output.shape[1]
    matrix = np.zeros((n, n))
    for i in range(m):
        matrix[output[(..., i)].argmax()][expected[(..., i)].argmax()] += 1
    return matrix


def accuracy(matrix: np.ndarray) -> float:
    """
    Calculate accuracy of prediction

    :param matrix: Confusion matrix calculated
    :return: Accuracy
    """
    return matrix.diagonal().sum() / matrix.sum()


def precision(matrix: np.ndarray) -> np.ndarray:
    """
    Calculate precision of prediction

    :param matrix: Confusion matrix
    :return: Precision for every class
    """
    return np.divide(matrix.diagonal(), matrix.sum(axis=1))


def recall(matrix: np.ndarray) -> np.ndarray:
    """
    Calculate recall of prediction

    :param matrix: Confusion matrix
    :return: Recall for every class
    """
    return np.divide(matrix.diagonal(), matrix.sum(axis=0))


def f1_score(matrix: np.ndarray) -> np.ndarray:
    """
    F1-score of prediction

    :param matrix: Confusion matrix
    :return: F1-score for class
    """
    a = precision(matrix)
    b = recall(matrix)
    return 2 * np.divide(np.multiply(a, b), a + b)
