"""test_travel_path.py: Unit test of TravelPath"""
from test_genetic_algorithm import IndividualTest
from unittest import main
from networkx import Graph
from random import seed
from copy import deepcopy
from genetic_algorithm.individuals import TravelPath

"""Nodes"""
A = "A"
B = "B"
C = "C"
D = "D"
E = "E"
NODES = [A, B, C, D, E]

"""Edges"""
EDGES = [(A, B, {'weight': 10}), (A, C, {'weight': 20}), (A, D, {'weight': 30}), (A, E, {'weight': 40}),
         (B, C, {'weight': 50}), (B, D, {'weight': 70}), (B, E, {'weight': 250}),
         (C, D, {'weight': 42}), (C, E, {'weight': 3}),
         (D, E, {'weight': 109})]

LENGTH = len(NODES)


class TravelPathTest(IndividualTest):

    def setUp(self) -> None:
        """
        Sets up unittest
        """
        graph = Graph()
        graph.add_nodes_from(NODES)
        graph.add_edges_from(EDGES)
        self.individual = TravelPath(0.3, graph)
        self.stable_one = TravelPath(0, graph)

    def test_constructor(self):
        self.std_test_constructor(LENGTH, LENGTH)

    def test_generate_individual(self):
        self.std_test_generate_individual(LENGTH, LENGTH)

    def test_crossover(self):
        seed(10)
        first_new_one = self.individual.generate_individual()
        first_expected = deepcopy(self.individual.chromosome)
        insertion = first_expected.index(first_new_one.chromosome[0])
        for gen in first_new_one.chromosome[0: 3]:
            first_expected.remove(gen)
        first_expected = first_expected[0: insertion] + first_new_one.chromosome[0: 3] + first_expected[
                                                                                         insertion: LENGTH]
        """mutations"""
        first_expected[1], first_expected[3] = first_expected[3], first_expected[1]
        first_expected[2], first_expected[1] = first_expected[1], first_expected[2]
        """"""
        second_new_one = self.stable_one.generate_individual()
        second_expected = deepcopy(self.stable_one.chromosome)
        insertion = second_expected.index(second_new_one.chromosome[2])
        for gen in second_new_one.chromosome[2: 4]:
            second_expected.remove(gen)
        second_expected = second_expected[0: insertion] + second_new_one.chromosome[2: 4] + second_expected[
                                                                                            insertion: LENGTH]
        self.std_test_crossover(first_expected, second_expected, first_new_one, second_new_one)

    def test_get_allele(self):
        self.std_test_get_allele("town2")

    def test_fitness(self):
        self.individual.chromosome = [A, B, C, D, E]
        self.stable_one.chromosome = [E, D, C, B, A]
        expected = - sum([EDGES[i][-1]['weight'] for i in [0, 4, 7, 9]])
        self.assertEqual(expected, self.individual.fitness(), "Wrong fitness")
        self.assertEqual(expected, self.stable_one.fitness(), "Wrong fitness")
        self.individual.chromosome = [A, C, E, D, B]
        expected = - sum([EDGES[i][-1]['weight'] for i in [1, 5, 8, 9]])
        self.assertEqual(expected, self.individual.fitness(), "Wrong fitness")


if __name__ == '__main__':
    main()
