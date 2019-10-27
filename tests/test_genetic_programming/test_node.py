"""test_node.py: Unittest of class Node"""

from unittest import TestCase, main

EPSILON = 1e-10


class NodeTest(TestCase):
    
    def setUp(self) -> None:
        """
        Sets up unittest
        """
        self.first_node = None
        self.second_node = None

    def std_test_evaluate_float(self, expected: (float, float)):
        """
        Test evaluate, when result is float

        :param expected: A tuple with values expected
        :return: Test evaluate()
        """
        self.assertGreaterEqual(EPSILON, abs(expected[0] - self.first_node.evaluate()), "Wrong evaluate first nodes")
        self.assertGreaterEqual(EPSILON, abs(expected[1] - self.second_node.evaluate()), "Wrong evaluate second nodes")

    def std_test_evaluate_bool(self, expected: (bool, bool)):
        """
        Test evaluate, when result is boolean values

        :param expected: A tuple with values expected
        :return: Test evaluate()
        """
        self.assertEqual(expected[0], self.first_node.evaluate(), "Wrong evaluate first nodes")
        self.assertEqual(expected[1], self.second_node.evaluate(), "Wrong evaluate second nodes")

    def std_test_replace_node(self, position: int):
        """
        Test replace nodes for another

        :param position: Position to be replaced
        :return: Test replace_node()
        """
        self.assertNotEqual(self.first_node.arguments[position], self.second_node, "Nodes are the same")
        self.first_node.replace_node(self.second_node, position)
        self.assertEqual(self.first_node.arguments[position], self.second_node, "Nodes are not the same")


if __name__ == '__main__':
    main()
