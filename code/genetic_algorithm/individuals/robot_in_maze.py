"""robot_in_maze.py: RobotInMaze class"""

from math import sqrt
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
        self._maze = maze
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
        self._maze.enter_robot(self.chromosome)

    def _length(self) -> float:
        return self._maze.long_of_path()

    def _exit(self) -> float:
        dist = (self._maze.location - self._maze.exit) // 2
        return sqrt(dist[0]**2 + dist[1]**2)

    def graph(self, ax: Axes):
        self._maze.graph(ax)
        return None


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    a_maze = Maze(25)
    a_maze.generate()
    a_robot = RobotInMaze(0.0, a_maze)
    print(a_robot.chromosome)
    print(a_robot.fitness())
    print(a_robot.multi_fitness)
    print(a_robot.my_fitness)
    _, ax = plt.subplots()
    a_robot.graph(ax)
    plt.show()
