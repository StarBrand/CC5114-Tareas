"""test_null_individual.py: unnitest for NullIndividual class"""

import string
from copy import deepcopy
from random import choice
from unittest import TestCase, main
from genetic_algorithm import NullIndividual

RANDOM_TESTS = 3
EPSILON = 1e-10


class NullIndividualTest(TestCase):

    def setUp(self) -> None:
        """Sets up unittest"""
        self.individual = NullIndividual()

    def test_null_behaviour(self):
        self.assertIsInstance(self.individual.generate_individual(), NullIndividual, "Wrong child")
        prev = deepcopy(self.individual)
        self.individual.mutate()
        self.assertEqual(prev, self.individual, "Something change")
        child = self.individual.crossover(prev)
        self.assertEqual(self.individual, child, "Child change")
        for _ in range(RANDOM_TESTS):
            self.assertLessEqual(abs(self.individual.fitness() - 0), EPSILON, "Wrong fitness")
            self.assertIsNone(self.individual.get_allele(choice(string.ascii_lowercase)), "An allele (null)")
            self.assertLessEqual(abs(prev.fitness() - 0), EPSILON, "Wrong fitness (prev mutation)")
            self.assertIsNone(prev.get_allele(choice(string.ascii_lowercase)), "An allele (prev mutation)")
            self.assertLessEqual(abs(child.fitness() - 0), EPSILON, "Wrong fitness (child)")
            self.assertIsNone(child.get_allele(choice(string.ascii_lowercase)), "An allele (child)")


if __name__ == '__main__':
    main()
