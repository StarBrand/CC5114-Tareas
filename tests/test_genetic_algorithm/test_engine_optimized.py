"""test_engine_optimized.py: GeneticEngineOptimized unit test"""

from unittest import TestCase, main
from random import uniform, seed
from genetic_algorithm import GAEOptimized
from genetic_algorithm import Optimization
from genetic_algorithm.individuals import MultiObjectiveIndividual, Individual

POPULATION = 100
EPSILON = 0.1  # Epsilon to test difference between known optimal and found (not needed to be so accurate)


def _generate():
    return uniform(0, 10)


def _first_fitness(x: float):
    return -(x**2) + (12 * x) + 3.5


def _second_fitness(x: float):
    return ((1/5) * x) + 1


def _first_pareto(x: float):
    if x is not None:  # to have same functionality of _first_fitness
        return 2


def _second_pareto(x: float):
    if abs(x - 4) <= EPSILON:
        return 10
    else:
        return 0


class TesterIndividual(MultiObjectiveIndividual):
    """
    Individual for tester purpose with multi fitness
    """

    def __init__(self):
        super().__init__([_first_fitness, _second_fitness], _generate, 1, 0.0)

    def fitness(self) -> float:
        """
        Test fitness

        :return: Fitness
        """
        self.multi_fitness = list()
        for func in self._fitness_function:
            self.multi_fitness.append(func(self.chromosome[0]))
        return super().fitness()

    def get_gene(self) -> float:
        """
        Get only gene

        :return: Gene, a single float
        """
        return self.chromosome[0]

    def generate_individual(self) -> Individual:
        """
        Generate a new idem tester

        :return: New Tester
        """
        return TesterIndividual()


class ParetoTester(TesterIndividual):
    """
    Replace fitness function to test pareto optimization
    """
    def __init__(self):
        super().__init__()
        self._fitness_function = [_first_pareto, _second_pareto]

    def generate_individual(self) -> Individual:
        """
        Individual is generated from ParetoTester

        :return: A new instance of ParetoTester
        """
        return ParetoTester()


class EngineOptimizedTest(TestCase):

    def setUp(self) -> None:
        """
        Sets up test
        """
        self.engine = GAEOptimized(TesterIndividual())

    def test_elitism(self):
        self.engine.initialize_population(POPULATION)
        self.engine.population[0] = TesterIndividual()
        self.engine.evaluate_fitness()
        prev_score = 1  # due to provided function, min value
        for _ in range(100):
            self.engine.next_generation()
            actual = max(self.engine.population).my_fitness
            self.assertLessEqual(prev_score, actual, "In one generation, score was reduced")
            prev_score = actual

    def std_test_optimization(self, optimization: int, individual: MultiObjectiveIndividual, expected: int,
                              expected1: int, expected2: int, first: str, second: str):
        """
        Standard way to test run algorithm

        :param optimization: Optimization to be tested
        :param individual: Tester
        :param expected: Expected value of chromosome
        :param expected1: Expected value of another optimization (1)
        :param expected2: Expected value of another optimization (2)
        :param first: Another optimization (1)
        :param second: Another optimization (2)
        """
        self.engine = GAEOptimized(individual, optimization)
        self.engine.run_to_equilibrium(POPULATION, 10)
        actual = max(self.engine.population)
        self.assertGreaterEqual(EPSILON, abs(expected - actual.chromosome[0]), "Maximum individual not found")
        self.assertLessEqual(EPSILON, abs(expected1 - actual.chromosome[0]),
                             "Maximum individual found using {} optimization".format(first))
        self.assertLessEqual(EPSILON, abs(expected2 - actual.chromosome[0]),
                             "Maximum individual found using {} optimization".format(second))

    def test_optimization_pareto(self):
        seed(10)
        self.std_test_optimization(Optimization.PARETO, ParetoTester(), 4, 6, 10, "priority", "no")

    def test_optimization_priority(self):
        seed(10)
        self.std_test_optimization(Optimization.PRIORITY, TesterIndividual(), 6, 4, 10, "optimization", "no")

    def test_no_optimization(self):
        seed(10)
        self.std_test_optimization(Optimization.NONE, TesterIndividual(), 10, 6, 4, "priority", "pareto")


if __name__ == '__main__':
    main()
