"""evaluate_ga_engine_mutation.py: show and evaluate a genetic algorithm to predict a single word"""
import logging
import math
import numpy as np
import matplotlib.pyplot as plt
from random import seed
from genetic_algorithm import GAEngine, WordGuesser

WORD_TO_GUESS = "algorithm"
SCORE = len(WORD_TO_GUESS)
POPULATION_SIZE = [10, 100, 300, 500]
MUTATION_RATE = list(np.arange(0, 1.05, 0.05))

seed(math.log(2))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    _, ax = plt.subplots(figsize=(12, 12))
    for size in POPULATION_SIZE:
        logging.info("Population size used: {}".format(size))
        generations = list()
        for m_rate in MUTATION_RATE:
            logging.info("==> Mutation rate used: {}".format(m_rate))
            environment = GAEngine(WordGuesser(m_rate, WORD_TO_GUESS))
            result = environment.run_genetic_algorithm(SCORE, size)
            generations.append(result.get_generations()[-1])
        ax.plot(MUTATION_RATE, generations, label="Population: {}".format(size))
    ax.set_xlabel("\nMutation rate", fontsize=20)
    ax.set_ylabel("Generations of run\n", fontsize=20)
    ax.set_title("Guess word on mutation rate\n", fontsize=25)
    ax.legend(fontsize=20)
    ax.grid()
    plt.savefig("../results/algorithm_vs_mutation.png")
