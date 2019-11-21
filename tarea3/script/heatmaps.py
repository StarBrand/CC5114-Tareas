"""heatmaps.py: Heatmaps of genetic programming problems"""

import logging
import matplotlib.pyplot as plt
from random import seed
from genetic_programming import EquationGuesser, BinaryAST, ChiffresYesNoVariant
from useful3 import generate_heatmap

DEPTH = 2
PROB_TERMINAL = 0.03
VALUES = list(range(-10, 10 + 1)) + ["x"]
MUTATION_RATE = [0.0, 0.05, 0.4, 0.75, 1.0]
POPULATION_SIZE = [5, 10, 50, 100, 150]
ALLOWED_VALUES = list(range(-10, 10 + 1, 5))


def expected_function(x: float) -> float:
    """
    Function to guess

    :param x: value
    :return: result
    """
    return x**2 - 2*x - 15


EXPECTED = expected_function


if __name__ == '__main__':

    problems = dict()

    problems["eq_guess"] = {
        "ast": EquationGuesser(EXPECTED, VALUES, float, PROB_TERMINAL, DEPTH, 0.0),
        "acceptable": 0.1,
        "name": "Equation Guesser",
        "file": "eq_guesser",
        "values": list(range(-100, 101))
    }

    problems["eq_guess_div"] = {
        "ast": EquationGuesser(EXPECTED, VALUES, float, PROB_TERMINAL, DEPTH, 0.0, division=True),
        "acceptable": 0.1,
        "name": "Equation Guesser Division",
        "file": "eq_guesser_div",
        "values": list(range(-100, 101))
    }

    problems["number"] = {
        "ast": BinaryAST(20, 4, PROB_TERMINAL, 0.0, ALLOWED_VALUES),
        "acceptable": 0.0,
        "name": "Number",
        "file": "n_guesser",
        "values": None
    }

    problems["number_01"] = {
        "ast": ChiffresYesNoVariant(20, [-10, -5, 5, 10], 0.0),
        "acceptable": 0.0,
        "name": "Number 0/1",
        "file": "n_guesser_01",
        "values": None
    }

    logging.basicConfig(level=logging.INFO)
    for key in problems.keys():
        seed(2)
        _, ax = plt.subplots(figsize=(12, 12))
        logging.info("Problem {}".format(problems[key]["name"]))
        generate_heatmap(ax, POPULATION_SIZE, MUTATION_RATE, problems[key]["ast"], problems[key]["acceptable"],
                         problems[key]["name"], problems[key]["file"], values=problems[key]["values"])
