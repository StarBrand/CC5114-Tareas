"""test_variable: Unit testing with variable allowed"""

from copy import deepcopy
from random import seed, uniform
from unittest import main
from genetic_programming.ast.nodes import TerminalVariable, AndNode, OrNode, NotNode, GreaterNode, LesserNode
from genetic_programming.ast.nodes import AddNode, SubNode, MaxNode, MultNode, TerminalNode
from test_genetic_programming import BooleanNodeTest
from test_genetic_programming import BinaryNodeTest

EPSILON = 1e-10


class BooleanVariableNodeTest(BooleanNodeTest):

    def setUp(self) -> None:
        """
        Alter nodes to test with variables
        """
        seed(2)
        values = [uniform(0, 100) for _ in range(4)]
        self.first_node = OrNode(
            AndNode(
                GreaterNode(TerminalNode(values[0]), TerminalNode(values[1])),
                TerminalVariable("x", bool)
            ), AndNode(
                TerminalVariable("y", bool),
                LesserNode(TerminalNode(values[2]), TerminalNode(values[3]))
            )
        )
        self.second_node = NotNode(
            TerminalVariable("y", bool)
        )
        expected1 = list()
        variables = [
            {"x": True, "y": True}, {"x": True, "y": False},
            {"x": False, "y": True}, {"x": False, "y": False}
        ]
        for variable in variables:
            expected1.append((values[0] > values[1] and
                              variable["x"]) or (variable["y"] and
                                                 values[2] < values[3]))
        expected2 = list()
        for variable in variables:
            expected2.append(not variable["y"])
        self.variables = {
            "x": [True, False],
            "y": [True, False]
        }
        self.values = values
        self.expected = (expected1, expected2)

    def std_test_evaluate_bool(self, expected: (bool, bool)):
        """
        Test evaluate, with variables

        :param expected: List of expected values
        :return: Test evaluate(variable_values: [dict])
        """
        actual_ones = self.first_node.evaluate(values=self.variables)
        for an_expected, actual in zip(expected[0], actual_ones):
            self.assertEqual(an_expected, actual, "Wrong evaluate first nodes")
        actual_ones = self.second_node.evaluate(values=self.variables)
        for an_expected, actual in zip(expected[1], actual_ones):
            self.assertEqual(an_expected, actual, "Wrong evaluate second nodes")

    def test_replace_node(self):
        self.std_test_replace_node(0)
        values = deepcopy(self.values)
        expected1 = list()
        variables = [
            {"x": True, "y": True}, {"x": True, "y": False},
            {"x": False, "y": True}, {"x": False, "y": False}
        ]
        for variable in variables:
            expected1.append((not variable["y"]) or (variable["y"] and
                                                     values[2] < values[3]))
        self.std_test_evaluate_bool((expected1, self.expected[1]))

    def test_replace_advanced(self):
        self.first_node.arguments[0].replace_node(self.second_node, 1)
        values = deepcopy(self.values)
        expected1 = list()
        variables = [
            {"x": True, "y": True}, {"x": True, "y": False},
            {"x": False, "y": True}, {"x": False, "y": False}
        ]
        for variable in variables:
            expected1.append((values[0] > values[1] and
                              not variable["y"]) or (variable["y"] and
                                                     values[2] < values[3]))
        self.std_test_evaluate_bool((expected1, self.expected[1]))


class BinaryVariableNodeTest(BinaryNodeTest):

    def setUp(self) -> None:
        """
        Alter nodes to test with variables
        """
        seed(2)
        values = [uniform(0, 100) for _ in range(7)]
        self.first_node = AddNode(
            SubNode(
                TerminalNode(values[0]),
                TerminalVariable("x", float)
            ), MultNode(
                MaxNode(
                    TerminalNode(values[1]), AddNode(
                        TerminalNode(values[2]), TerminalNode(values[3])
                    )
                ), TerminalVariable("y", float)
            )
        )
        self.second_node = MultNode(
            TerminalNode(values[4]), MaxNode(
                TerminalNode(values[5]), AddNode(
                    TerminalNode(values[6]), TerminalVariable("y", float)
                )
            )
        )
        expected1 = list()
        self.variables = {
            "x": list(range(-100, 101, 50)),
            "y": list(range(-100, 101, 50))
        }
        self.values = values
        variables = list()
        for x in self.variables["x"]:
            for y in self.variables["y"]:
                variables.append({"x": x,
                                 "y": y})
        for variable in variables:
            expected1.append((self.values[0] - variable["x"]) + (
                    max(self.values[1], self.values[2] + self.values[3]) * variable["y"]))
        expected2 = list()
        for variable in variables:
            expected2.append(self.values[4] * max(
                self.values[5], self.values[6] + variable["y"]))
        self.values = values
        self.expected = (expected1, expected2)

    def std_test_evaluate_float(self, expected: (float, float)):
        """
        Test evaluate, with variables

        :param expected: List of expected values
        :return: Test evaluate(variable_values: [dict])
        """
        actual_ones = self.first_node.evaluate(values=self.variables)
        for an_expected, actual in zip(expected[0], actual_ones):
            self.assertGreaterEqual(EPSILON, abs(an_expected - actual), "Wrong evaluate first nodes")
        actual_ones = self.second_node.evaluate(values=self.variables)
        for an_expected, actual in zip(expected[1], actual_ones):
            self.assertGreaterEqual(EPSILON, abs(an_expected - actual), "Wrong evaluate second nodes")

    def test_replace_node(self):
        self.std_test_replace_node(0)
        expected1 = list()
        for index, an_expected in enumerate(self.expected[0]):
            expected1.append(an_expected - (self.values[0] - self.variables["x"][index // 5]) +
                             self.expected[1][index])
        self.std_test_evaluate_float((expected1, self.expected[1]))

    def test_replace_advanced(self):
        self.first_node.arguments[0].replace_node(self.second_node, 1)
        expected1 = list()
        for index, an_expected in enumerate(self.expected[0]):
            expected1.append(an_expected + self.variables["x"][index // 5] - self.expected[1][index])
        self.std_test_evaluate_float((expected1, self.expected[1]))

    def test_terminal_node(self):
        a = 0.0
        node = TerminalNode(a)
        actual = node.evaluate(values={"x": [1, 2, 3], "y": [4, 5]})
        self.assertEqual(6, len(actual), "Length of terminal node with values")
        self.assertEqual([a]*6, actual, "Terminal node miscalculated")
        actual = node.evaluate(values={"x": [1, 2, 3]})
        self.assertEqual(3, len(actual), "Length of terminal node with values")
        self.assertEqual([a] * 3, actual, "Terminal node miscalculated")
        actual = node.evaluate(values={})
        self.assertEqual(0, len(actual), "Length of terminal node with values")
        self.assertEqual([a] * 0, actual, "Terminal node miscalculated")


if __name__ == '__main__':
    main()
