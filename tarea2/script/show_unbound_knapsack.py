"""show_unbound_knapsack.py: show and evaluate a genetic algorithm of the unbound knapsack problem"""

import logging
import matplotlib.pyplot as plt
from random import seed
from genetic_algorithm import GAEOptimized, Optimization
from genetic_algorithm.individuals import UnboundKnapsack

POPULATION_SIZE = 350
EQUILIBRIUM = 10
MUTATION_RATE = 0.01

seed(5)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    environment = GAEOptimized(UnboundKnapsack(MUTATION_RATE), Optimization.PRIORITY)
    result = environment.run_to_equilibrium(POPULATION_SIZE, EQUILIBRIUM, log=True)

    _, ax = plt.subplots(figsize=(12, 12))

    ax.plot(result.get_generations(), result.get_max_scores(), "-o", label="Maximum score")
    ax.plot(result.get_generations(), result.get_mean_scores(), "-o", label="Mean score")
    ax.plot(result.get_generations(), result.get_min_scores(), "-o", label="Minimum score")
    ax.set_title("Unbound backpack\n", fontsize=25)
    ax.set_xlabel("\nGeneration", fontsize=20)
    ax.set_ylabel("Maximum Score\n", fontsize=20)
    ax.tick_params(labelsize=20)
    ax.legend(fontsize=20)
    ax.grid()

    logging.info("Maximum value in knapsack: {}".format(result.get_max_scores()[-1]))
    logging.info("Weight of maximum knapsack: {}".format(result.individual.multi_fitness[0]))

    plt.savefig("../results/unbound_knapsack.png")
