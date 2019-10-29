"""test_boolean_node.py: Unittest of boolean nodes"""

from copy import deepcopy
from unittest import main
from random import seed, uniform
from genetic_programming.ast.nodes import GreaterNode, LesserNode, EqualNode
from genetic_programming.ast.nodes import NotNode, TerminalNode, AndNode, OrNode
from test_genetic_programming import NodeTest


class BooleanNodeTest(NodeTest):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        seed(2)
        values = [uniform(0, 100) for _ in range(10)]
        self.first_node = OrNode(
            AndNode(
                GreaterNode(TerminalNode(values[0]), TerminalNode(values[1])),
                LesserNode(TerminalNode(values[2]), TerminalNode(values[3]))
            ), AndNode(
                GreaterNode(TerminalNode(values[4]), TerminalNode(values[5])),
                LesserNode(TerminalNode(values[6]), TerminalNode(values[7]))
            )
        )
        self.second_node = NotNode(
            EqualNode(
                TerminalNode(values[8]), TerminalNode(values[9])
            )
        )
        expected1 = (values[0] > values[1] and
                     values[2] < values[3]) or (values[4] > values[5] and
                                                values[6] < values[7])
        expected2 = values[8] != values[9]
        self.values = values
        self.expected = (expected1, expected2)

    def test_evaluate_bool(self):
        self.std_test_evaluate_bool(self.expected)

    def test_replace_node(self):
        self.std_test_replace_node(0)
        values = deepcopy(self.values)
        expected1 = (values[8] != values[9]) or (values[4] > values[5] and
                                                 values[6] < values[7])
        self.std_test_evaluate_bool((expected1, self.expected[1]))

    def test_replace_advanced(self):
        self.first_node.arguments[0].replace_node(self.second_node, 1)
        values = deepcopy(self.values)
        expected1 = (values[0] > values[1] and
                     values[8] != values[9]) or (values[4] > values[5] and
                                                 values[6] < values[7])
        self.std_test_evaluate_float((expected1, self.expected[1]))

    def test_exceptions(self):
        self.assertRaises(ValueError, NotNode, TerminalNode(9))
        self.assertFalse(NotNode(TerminalNode(True)).evaluate())
        self.assertRaises(ValueError, AndNode, TerminalNode(8), TerminalNode(7))
        self.assertFalse(AndNode(TerminalNode(True), TerminalNode(False)).evaluate())
        self.assertRaises(ValueError, OrNode, TerminalNode(8), TerminalNode(7))
        self.assertFalse(OrNode(TerminalNode(False), TerminalNode(False)).evaluate())


if __name__ == '__main__':
    main()
