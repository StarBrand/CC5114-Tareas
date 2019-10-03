"""maze_rdm.py; Maze class with recursive division method as algorithm"""

import logging
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
from random import randint, choice, choices, sample
from matplotlib.axes import Axes
from genetic_algorithm.individuals import RobotInMaze

EPSILON = 1e-10


class Maze:
    """
    Maze Class, recursive division method as generator algorithm
    """
    def __init__(self, size: int):
        self.size = 2 * size + 1
        self._robot = None
        self._maze = np.zeros((self.size, self.size))
        self.start, self.exit = (0, 0), (0, 0)

    def generate(self) -> None:
        """
        Generate the maze using Recursive Division Method

        :return: None
        """
        self._maze = self._recursion(self._maze)
        return

    def has_robot(self) -> bool:
        """
        Gets if there is a robot on the maze

        :return: Whether maze has a robot
        """
        return self._robot is not None

    def is_generated(self) -> bool:
        """
        Return whether the maze was generated or not

        :return: Whether maze has walls
        """
        return not abs(self._maze.sum() - 0.0) <= EPSILON

    def graph(self, ax: Axes) -> None:
        """
        Plot the maze as a black and white numpy.ndarray
        In case there is a robot on it, plot its path as gray

        :param ax: Axes in which Maze will be plotted

        :return: None
        """
        return

    def enter_robot(self, robot: RobotInMaze) -> None:
        """
        Put a robot in maze

        :param robot: Robot to put in this maze
        :return: None
        """
        self._robot = robot
        return

    def long_of_path(self) -> int:
        """
        Calculate the length of path of the robot in the maze

        :raise: AttributeError: in case there is no robot to walk the maze
        :return: Length of path
        """
        if not self.has_robot() or not self.is_generated():
            raise AttributeError("No robot in maze to walk in maze")
        return 0

    def found_exit(self) -> bool:
        """
        Return whether robot found the exit of the maze

        :raise: AttributeError: in case there is no robot to walk the maze
        :return: whether robot found the exit
        """
        if not self.has_robot() or not self.is_generated():
            raise AttributeError("No robot in maze to found an exit")
        return False

    def reset(self) -> None:
        """
        Reset maze and delete robot

        :return: None
        """
        self._maze = np.zeros((self.size, self.size))
        self._robot = None
        self.start, self.exit = 0, 0
        return

    @staticmethod
    def _get_start_and_exit(size: int) -> ((int, int), (int, int)):
        """
        Coordinates of the start and the exit of maze

        :param size: Size of maze
        :return: Coordinates of start and exit
        """
        last = size * 2 - 1
        x, y = choices(range(1, size * 2, 2), k=2)
        return choice([(1, x), (x, 1)]), choice([(last, y), (y, last)])

    @staticmethod
    def _generate_border(maze: np.ndarray) -> np.ndarray:
        """
        Copy maze with border

        :param maze: A maze
        :return: Maze with border (ones)
        """
        maze[0], maze[-1] = 1, 1
        maze[..., 0], maze[..., -1] = 1, 1
        return deepcopy(maze)

    @staticmethod
    def _recursion(maze: np.ndarray) -> np.ndarray:
        """
        Recursion step of the generation of the maze

        :param maze: A maze
        :return: Maze with walls and opens added
        """
        if not abs(maze.sum()) <= EPSILON:
            raise ValueError("Not empty maze passed")
        if min(maze.shape) == 1:
            pass
        elif maze.shape == (3, 3):
            an_open = choice(range(0, 3, 2))
            if randint(0, 1):
                maze[..., 1] = 1
                maze[an_open, 1] = 0
            else:
                maze[1] = 1
                maze[1, an_open] = 0
        elif min(maze.shape) == 3:
            an_open = choice(range(0, max(maze.shape), 2))
            if maze.shape.index(3):
                maze[..., 1] = 1
                maze[an_open, 1] = 0
            else:
                maze[1] = 1
                maze[1, an_open] = 0
        else:
            size_x, size_y = maze.shape
            x_wall = choice(range(1, size_x, 2))
            y_wall = choice(range(1, size_y, 2))
            maze[x_wall], maze[..., y_wall] = 1, 1
            x_open1, x_open2 = Maze._open(size_y, y_wall)
            y_open1, y_open2 = Maze._open(size_x, x_wall)
            for an_open in sample([(x_wall, x_open1), (x_wall, x_open2),
                                   (y_open1, y_wall), (y_open2, y_wall)], k=3):
                maze[an_open] = 0
            maze[0:x_wall, 0:y_wall] = Maze._recursion(maze[0:x_wall, 0:y_wall])
            maze[0:x_wall, y_wall + 1:size_y] = Maze._recursion(maze[0:x_wall, y_wall + 1:size_y])
            maze[x_wall + 1:size_x, 0:y_wall] = Maze._recursion(maze[x_wall + 1:size_x, 0:y_wall])
            maze[x_wall + 1:size_x, y_wall + 1:size_y] = Maze._recursion(maze[x_wall + 1:size_x, y_wall + 1:size_y])
        return deepcopy(maze)

    @staticmethod
    def _open(size: int, wall: int) -> (int, int):
        return choice(range(0, wall, 2)), choice(range(wall + 1, size, 2))

    def __len__(self):
        return int((self.size - 1) / 2)


if __name__ == '__main__':
    a = Maze(10)
    a.generate()
    plt.matshow(a._maze)
    plt.show()
