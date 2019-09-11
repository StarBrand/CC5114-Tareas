"""individual.py: Individual ABC"""

from __future__ import annotations
from abc import ABC, abstractmethod
from random import randint


class Individual(ABC):
    """An abstraction of an individual"""

    def __init__(self, fitness_function: callable, mutation_rate: float):
        self.chromosome = list()
        self.genes = list()
        self.fitness_function = fitness_function
        self.my_fitness = 0
        self.mutation_rate = mutation_rate

    @abstractmethod
    def generate_individual(self) -> Individual:
        """
        Return a concrete individual

        """
        pass

    @abstractmethod
    def get_allele(self, gene: str) -> object:
        """
        Get allele (characteristics) of name 'gene'

        :param gene: Name of gene
        :return: The characteristics of the individual
        """
        pass

    def fitness(self) -> float:
        """
        Evaluate fitness of individual

        :return: Fitness
        """
        self.my_fitness = self.fitness_function(chromosome=self.chromosome)
        return self.my_fitness

    @abstractmethod
    def mutate(self) -> None:
        """
        Mutate an allele

        :return: None
        """
        pass

    def crossover(self, partner: Individual) -> Individual:
        """
        Standard method to generate new individual by recombining his chromosome

        :param partner: Another individual
        :raises: TypeError: If size of chromosomes do not match
                 TypeError: If number of genes do not match
        :return: New individual recombined
        """
        if len(partner) != len(self):
            raise TypeError("Cannot do crossover, due to mismatch number of genes")
        if partner.genes != self.genes:
            raise TypeError("Cannot do crossover, due to different genes")
        child = self.generate_individual()
        chiasma = randint(0, len(self))
        first_half = self.chromosome[0:chiasma]
        second_half = partner.chromosome[chiasma:len(partner)]
        child.chromosome = first_half + second_half
        child.mutate()
        return child

    def __gt__(self, other: Individual) -> bool:
        return self.my_fitness > other.my_fitness

    def __lt__(self, other: Individual) -> bool:
        return self.my_fitness < other.my_fitness

    def __ge__(self, other: Individual) -> bool:
        return self.my_fitness >= other.my_fitness

    def __le__(self, other: Individual) -> bool:
        return self.my_fitness <= other.my_fitness

    def __len__(self):
        return len(self.chromosome)
