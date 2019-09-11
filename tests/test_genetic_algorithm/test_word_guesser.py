"""test_word_guesser.py: unittest of WordGuesser"""
from unittest import TestCase, main
from random import seed
from genetic_algorithm import WordGuesser

WORD_1 = "algorithm"
WORD_2 = "cat"
LENGTH_1 = len(WORD_1)
LENGTH_2 = len(WORD_2)


class WordGuesserTest(TestCase):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        self.individual = WordGuesser(0.3, WORD_1)
        self.stable_one = WordGuesser(0, WORD_2)

    def test_constructor(self):
        self.assertEqual(LENGTH_1, len(self.individual), "Length mismatch")
        self.assertEqual(LENGTH_1, len(self.individual.chromosome), "Chromosome mismatch")
        self.assertEqual(LENGTH_1, len(self.individual.genes), "Genes mismatch")
        self.assertEqual(LENGTH_2, len(self.stable_one), "Length mismatch")
        self.assertEqual(LENGTH_2, len(self.stable_one.chromosome), "Chromosome mismatch")
        self.assertEqual(LENGTH_2, len(self.stable_one.genes), "Genes mismatch")

    def test_generate_individual(self):
        new_one = self.individual.generate_individual()
        self.assertEqual(LENGTH_1, len(new_one), "Length mismatch")
        self.assertEqual(LENGTH_1, len(new_one.chromosome), "Chromosome mismatch")
        self.assertEqual(LENGTH_1, len(new_one.genes), "Genes mismatch")
        new_one = self.stable_one.generate_individual()
        self.assertEqual(LENGTH_2, len(new_one), "Length mismatch")
        self.assertEqual(LENGTH_2, len(new_one.chromosome), "Chromosome mismatch")
        self.assertEqual(LENGTH_2, len(new_one.genes), "Genes mismatch")

    def test_crossover(self):
        seed(10)
        new_one = self.individual.generate_individual()
        child = self.individual.crossover(new_one)
        expected_child = self.individual.chromosome[0: 3] + new_one.chromosome[3: LENGTH_1]
        expected_child[4] = "l"
        expected_child[6] = "v"
        expected_child[7] = "f"
        self.assertEqual(expected_child, child.chromosome, "Wrong Child")
        new_one = self.stable_one.generate_individual()
        child = self.stable_one.crossover(new_one)
        expected_child = self.stable_one.chromosome
        self.assertEqual(expected_child, child.chromosome, "Wrong Child")

    def test_get_allele(self):
        expected = self.individual.chromosome[2]
        actual = self.individual.get_allele("2")
        self.assertEqual(expected, actual, "Wrong allele")
        expected = self.stable_one.chromosome[2]
        actual = self.stable_one.get_allele("2")
        self.assertEqual(expected, actual, "Wrong allele")

    def test_fitness(self):
        self.individual.chromosome = ["a", "n", "o", "o", "r", "y", "b", "p", "n"]
        self.stable_one.chromosome = ["c", "o", "w"]
        self.assertEqual(3, self.individual.fitness(), "Wrong fitness")
        self.assertEqual(1, self.stable_one.fitness(), "Wrong fitness")


if __name__ == '__main__':
    main()
