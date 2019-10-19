"""unbound_knapsack.py: Unbound Knapsack class"""

from random import choice
from genetic_algorithm.individuals import MultiObjectiveIndividual, Individual
from useful.simulations import Box, NullBox, BOX1, BOX2, BOX3, BOX4, BOX5


def _capacity(boxes: [Box]) -> float:
    capacity = 15  # kg
    total_weight = 0.0
    for box in boxes:
        total_weight += box.weight
    difference = capacity - total_weight
    if difference >= 0:
        return 0.0
    else:
        return difference


def _value(boxes: [Box]) -> float:
    total_value = 0
    for box in boxes:
        total_value += box.value
    return total_value


def _boxes() -> int:
    return choice([BOX1, BOX2, BOX3, BOX4, BOX5, NullBox])


class UnboundKnapsack(MultiObjectiveIndividual):
    """Model the unbound-knapsack problem"""

    def __init__(self, mutation_rate: float):
        super().__init__([_capacity, _value], _boxes, 15, mutation_rate)
        for i in range(15):
            self.genes.append("box{}".format(i + 1))
        return

    def fitness(self) -> float:
        """
        Calculate, storage and return fitness.
        Storage min fitness, but compare according to optimization

        :return: Second fitness
        """
        self.multi_fitness = list()
        for func in self._fitness_function:
            self.multi_fitness.append(func(self.chromosome))
        self.my_fitness = min(self.multi_fitness)
        return self.multi_fitness[1]

    def generate_individual(self) -> Individual:
        """
        Generate new individual

        :return: New instance UnboundKnapsack
        """
        return UnboundKnapsack(self.mutation_rate)
