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

    def evaluate_fitness(self, register: bool = False, **kwargs) -> None:
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
            self.fitness.append(self.population[index].fitness(**kwargs))
        if register:
            winner = self.population.index(max(self.population))
            loser = self.population.index(min(self.population))
            mean = sum(self.fitness) / len(self.fitness)
            self.result.register_score(self.fitness[winner], mean, self.fitness[loser], generation=self.generation)
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
            logging.info("Generation: {}".format(self.generation))
            logging.info("\tCloser one:\n{}".format(close))
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
        self.selected = False
        return None

    def next_generation(self, register: bool = False, tournament_size: int = TOURNAMENT_SIZE, **kwargs) -> None:
        """
        Generate a new generation doing the three needed steps

        :param register:
        :param tournament_size:
        :return:
        """
        self.selection(tournament_size=tournament_size)
        self.reproduction()
        self.evaluate_fitness(register=register, **kwargs)
        return

    def run_to_reach(self, expected_score: float, acceptable: float, population_size: int,
                     max_generation: int = MAX_GENERATIONS, tournament_size: int = TOURNAMENT_SIZE,
                     use_prev: bool = False,  log: bool = False, **kwargs) -> GAResult:
        """
        Run algorithm until reach expected score with an acceptable (given) margin

        :param expected_score: Score expected to reach
        :param acceptable: Acceptable margin
        :param population_size: Size of the population
        :param max_generation: (optional) Maximum of generation (fixed for safety)
        :param tournament_size: (optional) Size of tournament, default: TOURNAMENT_SIZE (begin of file)
        :param use_prev: (optional) Use actual generated generation
        :param log: (optional) Print logs
        :raises RuntimeError: If prev_generation is given true without a population generated
        :return: Result of algorithm
        """
        self._initialize(population_size, use_prev, **kwargs)
        internal_generation = 1
        while internal_generation < max_generation and not self.solution_found(expected_score, acceptable, log=log):
            self.next_generation(register=True, tournament_size=tournament_size, **kwargs)
            internal_generation += 1
        self.result.ready_to_export(max(self.population), self.solution_found(expected_score, acceptable, log=log))
        return self.result

    def run_to_equilibrium(self, population_size: int, equilibrium: int, max_generation: int = MAX_GENERATIONS,
                           tournament_size: int = TOURNAMENT_SIZE, use_prev: bool = False,
                           log: bool = False, **kwargs) -> GAResult:
        """
        Run algorithm until score does not change on 'equilibrium' times

        :param population_size: Size of population
        :param equilibrium: Number of generation with same score to stop algorithm
        :param max_generation: (optional) maximum generation
        :param tournament_size: (optional) size of tournament for selection
        :param use_prev: (optional) Use actual generated generation
        :param log: (optional) Print logs
        :return: Result of algorithm
        """
        def _register():
            if log:
                logging.info("Generation: {}".format(self.generation))
                logging.info("\tCloser one: {}".format(max(self.population)))
        self._initialize(population_size, use_prev)
        internal_generation = 1
        times_in_a_row = 1
        score = max(self.population).my_fitness
        prev_score = score
        while internal_generation < max_generation and times_in_a_row < equilibrium:
            _register()
            self.next_generation(register=True, tournament_size=tournament_size, **kwargs)
            score = max(self.population).my_fitness
            if prev_score == score:
                times_in_a_row += 1
            else:
                times_in_a_row = 1
                prev_score = score
            internal_generation += 1
        _register()
        self.result.ready_to_export(max(self.population), True)
        return self.result

    def run_fixed_generation(self, population_size: int, max_generation: int, tournament_size: int = TOURNAMENT_SIZE,
                             use_prev: bool = False, log: bool = False, **kwargs) -> GAResult:
        """
        Run algorithm until reach expected score with an acceptable (given) margin

        :param population_size: Size of the population
        :param max_generation: Maximum of generation (fixed for safety)
        :param tournament_size: (optional) Size of tournament, default: TOURNAMENT_SIZE (begin of file)
        :param use_prev: (optional) Use actual generated generation
        :param log: (optional) Print logs
        :raises RuntimeError: If prev_generation is given true without a population generated
        :return: Result of algorithm
        """
        self._initialize(population_size, use_prev)
        internal_generation = 1
        if log:
            logging.info("Generation: {}".format(self.generation))
            logging.info("\tCloser one: {}".format(max(self.population).chromosome))
        while internal_generation < max_generation:
            self.next_generation(register=True, tournament_size=tournament_size, **kwargs)
            if log:
                logging.info("Generation: {}".format(self.generation))
                logging.info("\tCloser one: {}".format(max(self.population).chromosome))
            internal_generation += 1
        self.result.ready_to_export(max(self.population), True)
        return self.result

    def _initialize(self, population_size: int, use_prev: bool, **kwargs) -> None:
        """
        Initialize run algorithm

        :param population_size: Population size (not used if use_prev = True)
        :param use_prev: Use previous generated generation (otherwise, erase it and initialize anew)
        :raises RuntimeError: Use previous generation when there is no one
        :return: None (update self.population)
        """
        if not use_prev:
            self.initialize_population(population_size)
            self.evaluate_fitness(register=True, **kwargs)
        elif len(self.population) == 0:
            raise RuntimeError("Not population to use")

    def __len__(self):
        return len(self.population)

    def __add__(self, other: GAEngine) -> GAEngine:
        new_one = deepcopy(self)
        new_one.population = self.population + other.population
        new_one.selected = False
        return new_one
