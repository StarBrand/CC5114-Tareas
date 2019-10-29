"""test_if_then_else_node.py: Unit testing of IfThenElseNode"""

from unittest import TestCase, main
from random import seed, uniform
from genetic_programming.ast.nodes import IfThenElseNode
from genetic_programming.ast.nodes import GreaterNode, TerminalNode

EPSILON = 1e-10


class IfThenElseTest(TestCase):

    def test_assertion(self):
        seed(2)
        values = [uniform(-100, 100) for _ in range(4)]
        if values[0] > values[1]:
            expected = values[2]
        else:
            expected = values[3]
        node = IfThenElseNode(
            GreaterNode(TerminalNode(values[0]), TerminalNode(values[1])),
            TerminalNode(values[2]), TerminalNode(values[3])
        )
        self.assertGreaterEqual(EPSILON, abs(expected - node.evaluate()), "Wrong evaluation")

    def test_replace_node(self):
        node = IfThenElseNode(TerminalNode(True), TerminalNode(1), TerminalNode(2))
        self.assertGreaterEqual(EPSILON, abs(1 - node.evaluate()), "Wrong calculated")
        node.replace_node(TerminalNode(3), 2)
        self.assertGreaterEqual(EPSILON, abs(1 - node.evaluate()), "Wrong calculated (replaced wrongly 'else')")
        node.replace_node(TerminalNode(3), 1)
        self.assertGreaterEqual(EPSILON, abs(3 - node.evaluate()), "Wrong calculated (replaced wrongly 'then')")
        node.replace_node(TerminalNode(4), 2)
        node.replace_node(TerminalNode(False), 0)
        self.assertGreaterEqual(EPSILON, abs(4 - node.evaluate()), "Wrong calculated (replaced wrongly 'if')")

    def test_exceptions(self):
        self.assertRaises(ValueError, IfThenElseNode, TerminalNode(1), TerminalNode(2), TerminalNode(3))
        node = IfThenElseNode(TerminalNode(True), TerminalNode(1), TerminalNode(2))
        self.assertRaises(ValueError, node.replace_node, TerminalNode(1), 0)


if __name__ == '__main__':
    main()
