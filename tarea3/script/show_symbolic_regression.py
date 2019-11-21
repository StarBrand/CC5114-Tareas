"""show_symbolic_regression.py: show a genetic programming solution of look for equation"""

import logging
import matplotlib.pyplot as plt
from random import seed
from argparse import ArgumentParser
from genetic_algorithm import GAEngine
from genetic_programming import EquationGuesser

DEPTH = 2
PROB_TERMINAL = 0.03
VALUES = list(range(-10, 10 + 1))
MUTATION_RATE = 0.05
POPULATION_SIZE = 50
ACCEPTABLE = 0.1
FOR_EVALUATE = list(range(-100, 101))


def expected_function(x: float) -> float:
    """
    Function to guess

    :param x: value
    :return: result
    """
    return x**2 + x - 6


EXPECTED = expected_function
seed(5)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    parser = ArgumentParser()
    parser.add_argument("-d", "--divide", default=False, action="store_true",
                        help="Allow divide")

    args = parser.parse_args()

    extra = ""
    if args.divide:
        extra = "(div)"

    ast = EquationGuesser(EXPECTED, VALUES, float, PROB_TERMINAL, DEPTH, MUTATION_RATE, division=args.divide)
    environment = GAEngine(ast)
    result = environment.run_to_reach(0, ACCEPTABLE, POPULATION_SIZE, log=True, values=FOR_EVALUATE)

    _, ax = plt.subplots(figsize=(12, 12))

    ax.set_title("Symbolic Regression {}".format(extra), fontsize=25)
    ax.set_xlabel("\nGeneration", fontsize=20)
    ax.set_ylabel("Score\n", fontsize=20)
    ax.tick_params(labelsize=20)
    ax.grid()

    ax.plot(result.get_generations(), result.get_max_scores(), "-*", label="Maximum score")
    ax.plot(result.get_generations(), result.get_mean_scores(), "-*", label="Mean score")
    ax.plot(result.get_generations(), result.get_min_scores(), "-*", label="Minimum score")

    ax.set_yscale("symlog")
    ax.legend(fontsize=20)

    logging.info("Maximum value: {}".format(result.get_max_scores()[-1]))

    plt.savefig("../results/symbolic_regression{}.png".format(extra))
