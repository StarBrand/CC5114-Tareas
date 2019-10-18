"""travel_path.py: TravelPath class"""
import networkx as nx
from copy import deepcopy
from random import sample, uniform, randint
from genetic_algorithm.individuals import Individual

towns = []


def _travel_length(path: [str], state_map: nx.Graph) -> float:
    result = 0
    start = path[0]
    for town in path[1: len(path)]:
        result += state_map.get_edge_data(start, town)['weight']
        start = deepcopy(town)
    return -result


def _not_visited_town() -> str:
    global towns
    selected = randint(0, len(towns) - 1)
    return towns.pop(selected)


class TravelPath(Individual):
    """TravelPath, traveling sales problem candidate solution"""

    def __init__(self, mutation_rate: float, state: nx.Graph):
        self.state = state.copy()
        global towns
        towns = list(deepcopy(self.state.nodes))
        super().__init__(_travel_length, _not_visited_town, len(towns), mutation_rate)
        for gen, _ in enumerate(self.chromosome):
            if gen == 0:
                self.genes.append("start")
            elif gen == len(self) - 1:
                self.genes.append("end")
            else:
                self.genes.append("town{}".format(gen))

    def generate_individual(self) -> Individual:
        """
        Return another TravelPath

        :return: New travel path
        """
        return TravelPath(self.mutation_rate, self.state)

    def mutate(self) -> None:
        """
        Mutate an allele

        :return: None
        """
        for index, _ in enumerate(self.chromosome):
            if uniform(0, 1) < self.mutation_rate:
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
        return super().fitness(path=self.chromosome, state_map=self.state)
