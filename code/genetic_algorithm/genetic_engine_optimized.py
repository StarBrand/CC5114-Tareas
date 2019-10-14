"""genetic_engine_optimized.py: GeneticEngineOptimized class"""

from types import MethodType
from copy import deepcopy
from genetic_algorithm import GAEngine, GAResult
from genetic_algorithm.individuals import MultiObjectiveIndividual

TOURNAMENT_SIZE = 5
MAX_GENERATIONS = 1000


class GeneticEngineOptimized(GAEngine):
    """
    Genetic Algorithm engine, for multi objective individual (and his optimization)
    and elitism
    """
    def __init__(self, population_type: MultiObjectiveIndividual):
        super().__init__(population_type)

    def selection(self, tournament_size: int = TOURNAMENT_SIZE) -> None:
        """
        Select population using tournament algorithm, and making sure winner stays

        :param tournament_size: (Optional) Amount of contestant
               if less than actual population size, use a quarter of that
        :return: None
        """
        winner = deepcopy(max(self.population))
        super().selection(tournament_size)
        self.population[0] = winner
        return

    def run_genetic_algorithm(self, expected_score: float, population_size: int, equilibrium: int or None = None,
                              log: bool = False, acceptable: float = 0.0, max_generation: int = MAX_GENERATIONS,
                              tournament_size: int = TOURNAMENT_SIZE) -> GAResult:
        """

        :param expected_score:
        :param population_size:
        :param equilibrium:
        :param log:
        :param acceptable:
        :param max_generation:
        :param tournament_size:
        :return:
        """
        self.reproduction = super().reproduction
        return super().run_genetic_algorithm(expected_score, population_size, equilibrium=equilibrium, log=log,
                                                 acceptable=acceptable, max_generation=max_generation,
                                                 tournament_size=tournament_size)

    def run_optimized_pareto(self, expected_score: float, population_size: int, equilibrium: int or None = None,
                             log: bool = False, acceptable: float = 0.0, max_generation: int = MAX_GENERATIONS,
                             tournament_size: int = TOURNAMENT_SIZE) -> GAResult:
        """


        :param expected_score:
        :param population_size:
        :param equilibrium:
        :param log:
        :param acceptable:
        :param max_generation:
        :param tournament_size:
        :return:
        """
        self.reproduction = self._reproduction_pareto
        return super().run_genetic_algorithm(expected_score, population_size, equilibrium=equilibrium, log=log,
                                                 acceptable=acceptable, max_generation=max_generation,
                                                 tournament_size=tournament_size)

    def run_optimized_priority(self, expected_score: float, population_size: int, equilibrium: int or None = None,
                               log: bool = False, acceptable: float = 0.0, max_generation: int = MAX_GENERATIONS,
                               tournament_size: int = TOURNAMENT_SIZE) -> GAResult:
        """


        :param expected_score:
        :param population_size:
        :param equilibrium:
        :param log:
        :param acceptable:
        :param max_generation:
        :param tournament_size:
        :return:
        """
        self.reproduction = self._reproduction_priority
        return super().run_genetic_algorithm(expected_score, population_size, equilibrium=equilibrium, log=log,
                                                 acceptable=acceptable, max_generation=max_generation,
                                                 tournament_size=tournament_size)

    def _reproduction_pareto(self) -> None:
        super().reproduction()
        for index, _ in enumerate(self.population):
            self.population[index].pareto = True
            self.population[index].priority = False

    def _reproduction_priority(self) -> None:
        super().reproduction()
        for index, _ in enumerate(self.population):
            self.population[index].pareto = False
            self.population[index].priority = True
