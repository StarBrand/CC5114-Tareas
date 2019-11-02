"""show_DesChiffresEtDesLettres.py: show a genetic programming solution of this french game"""

import logging
from argparse import ArgumentParser
import matplotlib.pyplot as plt
from random import seed
from genetic_algorithm import GAEngine
from genetic_programming import BinaryAST, ChiffresYesNoVariant

DEPTH = 4
PROB_TERMINAL = 0.03
VALUES = [25, 7, 8, 100, 4, 2]
EXPECTED = 459

MUTATION_RATE = {
    "unbound": 0.05,
    "yes-or-no": 0.1
}

PROBLEMS = {
    "unbound": BinaryAST(EXPECTED, DEPTH, PROB_TERMINAL, MUTATION_RATE["unbound"], VALUES),
    "yes-or-no": ChiffresYesNoVariant(EXPECTED, VALUES, MUTATION_RATE["yes-or-no"])
}

POPULATION_SIZE = {
    "unbound": 50,
    "yes-or-no": 20
}

ACCEPTABLE = {
    "unbound": 0.0,
    "yes-or-no": 1.5
}

seed(5)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    parser = ArgumentParser()
    parser.add_argument("-w", "--what_kind", type=str, required=True,
                        help="What kind of game:\n"
                             "Available:\tunbound,\tyes-or-no")

    args = parser.parse_args()
    try:
        ast = PROBLEMS[args.what_kind]
        population_size = POPULATION_SIZE[args.what_kind]
        acceptable = ACCEPTABLE[args.what_kind]
    except KeyError:
        raise KeyError("{} problem is not an option, available: unbound and yes-or-no".format(args.what_knapsack))

    environment = GAEngine(ast)
    result = environment.run_to_reach(0, acceptable, population_size, log=True)

    _, ax = plt.subplots(figsize=(12, 12))

    title = "yes-or-no"
    if args.what_kind == "unbound":
        title = "Unbound"
    ax.set_title("Des Chiffres Et Des Lettres ({})\n".format(title), fontsize=25)
    ax.set_xlabel("\nGeneration", fontsize=20)
    ax.set_ylabel("Score\n", fontsize=20)
    ax.tick_params(labelsize=20)
    ax.grid()

    ax.plot(result.get_generations(), result.get_max_scores(), "-o", label="Maximum score")

    plt.savefig("../results/{}_d_c_e_d_l(max).png".format(args.what_kind))

    ax.plot(result.get_generations(), result.get_mean_scores(), "-o", label="Mean score")
    ax.plot(result.get_generations(), result.get_min_scores(), "-o", label="Minimum score")

    ax.set_yscale("symlog")
    ax.legend(fontsize=20)

    logging.info("Maximum value: {}".format(result.get_max_scores()[-1]))

    plt.savefig("../results/{}_d_c_e_d_l.png".format(args.what_kind))
