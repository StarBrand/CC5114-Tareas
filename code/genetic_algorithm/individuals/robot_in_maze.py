"""robot_in_maze.py: RobotInMaze class"""

import logging
from math import sqrt
from copy import deepcopy
from random import choices, uniform, choice
from matplotlib.axes import Axes
from genetic_algorithm.individuals import MultiObjectiveIndividual, Individual
from useful.simulations import Maze, UP, DOWN, LEFT, RIGHT, Move


def _length(maze: Maze) -> float:
    return - maze.long_of_path()


def _exit(maze: Maze) -> float:
    dist = (maze.location - maze.exit) // 2
    return - sqrt(dist[0] ** 2 + dist[1] ** 2)


def _get_move():
    return choice([UP, DOWN, LEFT, RIGHT])


class RobotInMaze(MultiObjectiveIndividual):
    """
    Simulate a Robot walking on a maze
    """

    def __init__(self, mutation_rate: float, maze: Maze):
        self._maze = deepcopy(maze)
        super().__init__([_exit, _length], _get_move, len(self._maze) ** 2 + 1, mutation_rate)
        if not maze.is_generated():
            raise InterruptedError("Cannot initialize Robot if Maze is not generated")
        self._run = False
        self.genes.append("Entry_step")
        for i in range(1, len(self) - 1):
            self.genes.append("step{}".format(i))
        self.genes.append("Last_step")

    def fitness(self) -> float:
        """
        Calculate fitness from every fitness function, register it and
        return the minimum of them

        :return: Min of fitness
        """
        self.multi_fitness = list()
        self._performance()
        for fitness_func in self._fitness_function:
            self.multi_fitness.append(fitness_func(self._maze))
        return super().fitness()

    def generate_individual(self) -> Individual:
        """
        Return a new instance of Robot in Maze
        
        :return: Robot In Maze, new chromosome, same maze and mutation rate
        """
        return RobotInMaze(self.mutation_rate, self._maze)

    def mutate(self) -> None:
        """
        Change one step

        :return: None, it changed chromosome
        """
        for index, _ in enumerate(self.chromosome):
            if uniform(0, 1) <= self.mutation_rate:
                self.chromosome[index] = choice([UP, DOWN, LEFT, RIGHT])
        return None

    def _performance(self) -> None:
        self._run = True
        self._maze.enter_robot(self.chromosome)

    def graph(self, ax: Axes):
        """
        Add graph of maze to Axes given

        :param ax: Matplotlib Axes
        :return: None, modified Axes
        """
        if not self._run:
            logging.warning("Robot has not enter the maze yet")
        self._maze.graph(ax)
        return None
