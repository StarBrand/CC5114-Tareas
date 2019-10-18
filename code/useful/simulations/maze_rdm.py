"""maze_rdm.py; Maze class with recursive division method as algorithm"""

import logging
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
from random import randint, choice, choices, sample
from matplotlib.axes import Axes
from matplotlib.colors import ListedColormap
from utils.simulations import Move, UP, DOWN, LEFT, RIGHT

EPSILON = 1e-10
COLORMAP_MAZE = ListedColormap(['w', 'y', 'r', 'g', 'k'])


class Maze:
    """
    Maze Class, recursive division method as generator algorithm
    """
    def __init__(self, size: int):
        self.size = 2 * size + 1
        self._robot = []
        self._found_it = False
        self._long = 0
        self._maze = np.zeros((self.size, self.size))
        self.start, self.exit = np.array((0, 0), dtype='int'), np.array((0, 0), dtype='int')
        self._start, self._exit = np.array((0, 0), dtype='int'), np.array((0, 0), dtype='int')
        self.location = deepcopy(self._start)

    def generate(self) -> None:
        """
        Generate the maze using Recursive Division Method

        :return: None
        """
        self._maze = self._generate_border(self._maze)
        self._maze[1:-1, 1:-1] = self._recursion(self._maze[1:-1, 1:-1])
        self.start, self.exit = self._get_start_and_exit(len(self))
        if self.start[0] <= 1:
            self._start = self.start - (1, 0)
        else:
            self._start = self.start - (0, 1)
        if self.exit[0] >= self.size - 2:
            self._exit = self.exit + (1, 0)
        else:
            self._exit = self.exit + (0, 1)
        self._maze[self._start[0], self._start[1]] = 2
        self._maze[self._exit[0], self._exit[1]] = 2
        return

    def has_robot(self) -> bool:
        """
        Gets if there is a robot on the maze

        :return: Whether maze has a robot
        """
        return len(self._robot) > 0

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

        :return: None, axes given is changed
        """
        if not self.is_generated():
            logging.warning("Maze not generated, is going to plot a blank square")
        if not self.has_robot():
            logging.info("Maze without robot on it")
        ax.matshow(self._maze, cmap=COLORMAP_MAZE)
        return

    def enter_robot(self, direction: [Move]) -> None:
        """
        Put a robot in maze

        :param direction: Direction of the Robot to put in this maze
        :return: None
        """
        self._robot = deepcopy(direction)
        self._long = 0
        self._found_it = False
        self._long = self._run_robot()
        return

    def long_of_path(self) -> int:
        """
        Calculate the length of path of the robot in the maze

        :raise: AttributeError: in case there is no robot to walk the maze
        :return: Length of path
        """
        if not self.has_robot() or not self.is_generated():
            raise AttributeError("No robot in maze to walk in maze")
        return self._long

    def found_exit(self) -> bool:
        """
        Return whether robot found the exit of the maze

        :raise: AttributeError: in case there is no robot to walk the maze
        :return: whether robot found the exit
        """
        if not self.has_robot() or not self.is_generated():
            raise AttributeError("No robot in maze to found an exit")
        return self._found_it

    def _run_robot(self) -> int:
        out = 0
        try:
            move = self._robot[0]
        except IndexError:
            return out
        self.location = deepcopy(self._start)
        if self._is_a_wall(self.location + move.step()):
            self.location = deepcopy(self.start)
            return out
        out += 1
        self._maze[self._start[0], self._start[1]] += 1
        self._maze[self.start[0], self.start[1]] = 1
        self.location = deepcopy(self.start)
        for move in self._robot[1: len(self._robot)]:
            transition = self.location + move.step()
            if (self.location == self.exit).all():
                if (self._exit == transition).all():
                    self._maze[self._exit[0], self._exit[1]] += 1
                    self._found_it = True
                    return out + 1
                elif self._is_a_wall(transition):
                    return out
                else:
                    self._maze[transition[0], transition[1]] = 1
                    self.location = move + self.location
                    self._maze[self.location[0], self.location[1]] = 1
                    out += 1
            elif not self._is_a_wall(transition):
                self._maze[transition[0], transition[1]] = 1
                self.location = move + self.location
                self._maze[self.location[0], self.location[1]] = 1
                out += 1
            else:
                return out
        return out

    def _is_a_wall(self, location: np.ndarray) -> bool:
        if (location <= (0, 0)).any():
            """outside maze"""
            return True
        elif (location >= (self.size, self.size)).any():
            """outside maze"""
            return True
        elif self._maze[location[0], location[1]] >= 4:
            """wall"""
            return True
        else:
            """blank square"""
            return False

    def reset(self) -> None:
        """
        Reset maze and delete robot

        :return: None
        """
        self._robot = []
        self._found_it = False
        self._long = 0
        self._maze = np.zeros((self.size, self.size))
        self.start, self.exit = np.array((0, 0), dtype='int'), np.array((0, 0), dtype='int')
        self._start, self._exit = np.array((0, 0), dtype='int'), np.array((0, 0), dtype='int')
        self.location = deepcopy(self._start)
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
        return np.array(choice([(1, x), (x, 1)])), np.array(choice([(last, y), (y, last)]))

    @staticmethod
    def _generate_border(maze: np.ndarray) -> np.ndarray:
        """
        Copy maze with border

        :param maze: A maze
        :return: Maze with border (ones)
        """
        maze[0], maze[-1] = 4, 4
        maze[..., 0], maze[..., -1] = 4, 4
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
                maze[..., 1] = 4
                maze[an_open, 1] = 0
            else:
                maze[1] = 4
                maze[1, an_open] = 0
        elif min(maze.shape) == 3:
            an_open = choice(range(0, max(maze.shape), 2))
            if maze.shape.index(3):
                maze[..., 1] = 4
                maze[an_open, 1] = 0
            else:
                maze[1] = 4
                maze[1, an_open] = 0
        else:
            size_x, size_y = maze.shape
            x_wall = choice(range(1, size_x, 2))
            y_wall = choice(range(1, size_y, 2))
            maze[x_wall], maze[..., y_wall] = 4, 4
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
