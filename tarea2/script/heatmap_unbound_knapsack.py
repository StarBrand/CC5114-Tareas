"""heatmap_unbound_knapsack.py: show and evaluate a genetic algorithm of the unbound knapsack problem
at different mutation rate and population size"""

import numpy as np
import logging
import matplotlib.pyplot as plt
from random import seed
from genetic_algorithm import GAEOptimized, Optimization
from genetic_algorithm.individuals import UnboundKnapsack
from useful.results import show_matrix

POPULATION_SIZE = list(range(50, 501, 50))
MUTATION_RATE = [0, 0.01, 0.05, 0.1, 0.15, 0.2, 0.3, 0.5, 0.7, 1.0]
EQUILIBRIUM = 10

seed(5)
fig = plt.figure(figsize=(36, 13))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    ax1 = fig.add_subplot(131)
    ax2 = fig.add_subplot(132)
    ax3 = fig.add_subplot(133)

    matrix1 = list()
    matrix2 = list()
    matrix3 = list()

    for size in POPULATION_SIZE:
        logging.info("Population size used: {}".format(size))
        generations = list()
        result = None
        wights = list()
        values = list()
        for m_rate in MUTATION_RATE:
            logging.info("==> Mutation rate used: {}".format(m_rate))
            environment = GAEOptimized(UnboundKnapsack(m_rate), optimization=Optimization.PRIORITY)
            result = environment.run_to_equilibrium(size, EQUILIBRIUM)
            generations.append(result.get_generations()[-1])
            wights.append(result.individual.multi_fitness[0])
            values.append(result.individual.multi_fitness[1])
        matrix1.append(generations.copy())
        matrix2.append(wights)
        matrix3.append(values)

    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)
    matrix3 = np.array(matrix3)
    pop = [50, 150, 250, 350, 450]
    mut = [0, 0.05, 0.15, 0.3, 0.7]
    show_matrix(ax2, matrix2, (mut, pop), "Weight in knapsack\n", 20, 25, color_map="Blues")
    show_matrix(ax3, matrix3, (mut, pop), "Value in knapsack\n", 20, 25, color_map="Greens")

    mut[0] = "Mutation rate:\n{}".format(mut[0])
    pop[0] = "Population\nsize:\n{}".format(pop[0])
    show_matrix(ax1, matrix1, (mut, pop), "Number of iteration\n", 20, 25, color_map="Reds")

    plt.savefig("../results/algorithm_heatmap_multi_obj.png")
