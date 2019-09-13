"""evaluate_ga_engine_population.py: show and evaluate a genetic algorithm to predict a single word"""
import logging
import math
import matplotlib.pyplot as plt
from random import seed
from genetic_algorithm import GAEngine, WordGuesser

WORD_TO_GUESS = "algorithm"
SCORE = len(WORD_TO_GUESS)
POPULATION_SIZE = list(range(10, 100, 10)) + list(range(100, 1000, 100)) + [1000]
MUTATION_RATE = [0.0, 0.3, 0.5, 1.0]

seed(math.log(2))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    _, ax = plt.subplots(figsize=(12, 12))
    for m_rate in MUTATION_RATE:
        logging.info("Mutation rate used: {}".format(m_rate))
        generations = list()
        for size in POPULATION_SIZE:
            logging.info("==> Population size used: {}".format(size))
            environment = GAEngine(WordGuesser(m_rate, WORD_TO_GUESS))
            result = environment.run_genetic_algorithm(SCORE, size)
            generations.append(result.get_generations()[-1])
        ax.plot(POPULATION_SIZE, generations, label="Mut rate: {}".format(m_rate))
    ax.set_xlabel("\nPopulation", fontsize=20)
    ax.set_ylabel("Generations of run\n", fontsize=20)
    ax.set_title("Guess word on population\n", fontsize=25)
    ax.legend(fontsize=20)
    ax.grid()
    plt.savefig("../results/algorithm_vs_population.png")
