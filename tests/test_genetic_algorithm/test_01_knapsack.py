"""test_01_knapsack.py: Unittest of Knapsack class"""

from unittest import main
from random import seed
from genetic_algorithm.individuals import Knapsack01
from test_genetic_algorithm import UnboundKnapsackTest

EPSILON = 1e-10


class Knapsack01Test(UnboundKnapsackTest):

    def setUp(self) -> None:
        """
        Sets up unit test
        """
        self.chromosome_size = 5
        self.individual = Knapsack01(0.3)
        self.stable_one = Knapsack01(0.0)

    def test_crossover(self):
        seed(10)
        first_one = self.individual.generate_individual()
        first_expected = self.individual.chromosome[0: 0] + first_one.chromosome[0: self.chromosome_size]
        """mutate"""
        first_expected[3] = 1
        """"""
        second_one = self.stable_one.generate_individual()
        second_expected = self.stable_one.chromosome[0: 3] + second_one.chromosome[3: self.chromosome_size]
        self.std_test_crossover(first_expected, second_expected, first_one, second_one)

    def test_get_allele(self):
        self.std_test_get_allele("box3")

    def test_fitness(self):
        self.expected_individuals()
        capacities = -5, 0.0
        values = 19, 0.0
        self.std_test_fitness(capacities, values)

    def test_comparing(self):
        self.expected_individuals()
        self.std_test_greater_than(self.stable_one, self.individual, 0)
        self.std_test_greater_than(self.stable_one, self.individual, 2)

    def expected_individuals(self):
        """
        Generate individual with known performance knapsack
        """
        self.individual.chromosome = [1, 1, 1, 1, 1]
        self.stable_one.chromosome = [0, 0, 0, 0, 0]
        self.individual.fitness()
        self.stable_one.fitness()


if __name__ == '__main__':
    main()
