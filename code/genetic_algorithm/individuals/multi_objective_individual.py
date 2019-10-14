"""multi_objective_individual.py: MultiObjectiveIndividual class"""

from __future__ import annotations
from abc import ABC, abstractmethod
from genetic_algorithm.individuals import Individual


class MultiObjectiveIndividual(Individual, ABC):
    """
    Individual with multiple functions of fitness
    """

    def __init__(self, fitness: [callable], mutation_rate: float, pareto: bool = False, priority: bool = False):
        super().__init__(None, mutation_rate)
        self.multi_fitness = []
        self.fitness_function = fitness
        self.pareto = pareto
        self.priority = priority

    @abstractmethod
    def fitness(self) -> float:
        """
        Evaluate fitness as the minimum of all fitness

        :return: Fitness
        """
        self.my_fitness = min(self.multi_fitness)
        return self.my_fitness

    def __gt__(self, other: MultiObjectiveIndividual) -> bool:
        if self.priority:
            for index, func in enumerate(self.multi_fitness):
                if func != other.multi_fitness[index]:
                    return func > other.multi_fitness[index]
            return False
        elif self.pareto:
            exist = False
            for index, func in enumerate(self.multi_fitness):
                if not exist and func > other.multi_fitness[index]:
                    exist = True
                if func < other.multi_fitness[index]:
                    return False
            return exist
        else:
            return super().__gt__(other)

    def __eq__(self, other: MultiObjectiveIndividual) -> bool:
        if super().__eq__(other):
            return (self.multi_fitness == other.multi_fitness
                    and self.pareto == other.pareto
                    and self.priority == other.priority)
        else:
            return False
