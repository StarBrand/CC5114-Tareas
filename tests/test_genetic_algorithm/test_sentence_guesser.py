"""test_sentence_guesser.py: unittest of SentenceGuesser"""
from unittest import TestCase, main
from random import seed
from copy import deepcopy
from genetic_algorithm import SentenceGuesser

WORD = "We typically think of databases, queues, caches, etc. as being very different categories of tools."
LENGTH = len(WORD)


class SentenceGuesserTest(TestCase):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        self.individual = SentenceGuesser(0.3, WORD)

    def test_constructor(self):
        self.assertEqual(LENGTH, len(self.individual), "Length mismatch")
        self.assertEqual(LENGTH, len(self.individual.chromosome), "Chromosome mismatch")
        self.assertEqual(LENGTH, len(self.individual.genes), "Genes mismatch")

    def test_generate_individual(self):
        new_one = self.individual.generate_individual()
        self.assertEqual(LENGTH, len(new_one), "Length mismatch")
        self.assertEqual(LENGTH, len(new_one.chromosome), "Chromosome mismatch")
        self.assertEqual(LENGTH, len(new_one.genes), "Genes mismatch")

    def test_crossover(self):
        seed(10)
        new_one = self.individual.generate_individual()
        new_one.mutation_rate = 0.0
        self.individual.mutation_rate = 0.0
        child = self.individual.crossover(new_one)
        expected_child = self.individual.chromosome[0: 4] + new_one.chromosome[4: LENGTH]
        print(expected_child)
        print(child.chromosome)
        self.assertEqual(expected_child, child.chromosome, "Wrong Child")

    def test_get_allele(self):
        expected = self.individual.chromosome[2]
        actual = self.individual.get_allele("2")
        self.assertEqual(expected, actual, "Wrong allele")

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
