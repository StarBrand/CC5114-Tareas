"""binary_calculator.py: BinaryCalculator class"""
from math import pow
from random import choice, uniform
from genetic_algorithm.individuals import Individual


def _fitness(binary: [bool], expected: int) -> float:
    result = 0
    for index, bit in enumerate(reversed(binary)):
        result += pow(2, index) * int(bit)
    return - abs(expected - result)


def _bit() -> int:
    return int(choice([True, False]))


class BinaryCalculator(Individual):
    """BinaryCalculator, generate an array of bits"""

    def __init__(self, mutation_rate: float, number: int, bits: int):
        super().__init__(_fitness, _bit, bits, mutation_rate)
        self.number_to_calculate = number
        for bit in reversed(range(bits)):
            self.genes.append(str(bit))

    def generate_individual(self) -> Individual:
        """
        Return another Word Guesser

        :return: New word guesser
        """
        return BinaryCalculator(self.mutation_rate, self.number_to_calculate, len(self.genes))

    def fitness(self) -> float:
        """
        Evaluate fitness of individual

        :return: Fitness
        """
        return super().fitness(binary=self.chromosome, expected=self.number_to_calculate)
