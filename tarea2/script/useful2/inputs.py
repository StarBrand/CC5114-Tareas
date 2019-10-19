"""inputs.py: Inputs to test GAs"""

from networkx import Graph
from genetic_algorithm.individuals import Individual
from genetic_algorithm.individuals import WordGuesser, SentenceGuesser, BinaryCalculator, TravelPath

WORD_TO_GUESS = "algorithm"
LABEL = "The goal of having computers automatically \n" \
        "solve problems is central to artificial \n" \
        "intelligence"
SENTENCE_TO_GUESS = LABEL.replace("\n", "")
NUMBER = 200
BITS = 8
POPULATION_SIZE = {
    "word_guesser": 500,
    "sentence_guesser": 2000,
    "binary_calculator": 100,
    "travel_path": 50
}


def get_input(key: str, mutation_rate: float) -> (Individual, str, int, int):
    """
    Generate input

    :param key: Name of GAs
    :param mutation_rate: Mutation rate of individual
    :return: Individual for testing, label for graph, population size and score expected or equilibrium
    """
    if key == "word_guesser":
        return WordGuesser(mutation_rate, WORD_TO_GUESS), "Guess word: {}".format(WORD_TO_GUESS), POPULATION_SIZE[key],\
               len(WORD_TO_GUESS)
    elif key == "sentence_guesser":
        return SentenceGuesser(mutation_rate, SENTENCE_TO_GUESS), "Sentence: {}".format(LABEL),\
               POPULATION_SIZE[key], len(SENTENCE_TO_GUESS)
    elif key == "binary_calculator":
        return BinaryCalculator(mutation_rate, NUMBER, BITS), "Guess binary encoding: {}".format(NUMBER),\
               POPULATION_SIZE[key], 0
    elif key == "travel_path":
        return TravelPath(mutation_rate, _get_graph()), "Traveling Salesman Problem", POPULATION_SIZE[key], 100
    else:
        raise KeyError("Unexpected GA")


def _get_graph() -> Graph:
    g = Graph()
    nodes = list("abcdefghij")
    g.add_nodes_from(nodes)
    weights = [10, 10]
    edges = []
    for primary, node in enumerate(nodes):
        for secondary in range(primary):
            edges.append((node, nodes[secondary], {'weight': weights[-2]}))
            weights.append(weights[-2] + weights[-1])
    g.add_edges_from(edges)
    return g
