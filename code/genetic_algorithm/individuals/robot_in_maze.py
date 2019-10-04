"""robot_in_maze.py: RobotInMaze class"""

import logging
from math import sqrt
from copy import deepcopy
from random import choices, uniform, choice
from matplotlib.axes import Axes
from genetic_algorithm.individuals import MultiObjectiveIndividual, Individual
from utils.simulations import Maze, UP, DOWN, LEFT, RIGHT, Move


class RobotInMaze(MultiObjectiveIndividual):
    """
    Simulate a Robot walking on a maze
    """

    def __init__(self, mutation_rate: float, maze: Maze):
        super(RobotInMaze, self).__init__([self._exit, self._length], mutation_rate)
        if not maze.is_generated():
            raise InterruptedError("Cannot initialize Robot if Maze is not generated")
        self._maze = deepcopy(maze)
        self._run = False
        self.chromosome = choices([UP, DOWN, LEFT, RIGHT], k=len(self._maze)**2 + 1)
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
        for fitness_func in self.fitness_function:
            self.multi_fitness.append(fitness_func())
        self.my_fitness = min(self.multi_fitness)
        return self.my_fitness

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

    def _length(self) -> float:
        return - self._maze.long_of_path()

    def _exit(self) -> float:
        dist = (self._maze.location - self._maze.exit) // 2
        return - sqrt(dist[0]**2 + dist[1]**2)

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


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from test_utils import tester_maze, tester_robot_wrong, tester_robot_wrong_closer
    a_maze = tester_maze()
    a_robot = RobotInMaze(0.0, a_maze)
    b_robot = a_robot.generate_individual()
    a_robot.chromosome = tester_robot_wrong()
    b_robot.chromosome = tester_robot_wrong_closer()
    a_robot.fitness()
    b_robot.fitness()
    _, ax = plt.subplots()
    a_robot.graph(ax)
    print(a_robot.multi_fitness)
    print(a_robot._maze.location)
    print(b_robot._maze.location)
    plt.show()
    _, ax = plt.subplots()
    b_robot.graph(ax)
    print(b_robot.multi_fitness)
    plt.show()
