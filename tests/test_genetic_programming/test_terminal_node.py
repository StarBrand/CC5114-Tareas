"""test_terminal_node.py: Unit testing of Terminal Node"""

from unittest import main
from genetic_programming.ast.nodes import TerminalNode
from test_genetic_programming.test_null_node import TesterNode
from test_genetic_programming import NodeTest


class TerminalNodeTest(NodeTest):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        self.first_node = TerminalNode(10)
        self.second_node = TerminalNode(-10)

    def test_evaluate(self):
        self.std_test_evaluate_float((10, -10))

    def test_replace_node(self):
        self.first_node = TesterNode()
        self.std_test_replace_node(0)


if __name__ == '__main__':
    main()
