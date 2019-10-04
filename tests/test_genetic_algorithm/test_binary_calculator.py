"""test_binary_calculator.py: unittest of BinaryCalculator"""

from test_genetic_algorithm import IndividualTest
from unittest import main
from random import seed
from genetic_algorithm.individuals import BinaryCalculator

NUMBER_1 = 8
NUMBER_2 = 12
BITS = 4


class BinaryCalculatorTest(IndividualTest):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        self.individual = BinaryCalculator(0.3, NUMBER_1, BITS)
        self.stable_one = BinaryCalculator(0, NUMBER_2, BITS)

    def test_constructor(self):
        self.std_test_constructor(BITS, BITS)

    def test_generate_individual(self):
        self.std_test_generate_individual(BITS, BITS)

    def test_crossover(self):
        seed(10)
        first_new_one = self.individual.generate_individual()
        first_expected_child = self.individual.chromosome[0: 0] + first_new_one.chromosome[0: BITS]
        first_expected_child[0] = 0
        first_expected_child[1] = 1
        second_new_one = self.stable_one.generate_individual()
        second_expected_child = self.stable_one.chromosome[0: 2] + second_new_one.chromosome[2: BITS]
        self.std_test_crossover(first_expected_child, second_expected_child, first_new_one, second_new_one)

    def test_get_allele(self):
        self.std_test_get_allele("2")

    def test_fitness(self):
        self.individual.chromosome = [False, True, True, True]
        self.stable_one.chromosome = [False, True, True, True]
        self.assertEqual(7.0 - NUMBER_1, self.individual.fitness(), "Wrong fitness")
        self.assertEqual(7.0 - NUMBER_2, self.stable_one.fitness(), "Wrong fitness")


if __name__ == '__main__':
    main()
