import unittest
from perceptron import PerceptronSum


class SumTest(unittest.TestCase):

    def setUp(self) -> None:
        self.perceptron_sum = PerceptronSum()
        self.x1 = [0, 1]
        self.x2 = [0, 1]

    def test_output(self):
        actual = self.perceptron_sum.output(self.x1[0], self.x2[0])
        assert actual[0] and not actual[1]
        actual = self.perceptron_sum.output(self.x1[0], self.x2[1])
        assert actual[0] and not actual[1]
        actual = self.perceptron_sum.output(self.x1[1], self.x2[0])
        assert actual[0] and not actual[1]
        actual = self.perceptron_sum.output(self.x1[1], self.x2[1])
        assert not actual[0] and actual[1]


if __name__ == "__main__":
    unittest.main()
