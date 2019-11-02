"""test_chiffres_yes_no_variant.py: Test ChiffresYesNoVariant Class"""

from unittest import main
from random import seed
from genetic_programming import ChiffresYesNoVariant
from genetic_programming.ast.nodes import AddNode, TerminalNode, YesNoNode
from test_genetic_programming import ASTTest

TO_GUESS = 10
VALUES = [1, 2, 3, 4, 5, 6]
""" Calculating floor of log2 """
DEPTH_WHOLE = 3
DEPTH_PART = 2
EPSILON = 1e-10


class ChiffresVariantTest(ASTTest):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        seed(10)
        self.individual = ChiffresYesNoVariant(TO_GUESS, VALUES, 0.3)
        self.stable_one = ChiffresYesNoVariant(TO_GUESS, VALUES[0: 4], 0.0)
        self.expected_values = (0, 0)

    def _std_test_generate_tree(self, depth_to_test: [int]):
        for depth in depth_to_test:
            self.individual.root = self.individual.generate_tree(depth, 0.3)
            self.assertGreaterEqual(DEPTH_WHOLE, self.individual._calculate_depth(), "Too deep node (individual)")
            self.stable_one.root = self.stable_one.generate_tree(depth, 0.3)
            self.assertGreaterEqual(DEPTH_PART, self.stable_one._calculate_depth(), "Too deep node (stable_one)")

    def test_generate_individual(self):
        self._std_test_generate_individual(DEPTH_WHOLE, self.individual)
        self._std_test_generate_individual(DEPTH_PART, self.stable_one)

    def test_crossover(self):
        first_one = self.individual.generate_individual()
        first_expected = self.individual.replace_on_position((0, 0, 0, 0),
                                                             first_one.get_node((0, 0, 0, 0)))
        """mutate"""
        graft = YesNoNode(0, False)
        reference = first_expected.arguments[1]
        reference.replace_node(graft, 1)
        """"""
        second_one = self.stable_one.generate_individual()
        second_expected = self.stable_one.replace_on_position((0, 0),
                                                              second_one.get_node((0, 0)))
        self.std_test_crossover(first_expected, second_expected, first_one, second_one)

    def test_fitness(self):
        self.expected_individuals()
        self.assertGreaterEqual(EPSILON, abs(self.expected_values[0] - TO_GUESS + self.individual.my_fitness),
                                "Wrong fitness individual")
        self.assertGreaterEqual(EPSILON, abs(self.expected_values[1] - TO_GUESS + self.stable_one.my_fitness),
                                "Wrong fitness stable_one")

    def expected_individuals(self):
        """
        Generate individual with known performance knapsack
        """
        self.individual.root = AddNode(
            AddNode(
                AddNode(TerminalNode(1), TerminalNode(2)),
                AddNode(TerminalNode(3), TerminalNode(4))
            ),
            AddNode(TerminalNode(5), TerminalNode(6))
        )
        self.stable_one.root = AddNode(
            AddNode(TerminalNode(1), TerminalNode(2)),
            AddNode(TerminalNode(3), TerminalNode(4))
        )
        self.individual.fitness()
        self.stable_one.fitness()
        self.expected_values = (21, 10)


if __name__ == '__main__':
    main()
