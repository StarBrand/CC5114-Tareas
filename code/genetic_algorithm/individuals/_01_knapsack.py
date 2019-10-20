"""_01_knapsack.py: 0-1-Knapsack problem"""

from random import choice
from genetic_algorithm.individuals import UnboundKnapsack, Individual
from useful.simulations import BOX1, BOX2, BOX3, BOX4, BOX5

BOXES = [BOX1, BOX2, BOX3, BOX4, BOX5]


def _capacity(boxes: [int]) -> float:
    capacity = 15  # kg
    total_weight = 0
    for box, choose in zip(BOXES, boxes):
        total_weight += (box.weight * choose)
    difference = capacity - total_weight
    if difference >= 0:
        return 0.0
    else:
        return difference


def _value(boxes: [int]) -> float:
    total_value = 0
    for box, choose in zip(BOXES, boxes):
        total_value += (box.value * choose)
    return total_value


def _boxes() -> int:
    return choice([0, 1])


class Knapsack01(UnboundKnapsack):
    """
    Model the 0-1-Knapsack problem, using Unbound Knapsack as template
    """
    def __init__(self, mutation_rate: float):
        super(UnboundKnapsack, self).__init__([_capacity, _value], _boxes, 5, mutation_rate)
        for i in range(5):
            self.genes.append("box{}".format(i + 1))
        return

    def generate_individual(self) -> Individual:
        """
        Generate new individual

        :return: New instance Knapsack01
        """
        return Knapsack01(self.mutation_rate)
