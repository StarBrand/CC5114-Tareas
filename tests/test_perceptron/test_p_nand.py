"""test_p_nand.py: unittest of PerceptronNand"""
import unittest
from perceptron import PerceptronNand


class NandTest(unittest.TestCase):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
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
