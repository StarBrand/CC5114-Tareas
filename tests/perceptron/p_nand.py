import unittest
from code.perceptron import PerceptronNand


class AndTest(unittest.TestCase):

    def setUp(self) -> None:
        self.perceptron_nand = PerceptronNand()
        self.x1 = [0, 1]
        self.x2 = [0, 1]

    def test_output(self):
        actual = self.perceptron_nand.output(self.x1[0], self.x2[0])
        assert actual
        actual = self.perceptron_nand.output(self.x1[0], self.x2[1])
        assert actual
        actual = self.perceptron_nand.output(self.x1[1], self.x2[0])
        assert actual
        actual = self.perceptron_nand.output(self.x1[1], self.x2[1])
        assert not actual


if __name__ == "__main__":
    unittest.main()
