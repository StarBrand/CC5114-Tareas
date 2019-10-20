"""show_robot_in_maze.py: show and evaluate a genetic algorithm of a robot in a maze"""

import logging
import matplotlib.pyplot as plt
from random import seed
from genetic_algorithm import GAEOptimized, Optimization
from genetic_algorithm.individuals import RobotInMaze
from useful.simulations import SimpleMaze

POPULATION_SIZE = 200
EQUILIBRIUM = 20
MUTATION_RATE = 0.05
MAZE_SIZE = 20

seed(2)
fig = plt.figure(figsize=(36, 24))
fig.subplots_adjust(wspace=0.3)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    maze = SimpleMaze(MAZE_SIZE, "medium")
    maze.generate()

    environment = GAEOptimized(RobotInMaze(MUTATION_RATE, maze), Optimization.PRIORITY)
    environment.initialize_population(POPULATION_SIZE)
    environment.evaluate_fitness(register=True)
    logging.info("First generation generated!")
    first_try = max(environment.population)

    first_one = None
    is_out = first_try.found_exit()

    while not is_out:
        logging.info("Found exit not found yet...")
        environment.next_generation(register=True)
        is_out = max(environment.population).found_exit()

    logging.info("Exit found!!")
    first_one = max(environment.population)
    first_one_generation = environment.generation
    logging.info("Robot: {}".format(first_one.chromosome))

    result = environment.run_to_equilibrium(POPULATION_SIZE, EQUILIBRIUM, log=True, use_prev=True)

    ax = fig.add_subplot(211)
    ax1 = fig.add_subplot(234)
    ax2 = fig.add_subplot(235)
    ax3 = fig.add_subplot(236)

    max_score_plot = ax.plot(result.get_generations(), result.get_max_scores(), "-", label="Maximum score")
    ax.plot(result.get_generations(), result.get_mean_scores(), "-", label="Average score")
    ax.plot(result.get_generations(), result.get_min_scores(), "-", label="Minimum score")
    ax.set_title("Robot In Maze\n", fontsize=50)
    ax.set_xlabel("Generation", fontsize=40)
    ax.set_ylabel("Score\n", fontsize=40)
    ax.tick_params(labelsize=30)

    last_one = result.individual
    last_one.fitness()

    logging.info("Found exit: {}".format(last_one.found_exit()))
    logging.info("Distance from exit: {}".format(last_one.multi_fitness[0]))

    first_try.graph(ax1)
    first_one.graph(ax2)
    last_one.graph(ax3)

    ax.plot(1, first_try.my_fitness, '*', label="First robot", color=max_score_plot[0].get_color(), markersize=25)
    ax.plot(first_one_generation, first_one.my_fitness, '*', label="First exit found",
            color=max_score_plot[0].get_color(), markersize=25)
    ax.plot(environment.generation, last_one.my_fitness, '*', label="Solution according to algorithm",
            color=max_score_plot[0].get_color(), markersize=25)

    ax1.set_xlabel("\nFirst maximum score robot", fontsize=40)
    ax2.set_xlabel("\nFirst robot that found and exit", fontsize=40)
    ax3.set_xlabel("\nRobot with best score", fontsize=40)

    ax1.tick_params(labelsize=10)
    ax2.tick_params(labelsize=10)
    ax3.tick_params(labelsize=10)

    ax.legend(fontsize=30)
    ax.grid()

    plt.savefig("../results/robot_in_maze.png")
