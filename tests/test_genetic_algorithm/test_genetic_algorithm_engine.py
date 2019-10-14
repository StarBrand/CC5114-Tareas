"""test_genetic_algorithm_engine.py: unittest of GAEngine"""
from random import seed, randint, gauss
from unittest import TestCase, main
from genetic_algorithm import GAEngine
from genetic_algorithm.individuals import Individual

RANDOM_TEST = 5
POPULATION_SIZE = 100

seed(2)


class TesterIndividual(Individual):
    """An Individual design for testing purpose"""

    def __init__(self):
        super().__init__(gauss, mutation_rate=0.0)

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


def _zero():
    return 0.0


class TesterEquilibrium(TesterIndividual):
    """
    To test equilibrium on GA engine
    """
    def __init__(self):
        super().__init__()
        self.fitness_function = _zero

    def generate_individual(self) -> Individual:
        """
        Return TesterEquilibrium instead of TesterIndividual

        :return: TesterEquilibrium
        """
        return TesterEquilibrium()

    def fitness(self) -> float:
        """
        Return 0

        :return: 0
        """
        self.my_fitness = self.fitness_function()
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
        self.assertEqual(POPULATION_SIZE, len(actual_population), "Population size mismatch")
        self.assertEqual(POPULATION_SIZE, len(self.ga_engine), "Population size mismatch")
        for _ in range(RANDOM_TEST):
            i = randint(0, POPULATION_SIZE - 1)
            self.assertIsInstance(actual_population[i], TesterIndividual, "Population of unexpected class")

    def test_evaluate_fitness(self):
        self.assertLessEqual(self.ga_engine.solution_found(0.0), False, "Not always return false if not evaluated")
        self.ga_engine.evaluate_fitness()
        fitness = self.ga_engine.fitness
        self.assertEqual(len(fitness), POPULATION_SIZE, "Wrong number of fitness calculated")
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
        odd = 13
        self.ga_engine.initialize_population(odd)
        self.ga_engine.reproduction()
        expected = int(odd / 2) + 1
        self.assertEqual(expected, len(self.ga_engine))

    def test_initialize_again(self):
        self.assertEqual(POPULATION_SIZE, len(self.ga_engine), "Population size mismatch")
        self.ga_engine.initialize_population(100)
        self.assertEqual(100, len(self.ga_engine), "Population not over-generated")

    def test_run_no_solution(self):
        expected = 1e10  # unreachable
        max_generation = 10
        result = self.ga_engine.run_genetic_algorithm(expected, 10, max_generation=max_generation)
        generations = result.get_generations()[-1]
        found = result.found_solution
        self.assertEqual(max_generation, generations, "Not stop when supposed to")
        self.assertFalse(found, "Found it")

    def test_run_solution(self):
        expected = 50  # reachable
        result = self.ga_engine.run_genetic_algorithm(expected, 100)
        generations = result.get_generations()[-1]
        self.assertTrue(result.found_solution, "Solution not found")
        self.assertLessEqual(generations, 1000, "Run more than needed")

    def test_run_equilibrium(self):
        expected = 1e10  # unreachable
        max_generation = 10
        self.ga_engine.the_first_one = TesterEquilibrium()
        result = self.ga_engine.run_genetic_algorithm(expected, 100, equilibrium=max_generation)
        generations = result.get_generations()[-1]
        found = result.found_solution
        self.assertEqual(max_generation, generations, "Not stop when supposed to")
        self.assertFalse(found, "Found it")


if __name__ == '__main__':
    main()
