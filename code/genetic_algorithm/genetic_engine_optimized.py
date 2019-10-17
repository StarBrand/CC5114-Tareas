"""genetic_engine_optimized.py: GeneticEngineOptimized class"""

from copy import deepcopy
from genetic_algorithm import GAEngine, Optimization
from genetic_algorithm.individuals import MultiObjectiveIndividual

TOURNAMENT_SIZE = 5
MAX_GENERATIONS = 1000


class GAEOptimized(GAEngine):
    """
    Genetic Algorithm engine, for multi objective individual (and his optimization)
    and elitism
    """
    def __init__(self, population_type: MultiObjectiveIndividual, optimization: int = Optimization.NONE):
        super().__init__(population_type)
        self.optimization = optimization

    def selection(self, tournament_size: int = TOURNAMENT_SIZE) -> None:
        """
        Select population using tournament algorithm, and making sure winner stays

        :param tournament_size: (Optional) Amount of contestant
               if less than actual population size, use a quarter of that
        :return: None
        """
        # Save winner
        winner = deepcopy(max(self.population))
        # Do selection
        super().selection(tournament_size)
        # Include winner
        self.population[0] = winner
        return

    def initialize_population(self, size: int) -> None:
        """
        Generate population, altering individual to optimization

        :param size: Size of population
        :return: None (alter self.population)
        """
        super().initialize_population(size)
        self._optimize_population()
        return

    def next_generation(self, register: bool = False, tournament_size: int = TOURNAMENT_SIZE) -> None:
        """
        Generate next generation, adding optimization

        :param register: Register generation
        :param tournament_size: (Optional) Tournament size
        :return: None (alter self.population)
        """
        self.selection(tournament_size=tournament_size)
        self.reproduction()
        self._optimize_population()
        self.evaluate_fitness(register=register)
        return

    def _optimize_population(self) -> None:
        """
        Turn every individual of population to optimization of engine

        :return: None (alter self.population)
        """
        for index, _ in enumerate(self.population):
            self.population[index].pareto = False
            if self.optimization == Optimization.PRIORITY:
                self.population[index].priority = True
            else:
                self.population[index].priority = False
            if self.optimization == Optimization.PRIORITY:
                self.population[index].pareto = True
            else:
                self.population[index].pareto = False
        return
