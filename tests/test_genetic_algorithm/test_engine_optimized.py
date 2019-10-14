"""test_engine_optimized.py: GeneticEngineOptimized unit test"""

from unittest import TestCase, main
from random import choice
from genetic_algorithm import GeneticEngineOptimized
from genetic_algorithm.individuals import MultiObjectiveIndividual, Individual

POPULATION = 100
EPSILON = 1e-10


class TesterIndividual(MultiObjectiveIndividual):
    """
    Individual for tester purpose with multi fitness
    """

    def __init__(self, char: float):
        super().__init__([self._first_fitness,
                                                self._second_fitness,
                                                self._third_fitness], 0.0)
        self.char = char

    def __repr__(self):
        return str(self.char)

    def fitness(self) -> float:
        """
        Test fitness

        :return: Fitness
        """
        self.multi_fitness = list()
        for func in self.fitness_function:
            self.multi_fitness.append(func(self.char))
        self.my_fitness = min(self.multi_fitness)
        return self.my_fitness

    def generate_individual(self) -> Individual:
        """
        Generate a new idem tester

        :return: New Tester
        """
        char = choice([1.0, 1.5, 2.0])
        return TesterIndividual(char)

    def mutate(self) -> None:
        """
        Mutate do nothing
        :return: None
        """
        return

    @staticmethod
    def _first_fitness(char: float) -> float:
        return 1.0 * char

    @staticmethod
    def _second_fitness(char: float) -> float:
        return 2.0 / char

    @staticmethod
    def _third_fitness(char: float) -> float:
        return 3.0 + char


class EngineOptimizedTest(TestCase):

    def setUp(self) -> None:
        """
        Sets up test
        """
        self.engine = GeneticEngineOptimized(TesterIndividual(1.0))

    def test_elitism(self):
        self.engine.initialize_population(POPULATION)
        self.engine.population[0] = TesterIndividual(1.5)
        self.engine.evaluate_fitness()
        for _ in range(100):
            self.engine.selection()
            self.engine.reproduction()
            self.engine.evaluate_fitness()
            actual = max(self.engine.population)
            self.assertGreaterEqual(EPSILON, abs(actual.char - 1.5), "In one generation, winner was not selected")

    def test_optimization_pareto(self):
        self.engine.run_genetic_algorithm(1000, POPULATION, max_generation=3)
        actual = max(self.engine.population)
        uno = TesterIndividual(2.0)
        dos = TesterIndividual(1.0)
        uno.fitness(), dos.fitness()
        uno.pareto, dos.pareto = True, True
        print(uno > dos)
        print(dos > uno)
        print(self.engine.population)
        print(actual.multi_fitness)
        print(actual.char)
        self.engine.run_optimized_pareto(1000, POPULATION, max_generation=3)
        actual = max(self.engine.population)
        print(self.engine.population)
        print(actual.multi_fitness)
        print(actual.char)

    def test_optimization_priority(self):
        self.engine.run_optimized_priority(1000, POPULATION, max_generation=3)
        actual = max(self.engine.population)
        print(actual)


if __name__ == '__main__':
    main()
