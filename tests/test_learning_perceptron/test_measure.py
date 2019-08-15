from unittest import TestCase, main
from random import uniform
from learning_perceptron.utils import confusion_matrix, accuracy, precision, recall, f1_score, Line

FP = TP = FN = TN = 5
N = 20
POS = NEG = 10
T = F = 10


class MeasureTest(TestCase):

    def setUp(self) -> None:
        self.line = Line((1, 1), (0, 0), (-10, 10), (-10, 10))
        self.x1 = []
        self.x2 = []
        for i in range(5):
            self.x1.append(uniform(-10, 0))
            self.x2.append(uniform(-10, 0))
            self.x1.append(uniform(0, 10))
            self.x2.append(uniform(0, 10))
        self.y1 = []
        self.y2 = []
        for i in range(5):
            self.y1.append(uniform(0, 10))
            self.y2.append(uniform(0, 10))
            self.y1.append(uniform(-10, 0))
            self.y2.append(uniform(-10, 0))

    def test_confusion_matrix(self):
        fp, tp, fn, tn = confusion_matrix(self.line, self.x1, self.y1, self.x2, self.y2)
        assert fp == FP
        assert tp == TP
        assert fn == FN
        assert tn == TN

    @staticmethod
    def test_accuracy_measure():
        assert accuracy(FP, TP, FN, TN) == T/N
        actual_precision = precision(FP, TP)
        assert actual_precision == TP / POS
        actual_recall = recall(TP, FN)
        assert actual_recall == TP / (TP + FN)
        assert f1_score(FP, TP, FN) == 2 * (
                (actual_precision * actual_recall) / (actual_precision + actual_precision)
        )


if __name__ == "__main__":
    main()
