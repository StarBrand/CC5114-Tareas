"""test_p_or.py: unittest of PerceptronOr"""
import unittest
from perceptron import PerceptronOr


class OrTest(unittest.TestCase):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        self.perceptron_or = PerceptronOr()
        self.x1 = [0, 1]
        self.x2 = [0, 1]

    def test_output(self):
        actual = self.perceptron_or.output(self.x1[0], self.x2[0])
        assert not actual
        actual = self.perceptron_or.output(self.x1[0], self.x2[1])
        assert actual
        actual = self.perceptron_or.output(self.x1[1], self.x2[0])
        assert actual
        actual = self.perceptron_or.output(self.x1[1], self.x2[1])
        assert actual


if __name__ == "__main__":
    unittest.main()
