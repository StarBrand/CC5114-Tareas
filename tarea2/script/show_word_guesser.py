"""show_word_guesser.py: show and evaluate a genetic algorithm to predict a single word"""
import logging
import math
import matplotlib.pyplot as plt
from random import seed
from genetic_algorithm import GAEngine, WordGuesser

WORD_TO_GUESS = "algorithm"
SCORE = len(WORD_TO_GUESS)
POPULATION_SIZE = 500
MUTATION_RATE = 0.3

seed(math.log(2))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info("Generate engine:")
    environment = GAEngine(WordGuesser(MUTATION_RATE, WORD_TO_GUESS))
    logging.info("Run algorithm:")
    result = environment.run_genetic_algorithm(SCORE, POPULATION_SIZE, log=True)
    _, ax = plt.subplots(figsize=(12, 12))
    ax.plot(result.get_generations(), result.get_scores(), "-o", label=WORD_TO_GUESS)
    ax.set_xlabel("\nGeneration", fontsize=20)
    ax.set_ylabel("Maximum Score\n", fontsize=20)
    ax.set_title("Guess 'algorithm'\n", fontsize=25)
    ax.legend(fontsize=20)
    ax.grid()
    plt.savefig("../results/word_guesser.png")

"""Results on execution:"""

"""
INFO:root:Generate engine:
INFO:root:Run algorithm:
INFO:root:Generation 1
INFO:root:Closed word: hqjbritgx
INFO:root:Generation 2
INFO:root:Closed word: afooischs
INFO:root:Generation 3
INFO:root:Closed word: avjonzchm
INFO:root:Generation 4
INFO:root:Closed word: ahmbritgx
INFO:root:Generation 5
INFO:root:Closed word: aygbrifhj
INFO:root:Generation 6
INFO:root:Closed word: aleositha
INFO:root:Generation 7
INFO:root:Closed word: jlgjrichm
INFO:root:Generation 8
INFO:root:Closed word: algizithm
INFO:root:Generation 9
INFO:root:Closed word: altlrithm
INFO:root:Generation 10
INFO:root:Closed word: aggwrithm
INFO:root:Generation 11
INFO:root:Closed word: algoritem
INFO:root:Generation 12
INFO:root:Closed word: algorinhm
INFO:root:Generation 13
INFO:root:Closed word: algorithz
INFO:root:Generation 14
INFO:root:Closed word: algorifhm
INFO:root:Generation 15
INFO:root:Closed word: algorinhm
INFO:root:Generation 16
INFO:root:Closed word: wlgorithm
INFO:root:Generation 17
INFO:root:Closed word: algorcthm
INFO:root:Generation 18
INFO:root:Closed word: algorithm

Process finished with exit code 0
"""
