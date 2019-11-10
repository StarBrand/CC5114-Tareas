"""test_div_node.py: Unit testing of DivNode"""

from random import seed, uniform
from unittest import main
from genetic_programming.ast.nodes import TerminalNode, AddNode, MultNode, MaxNode, DivNode
from test_genetic_programming import BinaryNodeTest

EPSILON = 1e-10


class DivNodeTest(BinaryNodeTest):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        seed(2)
        values = [uniform(1, 100) for _ in range(9)]
        self.first_node = AddNode(
            DivNode(
                TerminalNode(values[0]),
                TerminalNode(values[1])
            ), MultNode(
                MaxNode(
                    TerminalNode(values[2]), DivNode(
                        TerminalNode(values[3]), TerminalNode(values[4])
                    )
                ), TerminalNode(values[5])
            )
        )
        self.second_node = MultNode(
            TerminalNode(values[6]), MaxNode(
                TerminalNode(values[7]), DivNode(
                    TerminalNode(values[8]), TerminalNode(0)
                )
            )
        )
        expected1 = (values[0] / values[1]) + (max(values[2], values[3] / values[4]) * (values[5]))
        expected2 = None
        self.values = values
        self.expected = expected1, expected2

    def std_test_evaluate_float(self, expected: (float, float)):
        """
        Test evaluate, when result is float (and DivNode is used)

        :param expected: A tuple with values expected, but second values is going to raise an Exception
        :return: Test evaluate()
        """
        if expected[0] is None:
            self.assertRaises(ZeroDivisionError, self.first_node.evaluate)
        else:
            self.assertGreaterEqual(EPSILON, abs(expected[0] - self.first_node.evaluate()),
                                    "Wrong evaluate first nodes")
        if expected[1] is None:
            self.assertRaises(ZeroDivisionError, self.second_node.evaluate)
        else:
            self.assertGreaterEqual(EPSILON, abs(expected[1] - self.second_node.evaluate()),
                                    "Wrong evaluate second nodes")

    def test_replace_advanced(self):
        self.second_node.arguments[1].arguments[1].replace_node(self.first_node, 1)
        expected2 = (self.values[6]) * (max(self.values[7], self.values[8] / self.expected[0]))
        self.std_test_evaluate_float((self.expected[0], expected2))


if __name__ == '__main__':
    main()
