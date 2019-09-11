"""genetic_algorithm_engine.py: Genetic Algorithm Engine class"""

from __future__ import annotations
import logging
from random import randint
from copy import deepcopy
from genetic_algorithm import Individual

TOURNAMENT_SIZE = 5


class GAEngine(object):
    """Genetic Algorithm Engine"""

    def __init__(self, population_type: Individual):
        self.the_first_one = population_type
        self.population = list()
        self.fitness = list()
        self.selected = False
        return

    def initialize_population(self, size: int) -> None:
        """
        Generate a population of individual of class 'population_type'

        :param size: Size of population
        :return: None
        """
        self.selected = False
        if len(self.population) != 0:
            logging.warning("Actual population was erased and a new one was generated")
        self.population.clear()
        for _ in range(size):
            self.population.append(self.the_first_one.generate_individual())
        return

    def evaluate_fitness(self) -> None:
        """
        Evaluate fitness of every Individual on population

        :raise: RuntimeError in case there is no population
        :return: None
        """
        self.selected = False
        if len(self) == 0:
            raise RuntimeError("Cannot calculate fitness if there is no population")
        self.fitness.clear()
        for index, _ in enumerate(self.population):
            self.fitness.append(self.population[index].fitness())
        return

    def solution_found(self, expected: float, acceptable: float = 0.0) -> bool:
        """
        Indicates whether the solution was found

        :param expected: Expected fitness to be found
        :param acceptable: Acceptable difference between score and expectation
        :return: Logical value of proposition: "Solution is found"
        """
        if len(self.fitness) == 0:
            logging.warning("No solution found, due to fitness has not been calculated")
            return False
        for score in self.fitness:
            if expected - score <= acceptable:
                return True
        return False

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

        :return:
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
        if not self.selected:
            logging.warning("Population was reproduced, but without selection, population size will mismatch")
        return None

    def __len__(self):
        return len(self.population)

    def __add__(self, other: GAEngine) -> GAEngine:
        new_one = deepcopy(self)
        new_one.population = self.population + other.population
        new_one.selected = False
        return new_one
