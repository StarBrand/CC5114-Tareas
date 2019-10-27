"""test_null_node.py: Unit testing of NullNode class"""

from unittest import main
from genetic_programming.ast.nodes import Node, NullNode
from test_genetic_programming import NodeTest


class TesterNode(Node):
    """TesterNode for unit testing replace_node()"""

    def __init__(self):
        super().__init__(NullNode().function, 1)
        self.arguments.append(None)

    def evaluate(self) -> object:
        """
        Evaluate nodes
        """
        return self.function()


class NullNodeTest(NodeTest):

    def setUp(self) -> None:
        """Sets up unittest"""
        self.first_node = TesterNode()
        self.second_node = NullNode()

    def test_evaluate(self):
        self.assertEqual(self.first_node.evaluate(), self.second_node.evaluate(), "Different results")
        self.assertIsNone(self.first_node.evaluate(), "First not None")
        self.assertIsNone(self.second_node.evaluate(), "Second not None")

    def test_equal(self):
        self.assertEqual(self.first_node.function, self.second_node.function, "Did not inheritance function")

    def test_replace_node(self):
        self.std_test_replace_node(0)


if __name__ == '__main__':
    main()
