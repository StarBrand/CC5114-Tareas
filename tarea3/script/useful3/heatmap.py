"""heatmap.py: generate a heatmap"""

import numpy as np
import logging
import matplotlib.pyplot as plt
from copy import deepcopy
from matplotlib.axes import Axes
from genetic_algorithm import GAEngine
from genetic_programming.ast import AST
from useful.results import show_matrix


def generate_heatmap(ax: Axes, population_size: [int], mutation_rate: [float], ast: AST, acceptable: float,
                     name_of_problem: str, name_of_file: str, values: [float] = None) -> None:
    """
    Generate heatmap to compare performance in function of population size and mutation rate

    :param ax: An Axes
    :param population_size: Population sizes to use
    :param mutation_rate: Mutation rates to use
    :param ast: AST initialized
    :param acceptable: Acceptable difference to reach
    :param name_of_problem: Name of problem of heatmap generated
    :param name_of_file: Name of file
    :param values: (Optional) in case its needed
    :return: None, alter ax
    """
    logging.basicConfig(level=logging.INFO)

    matrix = list()

    for size in population_size:
        logging.info("Population size used: {}".format(size))
        generations = list()
        for m_rate in mutation_rate:
            logging.info("==> Mutation rate used: {}".format(m_rate))
            ast_to_be_used = deepcopy(ast)
            ast_to_be_used.mutation_rate = m_rate
            ast_to_be_used = ast_to_be_used.generate_individual()
            environment = GAEngine(ast_to_be_used)
            if values is not None:
                result = environment.run_to_reach(0, acceptable, size, values=values)
            else:
                result = environment.run_to_reach(0, acceptable, size)
            generations.append(result.get_generations()[-1])
        matrix.append(generations.copy())

    matrix = np.array(matrix)
    mut = mutation_rate.copy()
    pop = population_size.copy()
    mut[0] = "Mutation rate:\n{}".format(mut[0])
    pop[0] = "Population\nsize:\n{}".format(pop[0])
    show_matrix(ax, matrix, (mut, pop), "{}: Number of iteration\n".format(name_of_problem),
                20, 25, color_map="Reds")

    plt.savefig("../results/heatmap_{}.png".format(name_of_file))
