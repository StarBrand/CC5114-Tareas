"""test_unbound_knapsack.py: Unittest of UnboundKnapsack class"""

from unittest import main
from random import seed
from genetic_algorithm.individuals import UnboundKnapsack
from useful.simulations import BOX1, BOX2, BOX3, NullBox, BOX5
from test_genetic_algorithm import MultiIndividualTest

EPSILON = 1e-10


class UnboundKnapsackTest(MultiIndividualTest):

    def setUp(self) -> None:
        """
        Sets up unit test
        """
        self.chromosome_size = 15
        self.individual = UnboundKnapsack(0.3)
        self.stable_one = UnboundKnapsack(0.0)

    def test_constructor(self):
        self.std_test_constructor(self.chromosome_size, self.chromosome_size)

    def test_generate_individual(self):
        self.std_test_generate_individual(self.chromosome_size, self.chromosome_size)

    def test_crossover(self):
        seed(10)
        first_one = self.individual.generate_individual()
        first_expected = self.individual.chromosome[0: 7] + first_one.chromosome[7: self.chromosome_size]
        """mutate"""
        first_expected[0] = BOX3
        first_expected[6] = BOX5
        first_expected[11] = BOX1
        """"""
        second_one = self.stable_one.generate_individual()
        second_expected = self.stable_one.chromosome[0: 13] + second_one.chromosome[13: self.chromosome_size]
        self.std_test_crossover(first_expected, second_expected, first_one, second_one)

    def test_get_allele(self):
        self.std_test_get_allele("item3")

    def test_fitness(self):
        self.expected_individuals()
        capacity1 = 0.0
        capacity2 = - 21
        value1 = 8
        value2 = 12
        self.assertGreaterEqual(EPSILON, abs(self.individual.multi_fitness[0] - capacity1),
                                "Wrong capacity calculated individual")
        self.assertGreaterEqual(EPSILON, abs(self.individual.multi_fitness[1] - value1),
                                "Wrong value calculated individual")
        self.assertGreaterEqual(EPSILON, abs(self.stable_one.multi_fitness[0] - capacity2),
                                "Wrong capacity calculated stable one")
        self.assertGreaterEqual(EPSILON, abs(self.stable_one.multi_fitness[1] - value2),
                                "Wrong value calculated stable one")
        self.assertGreaterEqual(EPSILON, abs(self.individual.my_fitness - capacity1), "Wrong fitness individual")
        self.assertGreaterEqual(EPSILON, abs(self.stable_one.my_fitness - capacity2), "Wrong fitness stable one")

    def test_comparing(self):
        self.expected_individuals()
        self.std_test_greater_than(self.individual, self.stable_one, 0)
        self.std_test_greater_than(self.individual, self.stable_one, 2)

    def expected_individuals(self):
        """
        Generate individual with known performance knapsack
        """
        self.individual.chromosome = [BOX1, BOX2, BOX3] + [NullBox] * 12
        self.stable_one.chromosome = [BOX1] * 3 + [NullBox] * 12
        self.individual.fitness()
        self.stable_one.fitness()


if __name__ == '__main__':
    main()
