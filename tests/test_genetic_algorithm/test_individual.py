"""test_individual.py: unittest of Individual abstract class"""

from unittest import TestCase, main
from genetic_algorithm.individuals import Individual, NullIndividual


class IndividualTest(TestCase):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        self.individual = NullIndividual()
        self.stable_one = NullIndividual()

    def std_test_constructor(self, length_individual: int, length_stable: int):
        """
        Test constructor of Individual

        :param length_individual: Length of first individual (mutation_rate != 0)
        :param length_stable: Length of second one (stable one, mr = 0)
        """
        self._std_test_constructor(length_individual, self.individual)
        self._std_test_constructor(length_stable, self.stable_one)

    def _std_test_constructor(self, length_individual: int, individual: Individual):
        self.assertEqual(length_individual, len(individual), "Length mismatch")
        self.assertEqual(length_individual, len(individual.chromosome), "Chromosome mismatch")
        self.assertEqual(length_individual, len(individual.genes), "Genes mismatch")

    def std_test_generate_individual(self, length_individual: int, length_stable: int):
        """
        Test constructor generating individual

        :param length_individual: Length first individual
        :param length_stable: Length second individual
        """
        self._std_test_generate_individual(length_individual, self.individual)
        self._std_test_generate_individual(length_stable, self.stable_one)

    def _std_test_generate_individual(self, length_individual: int, individual: Individual):
        new_one = individual.generate_individual()
        self.assertEqual(length_individual, len(new_one), "Length mismatch")
        self.assertEqual(length_individual, len(new_one.chromosome), "Chromosome mismatch")
        self.assertEqual(length_individual, len(new_one.genes), "Genes mismatch")
        self.assertNotEqual(self.individual, new_one, "Equal son, unexpected")

    def std_test_crossover(self, first_expected_child: list, second_expected_child: list,
                           first_new_one: Individual, second_new_one: Individual):
        """
        Standard test crossover

        :param first_expected_child: First expected child
        :param second_expected_child: Second expected child
        :param first_new_one: First new individual
        :param second_new_one: Second new individual
        """
        self._std_test_crossover(first_expected_child, self.individual, first_new_one)
        self._std_test_crossover(second_expected_child, self.stable_one, second_new_one)

    def _std_test_crossover(self, expected_child: list, individual: Individual, new_one: Individual):
        child = individual.crossover(new_one)
        self.assertEqual(expected_child, child.chromosome, "Wrong Child")

    def std_test_get_allele(self, second_gen: str):
        """
        Standard get allele

        :param second_gen: Name of second gen
        """
        self._std_test_get_allele(self.individual, second_gen)
        self._std_test_get_allele(self.stable_one, second_gen)

    def _std_test_get_allele(self, individual: Individual, second_gen: str):
        expected = individual.chromosome[2]
        actual = individual.get_allele(second_gen)
        self.assertEqual(expected, actual, "Wrong allele")


if __name__ == '__main__':
    main()
