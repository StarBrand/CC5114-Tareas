"""test:asbt.py: Unittest BinaryAST class"""
from copy import deepcopy
from random import seed
from unittest import main
from genetic_programming import BinaryAST
from genetic_programming.ast.nodes import AddNode, SubNode, MultNode, MaxNode, TerminalNode
from test_genetic_programming import ASTTest
from test_genetic_programming.binary_nodes_expected import individual, stable_one
from test_genetic_programming.binary_nodes_expected import expected_individual, expected_stable_one

EPSILON = 1e-10
TO_GUESS = 10


class BinaryASTTest(ASTTest):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        seed(10)
        self.individual = BinaryAST(TO_GUESS, 10, 0.03, 0.3)
        self.stable_one = BinaryAST(TO_GUESS, 10, 0.03, 0.0)

    def test_generate_individual(self):
        self._std_test_generate_individual(10, self.individual)
        self._std_test_generate_individual(10, self.stable_one)

    def test_generate_tree(self):
        self._std_test_generate_tree(list(range(0, 10)))

    def test_crossover(self):
        seed(10)
        first_one = self.individual.generate_individual()
        first_expected = self.individual.replace_on_position((0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0),
                                                             first_one.get_node((0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0)))
        """mutate"""
        graft = MultNode(
            MultNode(
                MultNode(TerminalNode(-79), TerminalNode(-13)),
                AddNode(TerminalNode(-72), TerminalNode(-72))
            ),
            AddNode(
                MultNode(TerminalNode(36), TerminalNode(-16)),
                MaxNode(TerminalNode(24), TerminalNode(-26))
            )
        )
        reference = first_expected.arguments[0].arguments[1].arguments[0].arguments[0].arguments[1].arguments[1]
        reference.replace_node(graft, 1)
        """"""
        second_one = self.stable_one.generate_individual()
        second_expected = self.stable_one.replace_on_position((0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0),
                                                              second_one.get_node((0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1)))
        self.std_test_crossover(first_expected, second_expected, first_one, second_one)

    def test_replace_on_position(self):
        expected1 = deepcopy(self.individual.root)
        expected2 = deepcopy(stable_one)
        expected1.arguments[0].arguments[1].arguments[0].replace_node(individual, 1)
        self.std_test_replace_on_position((0, 0, 1, 0, 1), individual, expected1,
                                          (0, ), stable_one, expected2)

    def test_fitness(self):
        self.expected_individuals()
        self.assertGreaterEqual(EPSILON, abs(expected_individual - TO_GUESS + self.individual.my_fitness),
                                "Wrong fitness individual")
        self.assertGreaterEqual(EPSILON, abs(expected_stable_one - TO_GUESS + self.stable_one.my_fitness),
                                "Wrong fitness stable_one")

    def expected_individuals(self):
        """
        Generate individual with known performance knapsack
        """
        self.individual.root = individual
        self.stable_one.root = stable_one
        self.individual.fitness()
        self.stable_one.fitness()

    def test_get_node(self):
        expected = self.individual.root.arguments[0].arguments[1]
        self.assertEqual(expected, self.individual.get_node((0, 0, 1)), "Wrong get deep node")
        expected = self.stable_one.root
        self.assertEqual(expected, self.stable_one.get_node((0, )), "Wrong get root")


if __name__ == '__main__':
    main()
