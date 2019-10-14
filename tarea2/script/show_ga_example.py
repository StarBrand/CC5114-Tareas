"""show_ga_example.py: show and evaluate a genetic algorithm"""
import logging
import math
import matplotlib.pyplot as plt
from argparse import ArgumentParser
from random import seed
from genetic_algorithm import GAEngine
from useful2 import get_input

TOURNAMENT_SIZE = 20
MUTATION_RATE = 0.3

seed(math.log(2))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    parser = ArgumentParser()
    parser.add_argument("-m", "--mutation_rate", default=MUTATION_RATE, type=float,
                        help="Mutation rate of individuals on algorithm")
    parser.add_argument("-s", "--tournament_size", default=TOURNAMENT_SIZE, type=int,
                        help="Size of tournament to select")
    parser.add_argument("-e", "--equilibrium", type=int,
                        help="Stop when equilibrium")
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument("-t", "--type", required=True, type=int,
                               help="Type of genetic algorithm to use\n"
                                    "Options:\n"
                                    "\t0: word guesser\n"
                                    "\t1: sentences guesser\n"
                                    "\t2: binary calculator\n"
                                    "\t3: traveling salesman problem")

    args = parser.parse_args()
    keys = {
        0: "word_guesser",
        1: "sentence_guesser",
        2: "binary_calculator",
        3: "travel_path"
    }

    try:
        key = keys[args.type]
    except KeyError:
        raise KeyError("{} is not a valid option. Available options: "
                       "0: word guesser, 1: sentences guesser, "
                       "2: binary calculator, 3: traveling salesman problem".format(args.type))

    individual, label, population, score = get_input(key, args.mutation_rate)

    logging.info("Generate engine:")
    environment = GAEngine(individual)
    logging.info("Run algorithm:")
    result = environment.run_genetic_algorithm(score, population, log=True, tournament_size=args.tournament_size,
                                               equilibrium=args.equilibrium)
    _, ax = plt.subplots(figsize=(12, 12))
    if key == "sentence_guesser":
        ax.plot(result.get_generations(), result.get_scores(), "-", label=label)
        ax.set_title("Guess sentence\n", fontsize=25)
        ax.legend(fontsize=20)
    else:
        ax.plot(result.get_generations(), result.get_scores(), "-o")
        ax.set_title("{}\n".format(label), fontsize=25)
    ax.set_xlabel("\nGeneration", fontsize=20)
    ax.set_ylabel("Maximum Score\n", fontsize=20)
    ax.grid()
    plt.savefig("../results/{}.png".format(key))