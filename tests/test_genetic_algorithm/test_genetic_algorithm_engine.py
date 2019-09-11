"""test_genetic_algorithm_engine.py: unittest of GAEngine"""
from random import seed, randint, gauss
from unittest import TestCase, main
from genetic_algorithm import GAEngine, Individual

RANDOM_TEST = 5
POPULATION_SIZE = 100

seed(2)


class TesterIndividual(Individual):
    """An Individual design for testing purpose"""

    def __init__(self):
        super(TesterIndividual, self).__init__(gauss, mutation_rate=0.0)

    def generate_individual(self) -> Individual:
        """
        test version (docstring in Individual)
        """
        return TesterIndividual()

    def get_allele(self, gene: str) -> object:
        """
        test version (docstring in Individual)

        :param gene:
        """
        pass

    def mutate(self) -> None:
        """
        test version (docstring in Individual)
        """
        pass

    def fitness(self) -> float:
        """
        test version (docstring in Individual)
        """
        self.my_fitness = self.fitness_function(50, 10)
        return self.my_fitness


class GAEngineTest(TestCase):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        tester = TesterIndividual()
        self.ga_engine = GAEngine(tester)
        self.ga_engine.initialize_population(POPULATION_SIZE)

    def test_initialize_population(self):
        actual_population = self.ga_engine.population
        self.assertEqual(len(actual_population), POPULATION_SIZE, "Population size mismatch")
        self.assertEqual(len(self.ga_engine), POPULATION_SIZE, "Population size mismatch")
        for _ in range(RANDOM_TEST):
            i = randint(0, POPULATION_SIZE - 1)
            self.assertIsInstance(actual_population[i], TesterIndividual, "Population of unexpected class")

    def test_evaluate_fitness(self):
        self.ga_engine.evaluate_fitness()
        fitness = self.ga_engine.fitness
        self.assertEqual(len(fitness), POPULATION_SIZE, "Wrong number of fitness calculated")
        score = max(fitness)
        expected_score = 90
        expected_score = 90
        self.assertFalse(self.ga_engine.solution_found(expected_score), "Solution not found")
        expected_score = 70
        self.assertTrue(self.ga_engine.solution_found(expected_score), "Solution found")

    def test_selection(self):
        expected_score = 50
        self.ga_engine.evaluate_fitness()
        old_score = sum(self.ga_engine.fitness) / len(self.ga_engine)
        self.ga_engine.selection(expected_score)
        actual_population = self.ga_engine.population
        self.assertLess(POPULATION_SIZE, len(actual_population), "Population did not duplicate on selection")
        self.assertEqual(POPULATION_SIZE * 2, len(actual_population), "Population did not duplicate on selection")
        # Due to fitness is random:
        new_score = sum([x.my_fitness for x in self.ga_engine.population]) / len(self.ga_engine)
        self.assertGreater(new_score, old_score, "Score did not improve")

    def test_reproduction(self):
        expected_score = 40
        self.ga_engine.evaluate_fitness()
        self.ga_engine.selection(expected_score)
        self.assertLess(POPULATION_SIZE, len(self.ga_engine), "Mismatch population size")
        self.ga_engine.reproduction()
        self.assertEqual(POPULATION_SIZE, len(self.ga_engine), "Reproduction failed")
        self.ga_engine.evaluate_fitness()

    def test_add(self):
        new_one = GAEngine(TesterIndividual())
        new_one.initialize_population(50)
        last_one = self.ga_engine + new_one
        self.assertEqual(POPULATION_SIZE + 50, len(last_one), "Add bad implemented")
        self.assertEqual(len(self.ga_engine) + len(new_one), len(last_one), "Add bad implemented")

    def test_robust_operations(self):
        with self.assertRaises(RuntimeError):
            self.ga_engine.selection()
        self.ga_engine.population.clear()
        with self.assertRaises(RuntimeError):
            self.ga_engine.evaluate_fitness()


if __name__ == '__main__':
    main()
