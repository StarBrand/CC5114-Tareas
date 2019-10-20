"""show_knapsack_problem.py: show and evaluate a genetic algorithm of the unbound (or 0-1) knapsack problem"""

import logging
from argparse import ArgumentParser
import matplotlib.pyplot as plt
from random import seed
from genetic_algorithm import GAEOptimized, Optimization
from genetic_algorithm.individuals import UnboundKnapsack

POPULATION_SIZE = 350
EQUILIBRIUM = 10
MUTATION_RATE = 0.01

PROBLEMS = {
    "unbound": UnboundKnapsack(MUTATION_RATE),
    "0-1": UnboundKnapsack(MUTATION_RATE)
}

seed(5)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    parser = ArgumentParser()
    parser.add_argument("-w", "--what_knapsack", type=str, required=True,
                        help="What kind of knapsack problem to use:\n"
                             "Available:\tunbound,\t0-1")

    args = parser.parse_args()
    try:
        knapsack = PROBLEMS[args.what_knapsack]
    except KeyError:
        raise KeyError("{} knapsack problem is not an option, available: unbound and 0-1")

    environment = GAEOptimized(knapsack, Optimization.PRIORITY)
    result = environment.run_to_equilibrium(POPULATION_SIZE, EQUILIBRIUM, log=True)

    _, ax = plt.subplots(figsize=(12, 12))

    ax.plot(result.get_generations(), result.get_max_scores(), "-o", label="Maximum score")
    ax.plot(result.get_generations(), result.get_mean_scores(), "-o", label="Mean score")
    ax.plot(result.get_generations(), result.get_min_scores(), "-o", label="Minimum score")
    title = "0-1"
    if args.what_knapsack == "unbound":
        title = "Unbound"
    ax.set_title("{} knapsack\n".format(title), fontsize=25)
    ax.set_xlabel("\nGeneration", fontsize=20)
    ax.set_ylabel("Score\n", fontsize=20)
    ax.tick_params(labelsize=20)
    ax.legend(fontsize=20)
    ax.grid()

    logging.info("Maximum value in knapsack: {}".format(result.get_max_scores()[-1]))
    logging.info("Weight of maximum knapsack: {}".format(result.individual.multi_fitness[0]))

    plt.savefig("../results/{}_knapsack.png".format(args.what_knapsack))
