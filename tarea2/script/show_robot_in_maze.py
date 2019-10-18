"""show_robot_in_maze.py: show and evaluate a genetic algorithm of a robot in a maze"""

import logging
import matplotlib.pyplot as plt
from random import seed
from genetic_algorithm import GAEOptimized, Optimization
from genetic_algorithm.individuals import RobotInMaze
from useful.simulations import Maze

POPULATION_SIZE = 1000
EQUILIBRIUM = 20
MUTATION_RATE = 0.05
MAZE_SIZE = 20

seed(2)
fig = plt.figure(figsize=(20, 10))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    maze = Maze(MAZE_SIZE)
    maze.generate()

    environment = GAEOptimized(RobotInMaze(MUTATION_RATE, maze), Optimization.PRIORITY)
    result = environment.run_to_equilibrium(POPULATION_SIZE, EQUILIBRIUM, log=True)

    ax = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    ax.plot(result.get_generations(), result.get_scores(), "-")
    ax.set_title("Robot In Maze\n", fontsize=25)
    ax.set_xlabel("\nGeneration", fontsize=20)
    ax.set_ylabel("Maximum Score\n", fontsize=20)
    ax.grid()

    result.individual.fitness()
    result.individual.graph(ax2)

    plt.savefig("../results/robot_in_maze.png")
