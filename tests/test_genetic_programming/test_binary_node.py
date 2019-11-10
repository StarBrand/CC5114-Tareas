"""test_binary_node.py: Unit testing of BinaryNode"""

from random import seed, uniform
from unittest import main
from genetic_programming.ast.nodes import TerminalNode, AddNode, SubNode, MultNode, MaxNode
from test_genetic_programming import NodeTest

EPSILON = 1e-10


class BinaryNodeTest(NodeTest):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        seed(2)
        values = [uniform(0, 100) for _ in range(10)]
        self.first_node = AddNode(
            SubNode(
                TerminalNode(values[0]),
                TerminalNode(values[1])
            ), MultNode(
                MaxNode(
                    TerminalNode(values[2]), AddNode(
                        TerminalNode(values[3]), TerminalNode(values[4])
                    )
                ), TerminalNode(values[5])
            )
        )
        self.second_node = MultNode(
            TerminalNode(values[6]), MaxNode(
                TerminalNode(values[7]), AddNode(
                    TerminalNode(values[8]), TerminalNode(values[9])
                )
            )
        )
        self.values = values
        expected1 = (self.values[0] - self.values[1]) + (
                max(self.values[2], self.values[3] + self.values[4]) * (self.values[5]))
        expected2 = (self.values[6] * max(
            self.values[7], self.values[8] + self.values[9]))
        self.expected = expected1, expected2

    def test_evaluate(self):
        self.std_test_evaluate_float(self.expected)

    def test_replace_node(self):
        self.std_test_replace_node(0)
        if self.expected[1] is None:
            expected1 = None
        else:
            expected1 = self.expected[0] - (self.values[0] - self.values[1]) + self.expected[1]
        self.std_test_evaluate_float((expected1, self.expected[1]))

    def test_replace_advanced(self):
        self.first_node.arguments[0].replace_node(self.second_node, 1)
        expected1 = self.expected[0] + self.values[1] - self.expected[1]
        self.std_test_evaluate_float((expected1, self.expected[1]))


if __name__ == '__main__':
    main()
