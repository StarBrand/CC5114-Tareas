"""equation_guesser.py: EquationGuesser class"""
from copy import deepcopy
from math import log, e
from unittest import main
from random import seed
from genetic_programming import EquationGuesser
from genetic_programming.ast.nodes import AddNode, SubNode, MultNode, DivNode
from genetic_programming.ast.nodes import TerminalNode, TerminalVariable
from test_genetic_programming import ASTTest

TO_GUESS = log
VALUES = list(range(1, 10))
DEPTH = 6  # Depth of node
PROB = 0.03  # Probability of an internal node, became a terminal node
VALUES_FOR_FITNESS = list(range(1, 10))
EPSILON = 1e-10


class EquationGuesserTest(ASTTest):

    def setUp(self) -> None:
        """
        Sets up EquationGuesserTest unit testing
        """
        seed(2)
        self.individual = EquationGuesser(TO_GUESS, VALUES, float, PROB, DEPTH, 0.1)
        self.stable_one = EquationGuesser(TO_GUESS, VALUES, float, PROB, DEPTH, 0.0)
        self.individual_fitness = 0
        self.stable_one_fitness = 0

    def test_generate_individual(self):
        self._std_test_generate_individual(DEPTH, self.individual)
        self._std_test_generate_individual(DEPTH, self.stable_one)

    def test_generate_tree(self):
        self._std_test_generate_tree(list(range(0, 10)))

    def test_crossover(self):
        seed(2)
        first_one = self.individual.generate_individual()
        first_expected = self.individual.replace_on_position((0, 1, 1, 1, 0, 0, 0),
                                                             first_one.get_node((0, 0, 0, 0, 0, 1, 1)))
        """mutate"""
        graft = MultNode(TerminalNode(4), TerminalNode(9))
        reference = first_expected.arguments[1].arguments[0].arguments[0].arguments[1]
        reference.replace_node(graft, 1)
        """"""
        second_one = self.stable_one.generate_individual()
        second_expected = self.stable_one.replace_on_position((0, 0, 1, 1, 0, 1, 1),
                                                              second_one.get_node((0, 0, 0, 1, 0, 1, 0)))
        self.std_test_crossover(first_expected, second_expected, first_one, second_one)

    def test_fitness(self):
        self.expected_individuals()
        expected_individual = list()
        expected_stable_one = list()
        for index, value in enumerate(VALUES_FOR_FITNESS):
            expected_individual.append(abs(TO_GUESS(value) - self.individual_fitness[index]))
            expected_stable_one.append(abs(TO_GUESS(value) - self.stable_one_fitness[index]))
        expected_individual = - sum(expected_individual) / len(expected_individual)
        expected_stable_one = - sum(expected_stable_one) / len(expected_stable_one)
        self.assertGreaterEqual(EPSILON, abs(expected_individual - self.individual.my_fitness),
                                "Wrong fitness individual")
        self.assertGreaterEqual(EPSILON, abs(expected_stable_one - self.stable_one.my_fitness),
                                "Wrong fitness stable_one")
        self.assertRaises(KeyError, self.stable_one.fitness)
        self.assertRaises(KeyError, self.individual.fitness)
        self.assertRaises(ZeroDivisionError, self.stable_one.fitness, values=[])
        self.assertRaises(ZeroDivisionError, self.individual.fitness, values=[])

    def expected_individuals(self):
        """
        Generate individual with known performance knapsack
        """
        self.individual.root = MultNode(
            SubNode(
                AddNode(TerminalNode(e), TerminalVariable("x", float)),
                MultNode(TerminalNode(1), TerminalNode(2))
            ),
            AddNode(TerminalNode(e), TerminalNode(2))
        )
        self.stable_one.root = MultNode(
            TerminalNode(e), TerminalVariable("x", float)
        )
        self.individual.fitness(values=VALUES_FOR_FITNESS)
        self.stable_one.fitness(values=VALUES_FOR_FITNESS)
        expected_individual = list()
        expected_stable_one = list()
        for x in VALUES_FOR_FITNESS:
            expected_individual.append(((e + x) - (1 * 2)) * (e + 2))
            expected_stable_one.append(e * x)
        self.individual_fitness = expected_individual
        self.stable_one_fitness = expected_stable_one

    def test_div_zero_behaviour(self):
        from genetic_programming.equation_guesser import _mean_diff

        def _hyperbola(x: float) -> float:
            return 1 / x

        evaluate_at = list(range(-10, 10 + 1))

        equation_guesser = EquationGuesser(_hyperbola, [AddNode], float, 0, 0, 0, True)
        equation_guesser.root = MultNode(
            AddNode(TerminalNode(3), TerminalVariable("x", float)),
            TerminalVariable("x", float)
        )
        self.assertGreaterEqual(0, equation_guesser.fitness(values=evaluate_at), "Random Equation")
        equation_guesser.root = DivNode(TerminalNode(1), TerminalVariable("x", float))
        self.assertGreaterEqual(EPSILON, abs(0 - equation_guesser.fitness(values=evaluate_at)), "Same equation")
        equation_guesser.root = DivNode(TerminalVariable("x", float), TerminalNode(0))
        self.assertEqual(-float("Inf"), equation_guesser.fitness(values=evaluate_at), "Wrong equation")


if __name__ == '__main__':
    main()
