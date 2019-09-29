"""travel_path.py: TravelPath class"""
import networkx as nx
from copy import deepcopy
from random import sample, uniform, randint
from genetic_algorithm.individuals import Individual


def _fitness(path: [str], town_map: nx.Graph) -> float:
    result = 0
    start = path[0]
    for town in path[1: len(path)]:
        result += town_map.get_edge_data(start, town)['weight']
        start = deepcopy(town)
    return -result


class TravelPath(Individual):
    """TravelPath, traveling sales problem candidate solution"""

    def __init__(self, mutation_rate: float, state: nx.Graph):
        super(TravelPath, self).__init__(_fitness, mutation_rate)
        self.state = state.copy()
        self.chromosome = sample(list(self.state.nodes), k=len(self.state.nodes))
        for gen, _ in enumerate(self.chromosome):
            if gen == 0:
                self.genes.append("start")
            elif gen == len(self) - 1:
                self.genes.append("end")
            else:
                self.genes.append("town{}".format(gen))

    def generate_individual(self) -> Individual:
        """
        Return another Word Guesser

        :return: New word guesser
        """
        return TravelPath(self.mutation_rate, self.state)

    def mutate(self) -> None:
        """
        Mutate an allele

        :return: None
        """
        for index, _ in enumerate(self.chromosome):
            if uniform(0, 1) <= self.mutation_rate:
                swap = randint(0, len(self) - 1)
                if swap >= index:
                    swap += 1
                self.chromosome[index], self.chromosome[swap] = self.chromosome[swap], self.chromosome[index]
        return None

    def crossover(self, partner: Individual) -> Individual:
        """
        Not the same crossover as individuals

        :param partner: Individual to be crossing over
        """
        if len(partner) != len(self):
            raise TypeError("Cannot do crossover, due to mismatch number of genes")
        if partner.genes != self.genes:
            raise TypeError("Cannot do crossover, due to different genes")
        child = deepcopy(self)
        chiasmas = sample(range(len(self)), k=2)
        fragment = partner.chromosome[min(chiasmas):max(chiasmas)]
        insertion = child.chromosome.index(fragment[0])
        for gen in fragment:
            child.chromosome.remove(gen)
        child.chromosome = child.chromosome[0: insertion] + fragment + child.chromosome[insertion: len(child)]
        child.mutate()
        return child

    def fitness(self) -> float:
        """
        Evaluate fitness of individual

        :return: Fitness
        """
        self.my_fitness = self.fitness_function(self.chromosome, self.state)
        return self.my_fitness
