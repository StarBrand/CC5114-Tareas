"""test_yes_no_node.py: Unit testing of Yes No Node"""

from random import seed, uniform
from unittest import main
from genetic_programming.ast.nodes import AddNode, SubNode, MultNode, MaxNode, YesNoNode
from test_genetic_programming import NodeTest

EPSILON = 1e-10


class YesNoNodeTest(NodeTest):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        seed(2)
        values = [uniform(0, 100) for _ in range(20)]
        self.first_node = AddNode(
            SubNode(
                YesNoNode(values[0], True),
                YesNoNode(values[1], False)
            ), MultNode(
                MaxNode(
                    YesNoNode(values[2], True), AddNode(
                        YesNoNode(values[3], False), YesNoNode(values[4], True)
                    )
                ), YesNoNode(values[5], False)
            )
        )
        self.second_node = MultNode(
            YesNoNode(values[6], False), MaxNode(
                YesNoNode(values[7], True), AddNode(
                    YesNoNode(values[8], False), YesNoNode(values[9], True)
                )
            )
        )
        self.values = values
        expected1 = (self.values[0]) + (max(self.values[2], self.values[4]))
        expected2 = max(self.values[7], self.values[9])
        self.expected = expected1, expected2

    def test_evaluate(self):
        self.std_test_evaluate_float(self.expected)

    def test_replace_node(self):
        self.std_test_replace_node(0)
        expected1 = self.expected[0] - self.values[0] + self.expected[1]
        self.std_test_evaluate_float((expected1, self.expected[1]))

    def test_replace_advanced(self):
        self.first_node.arguments[0].replace_node(self.second_node, 1)
        expected1 = self.expected[0] - self.expected[1]
        self.std_test_evaluate_float((expected1, self.expected[1]))


if __name__ == '__main__':
    main()
