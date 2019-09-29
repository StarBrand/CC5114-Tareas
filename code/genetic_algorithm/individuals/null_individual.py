"""individual.py: NullIndividual to initialize GAResult"""

from __future__ import annotations
from genetic_algorithm.individuals import Individual


def _null_function() -> float:
    return 0.0


class NullIndividual(Individual):
    """An abstraction of an individual"""

    def __init__(self):
        super(NullIndividual, self).__init__(_null_function, 0.0)

    def generate_individual(self) -> Individual:
        """
        NullIndividual

        :return: Other instance of NullIndividual
        """
        return NullIndividual()

    def get_allele(self, gene: str) -> object:
        """
        Do nothing

        :param gene: Name of gene
        :return: The characteristics of the individual
        """
        return None

    def fitness(self) -> float:
        """
        Evaluate fitness of individual

        :return: Fitness
        """
        self.my_fitness = self.fitness_function()
        return self.my_fitness

    def mutate(self) -> None:
        """
        Do nothing

        :return: None
        """
        return None

    def crossover(self, partner: Individual) -> Individual:
        """
        Do nothing

        :param partner: To be ignored
        :return: NullIndividual
        """
        return self.generate_individual()
