"""test_word_guesser.py: unittest of WordGuesser"""
from test_genetic_algorithm import IndividualTest
from unittest import main
from random import seed
from genetic_algorithm.individuals import WordGuesser

WORD_1 = "algorithm"
WORD_2 = "cat"
LENGTH_1 = len(WORD_1)
LENGTH_2 = len(WORD_2)


class WordGuesserTest(IndividualTest):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        self.individual = WordGuesser(0.3, WORD_1)
        self.stable_one = WordGuesser(0, WORD_2)

    def test_constructor(self):
        self.std_test_constructor(LENGTH_1, LENGTH_2)

    def test_generate_individual(self):
        self.std_test_generate_individual(LENGTH_1, LENGTH_2)

    def test_crossover(self):
        seed(10)
        first_new_one = self.individual.generate_individual()
        first_expected_child = self.individual.chromosome[0: 0] + first_new_one.chromosome[0: LENGTH_1]
        """mutations"""
        first_expected_child[1] = "l"
        first_expected_child[3] = "v"
        first_expected_child[4] = "f"
        first_expected_child[7] = "y"
        """mutations"""
        second_new_one = self.stable_one.generate_individual()
        second_expected_child = self.stable_one.chromosome[0: LENGTH_2] + second_new_one.chromosome[LENGTH_2: LENGTH_2]
        self.std_test_crossover(first_expected_child, second_expected_child, first_new_one, second_new_one)

    def test_get_allele(self):
        self.std_test_get_allele("2")

    def test_fitness(self):
        self.individual.chromosome = ["a", "n", "o", "o", "r", "y", "b", "p", "n"]
        self.stable_one.chromosome = ["c", "o", "w"]
        self.assertEqual(3, self.individual.fitness(), "Wrong fitness")
        self.assertEqual(1, self.stable_one.fitness(), "Wrong fitness")


if __name__ == '__main__':
    main()
