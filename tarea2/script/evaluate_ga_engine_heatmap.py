"""evaluate_ga_engine_heatmap.py: show and evaluate a genetic algorithm to predict a single word"""
import logging
import math
import numpy as np
import matplotlib.pyplot as plt
from random import seed
from genetic_algorithm import GAEngine, WordGuesser
from utils.results import show_matrix


WORD_TO_GUESS = "algorithm"
SCORE = len(WORD_TO_GUESS)
POPULATION_SIZE = [10, 50, 100, 300, 500, 1000]
MUTATION_RATE = [0, 0.1, 0.2, 0.3, 0.4]

seed(math.log(2))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    _, ax = plt.subplots(figsize=(12, 13))
    matrix = list()
    for size in POPULATION_SIZE:
        logging.info("Population size used: {}".format(size))
        generations = list()
        for m_rate in MUTATION_RATE:
            logging.info("==> Mutation rate used: {}".format(m_rate))
            environment = GAEngine(WordGuesser(m_rate, WORD_TO_GUESS))
            result = environment.run_genetic_algorithm(SCORE, size)
            generations.append(result.get_generations()[-1])
        matrix.append(generations.copy())
    matrix = np.array(matrix)
    mut = MUTATION_RATE.copy()
    mut[0] = "Mutation rate: {}".format(mut[0])
    pop = POPULATION_SIZE.copy()
    pop[0] = "Population\nsize:\n{}".format(pop[0])
    show_matrix(ax, matrix, (mut, pop), "Word guesser (word: algorithm)\n", 20, 25, color_map="Reds")
    plt.savefig("../results/algorithm_heatmap.png")
