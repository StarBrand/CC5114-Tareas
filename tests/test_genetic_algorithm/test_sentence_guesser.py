"""test_sentence_guesser.py: unittest of SentenceGuesser"""
from test_genetic_algorithm import IndividualTest
from unittest import main
from random import seed
from copy import deepcopy
from genetic_algorithm.individuals import SentenceGuesser

SENTENCE = "We typically think of databases, queues, caches, etc. as being very different categories of tools."
LENGTH = len(SENTENCE)


class SentenceGuesserTest(IndividualTest):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        self.individual = SentenceGuesser(0.03, SENTENCE)
        self.stable_one = SentenceGuesser(0.0, SENTENCE)

    def test_constructor(self):
        self.std_test_constructor(LENGTH, LENGTH)

    def test_generate_individual(self):
        self.std_test_generate_individual(LENGTH, LENGTH)

    def test_crossover(self):
        seed(10)
        first_new_one = self.individual.generate_individual()
        first_expected_child = self.individual.chromosome[0: 46] + first_new_one.chromosome[46: LENGTH]
        """mutations..."""
        first_expected_child[26] = "u"
        """end mutations"""
        second_new_one = self.stable_one.generate_individual()
        second_expected_child = self.stable_one.chromosome[0: 55] + second_new_one.chromosome[55: LENGTH]
        self.std_test_crossover(first_expected_child, second_expected_child, first_new_one, second_new_one)

    def test_get_allele(self):
        self.std_test_get_allele("2")

    def test_mutate(self):
        prev = deepcopy(self.individual)
        self.individual.mutate()
        self.assertNotEqual(prev, self.individual)

    def test_fitness(self):
        short_sentence = ["W", "e", " ", "t", "y", "p", "i", "c", "a",
                          "l", "l", "y", " ", "t", "h", "i", "n", "k"]
        self.individual.chromosome = short_sentence
        self.assertEqual(len(short_sentence), self.individual.fitness(), "Wrong fitness")


if __name__ == '__main__':
    main()
