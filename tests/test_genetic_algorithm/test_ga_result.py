"""test_ga_result.py: unittest of GAResult class"""

from unittest import TestCase, main
from genetic_algorithm import GAResult
from genetic_algorithm.individuals import NullIndividual, WordGuesser


class GAResultTest(TestCase):

    def setUp(self) -> None:
        """Sets up unittest"""
        self.result = GAResult()

    def test_not_ready(self):
        self.assertIsInstance(self.result.individual, NullIndividual, "An actual individual returned")
        self.assertFalse(self.result.found_solution, "Found solution without set")

    def test_not_exportable(self):
        self.assertRaises(RuntimeError, self.result.get_scores)
        self.assertRaises(RuntimeError, self.result.get_generations)
        self.assertRaises(RuntimeError, len, self.result)

    def test_not_available_to_register(self):
        self.result.ready_to_export(NullIndividual(), False)
        self.assertRaises(RuntimeError, self.result.register_score, 0.0)

    def test_normal_functionality(self):
        scores = [1.0, 3.0, 2.0]
        generations = [1, 10, 11]
        self.result.register_score(scores[0])
        self.result.register_score(scores[1], generation=generations[1])
        self.result.register_score(scores[2])
        self.result.ready_to_export(WordGuesser(0.0, "test"), True)
        self.assertIsInstance(self.result.individual, WordGuesser, "Wrong individual")
        self.assertEqual(scores, self.result.get_scores(), "Fail to register scores")
        self.assertEqual(generations, self.result.get_generations(), "Fail to register generation")
        self.assertEqual(len(scores), len(self.result), "Mismatch length of scores and results")
        self.assertEqual(len(generations), len(self.result), "Mismatch length of generations and results")

    def test_length_mismatch(self):
        scores = [1.0, 3.0, 2.0]
        generations = [1, 10]
        self.result._scores = scores
        self.result._generations = generations
        self.result._ready = True
        self.assertRaises(RuntimeError, len, self.result)
        scores = [1.0, 3.0]
        generations = [1, 10, 11]
        self.result._scores = scores
        self.result._generations = generations
        self.result._ready = True
        self.assertRaises(RuntimeError, len, self.result)


if __name__ == '__main__':
    main()
