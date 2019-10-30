"""test_ast.py: Unittest AST class"""

from copy import deepcopy
from unittest import main
from genetic_algorithm.individuals import Individual
from genetic_programming.ast.nodes import Node, NullNode
from test_genetic_algorithm import IndividualTest
from genetic_programming.ast import AST

EPSILON = 1e-10


class TesterAST(AST):
    """
    Tester of AST, just unit test purpose
    """
    def __init__(self, mutation_rate: float):
        root = self.generate_tree(0, 0)
        super().__init__([], [], 0, mutation_rate, root)

    def fitness(self) -> float:
        """
        Fitness (unittest)

        :return: Zero
        """
        self.my_fitness = 0.0
        return self.my_fitness

    def generate_tree(self, depth: int, prob_terminal: float) -> Node:
        """
        Generates tree (unittest)

        :param depth:
        :param prob_terminal:
        :return: NullNode
        """
        return NullNode()

    def generate_individual(self) -> Individual:
        """
        Generates individual

        """
        return TesterAST(self.mutation_rate)

    def crossover(self, partner: AST) -> AST:
        """
        Null crossover

        :param partner: An AST
        :return: TesterAST
        """
        return TesterAST(self.mutation_rate)


class ASTTest(IndividualTest):

    def setUp(self) -> None:
        """
        Sets up unit testing
        """
        self.individual = TesterAST(0.3)
        self.stable_one = TesterAST(0.0)

    def _std_test_generate_individual(self, length_individual: int, individual: AST):
        new_one = individual.generate_individual()
        self.assertEqual(individual.depth, new_one.depth, "Depth mismatch")
        self.assertEqual(individual.prob_terminal, new_one.prob_terminal, "Probability of terminal node mismatch")
        self.assertNotEqual(individual, new_one, "Equal son, unexpected")

    def test_generate_tree(self):
        self._std_test_generate_tree([0.0])

    def _std_test_generate_tree(self, depth_to_test: [int]):
        actual = TesterAST(0.0)
        for depth in depth_to_test:
            actual.root = self.individual.generate_tree(depth, 0.3)
            self.assertGreaterEqual(depth, actual._calculate_depth(), "Too deep node (individual)")
            actual.root = self.stable_one.generate_tree(depth, 0.3)
            self.assertGreaterEqual(depth, actual._calculate_depth(), "Too deep node (stable_one)")

    def test_crossover(self):
        """mutate"""
        """ Cannot mutate"""
        """"""
        self.std_test_crossover(NullNode(), NullNode(),
                                TesterAST(0.0), TesterAST(0.3))

    def std_test_crossover(self, first_expected_child: Node, second_expected_child: Node,
                           first_new_one: AST, second_new_one: AST):
        """
        Standard test crossover

        :param first_expected_child: First expected child
        :param second_expected_child: Second expected child
        :param first_new_one: First new individual
        :param second_new_one: Second new individual
        """
        self._std_test_crossover(first_expected_child, self.individual, first_new_one)
        self._std_test_crossover(second_expected_child, self.stable_one, second_new_one)

    def _std_test_crossover(self, expected_child: Node, individual: AST, new_one: AST):
        child = individual.crossover(new_one)
        self.assertEqual(expected_child, child.root, "Wrong Child")

    def std_test_replace_on_position(self, position_individual: (int, ...), other_individual: Node,
                                     expected_individual: Node, position_stable_one: (int, ...),
                                     other_stable_one: Node, expected_stable_one: Node):
        """
        Standard test replace on position

        :param:
        """
        actual = self.individual.replace_on_position(position_individual, other_individual)
        self.assertEqual(expected_individual, actual, "Wrong test on individual")
        actual = self.stable_one.replace_on_position(position_stable_one, other_stable_one)
        self.assertEqual(expected_stable_one, actual, "Wrong test on stable one")

    def test_copy(self):
        expected = deepcopy(self.individual)
        copy = self.individual.copy()
        self.individual = None
        self.assertEqual(expected, copy, "Individual copied")
        expected = deepcopy(self.stable_one)
        copy = self.stable_one.copy()
        self.stable_one = None
        self.assertEqual(expected, copy, "Stable one copied")


if __name__ == '__main__':
    main()
