"""binary_calculator.py: BinaryCalculator class"""
from math import pow
from random import choice, uniform
from genetic_algorithm.individuals import Individual


def _fitness(binary: [bool], expected: int) -> float:
    result = 0
    for index, bit in enumerate(reversed(binary)):
        result += pow(2, index) * int(bit)
    return - abs(expected - result)


class BinaryCalculator(Individual):
    """BinaryCalculator, generate an array of bits"""

    def __init__(self, mutation_rate: float, number: int, bits: int):
        super(BinaryCalculator, self).__init__(_fitness, mutation_rate)
        self.number_to_calculate = number
        for bit in reversed(range(bits)):
            self.chromosome.append(self._bit())
            self.genes.append(str(bit))

    @staticmethod
    def _bit() -> int:
        return int(choice([True, False]))

    def generate_individual(self) -> Individual:
        """
        Return another Word Guesser

        :return: New word guesser
        """
        return BinaryCalculator(self.mutation_rate, self.number_to_calculate, len(self.genes))

    def mutate(self) -> None:
        """
        Mutate an allele

        :return: None
        """
        for index, _ in enumerate(self.chromosome):
            if uniform(0, 1) <= self.mutation_rate:
                self.chromosome[index] = self._bit()
        return None

    def fitness(self) -> float:
        """
        Evaluate fitness of individual

        :return: Fitness
        """
        self.my_fitness = self.fitness_function(self.chromosome, self.number_to_calculate)
        return self.my_fitness
