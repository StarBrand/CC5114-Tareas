"""genetic_algorithm_engine.py: Genetic Algorithm Engine class"""

from __future__ import annotations
import logging
from random import randint
from copy import deepcopy
from genetic_algorithm import GAResult
from genetic_algorithm.individuals import Individual

TOURNAMENT_SIZE = 5
MAX_GENERATIONS = 1000


class GAEngine(object):
    """Genetic Algorithm Engine"""

    def __init__(self, population_type: Individual):
        self.the_first_one = population_type
        self.population = list()
        self.fitness = list()
        self.selected = False
        self.generation = 0
        self.result = GAResult()
        return

    def initialize_population(self, size: int) -> None:
        """
        Generate a population of individual of class 'population_type'

        :param size: Size of population
        :return: None
        """
        self.result = GAResult()
        self.selected = False
        if len(self.population) != 0:
            logging.warning("Actual population was erased and a new one was generated")
        self.population.clear()
        for _ in range(size):
            self.population.append(self.the_first_one.generate_individual())
        self.generation = 1
        return

    def evaluate_fitness(self, register: bool = False) -> None:
        """
        Evaluate fitness of every Individual on population

        :raise: RuntimeError in case there is no population
        :param: register: register max fitness found
        :return: None
        """
        self.selected = False
        if len(self) == 0:
            raise RuntimeError("Cannot calculate fitness if there is no population")
        self.fitness.clear()
        for index, _ in enumerate(self.population):
            self.fitness.append(self.population[index].fitness())
        if register:
            self.result.register_score(max(self.fitness), generation=self.generation)
        return

    def solution_found(self, expected: float, acceptable: float = 0.0, log: bool = False) -> bool:
        """
        Indicates whether the solution was found

        :param expected: Expected fitness to be found
        :param acceptable: Acceptable difference between score and expectation
        :param log: Show logging (info)
        :return: Logical value of proposition: "Solution is found"
        """
        if len(self.fitness) == 0:
            logging.warning("No solution found, due to fitness has not been calculated")
            return False
        close = max(self.population)
        if log:
            logging.info("Closed: {}".format(close.chromosome))
        score = close.my_fitness
        return expected - score <= acceptable

    def selection(self, tournament_size: int = TOURNAMENT_SIZE) -> None:
        """
        Select population using tournament algorithm

        :param tournament_size: (Optional) Amount of contestant
                                if less than actual population size, use a quarter of that
        :return: None
        """
        if len(self.fitness) == 0:
            raise RuntimeError("Cannot select before calculate fitness")
        self.selected = True
        use = tournament_size
        if len(self) <= tournament_size:
            use = int(len(self) / 4)
        selected = list()
        tournament = list()
        for _ in range(len(self) * 2):
            tournament.clear()
            for _ in range(use):
                tournament.append(self.population[randint(0, len(self) - 1)])
            selected.append(max(tournament))
        self.population.clear()
        self.population = selected.copy()
        return

    def reproduction(self) -> None:
        """
        Generate next generation of population

        :return: None
        """
        next_gen = list()
        while len(self) != 0:
            parent_one = self.population.pop()
            try:
                parent_two = self.population.pop()
                next_gen.append(parent_one.crossover(parent_two))
            except IndexError:
                next_gen.append(parent_one)
        self.population = next_gen.copy()
        self.generation += 1
        if not self.selected:
            logging.warning("Population was reproduced, but without selection, population size will mismatch")
        return None

    # TODO: separate run algorithm for purpose (equilibrium, reach, max generations)
    def run_genetic_algorithm(self, expected_score: float, population_size: int, equilibrium: int or None = None,
                              log: bool = False, acceptable: float = 0.0, max_generation: int = MAX_GENERATIONS,
                              tournament_size: int = TOURNAMENT_SIZE) -> GAResult:
        """
        Run genetic algorithm

        :param expected_score: Score to reach
        :param population_size: Population size (number of Individuals)
        :param equilibrium: If it is None, it means nothing; but if not, the algorithm run until the same score is
                            found 'equilibrium' times in a row
        :param log: Show logging (info)
        :param acceptable: Acceptable difference to consider algorithm find a solution
        :param max_generation: Maximum number of generation to consider algorithm fail and end it
        :param tournament_size: Size of tournament for selection
        :return: Result to be exported
        """
        self.initialize_population(population_size)
        times_in_a_row = 0
        prev_score = None
        while True:
            if log:
                logging.info("Generation {}".format(self.generation))
            self.evaluate_fitness(register=True)
            winner = max(self.population)
            score = max(self.population).my_fitness
            if self.solution_found(expected_score, acceptable=acceptable, log=log):
                self.result.ready_to_export(winner, True)
                return self.result
            if self.generation == max_generation:
                self.result.ready_to_export(winner, False)
                return self.result
            if equilibrium is not None:
                if prev_score is None:
                    prev_score = score
                    times_in_a_row += 1
                else:
                    if prev_score == score:
                        times_in_a_row += 1
                    else:
                        prev_score = None
                        times_in_a_row = 0
                    if times_in_a_row == equilibrium:
                        self.result.ready_to_export(winner, False)
                        return self.result
            self.selection(tournament_size=tournament_size)
            self.reproduction()

    def __len__(self):
        return len(self.population)

    def __add__(self, other: GAEngine) -> GAEngine:
        new_one = deepcopy(self)
        new_one.population = self.population + other.population
        new_one.selected = False
        return new_one
