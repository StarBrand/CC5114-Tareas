"""toy_maze.py: Generate ToyMaze and ToyRobots for testing test"""

import numpy as np
from utils.simulations import Maze, Move, DOWN, RIGHT, UP


def tester_maze() -> Maze:
    """
    A little maze to test path of robot

    :return: Toy Maze
    """
    toy_maze = Maze(5)
    toy_maze._maze = Maze._generate_border(toy_maze._maze)
    toy_maze._maze[..., 2], toy_maze._maze[..., 4], toy_maze._maze[..., 6] = 4, 4, 4
    toy_maze._maze[9, 2], toy_maze._maze[9, 4], toy_maze._maze[9, 6] = 0, 0, 0
    toy_maze._maze[8, 3], toy_maze._maze[8, 7:10] = 4, 4
    toy_maze.start, toy_maze.exit = np.array((1, 1)), np.array((9, 9))
    toy_maze._start, toy_maze._exit = np.array((0, 1)), np.array((9, 10))
    toy_maze._maze[0, 1], toy_maze._maze[9, 10] = 2, 2
    return toy_maze


def tester_robot_out() -> [Move]:
    """
    Generate directions for testing

    :return: Directions that found exit of Maze
    """
    return [DOWN] * 5 + [RIGHT] * 20


def tester_robot_wrong() -> [Move]:
    """
    Generate directions for testing

    :return: Directions that failed
    """
    return [DOWN] * 5 + [RIGHT] * 2 + [UP] * 18


def tester_robot_wrong_closer() -> [Move]:
    """
    Generate directions for testing

    :return: Directions that failed, but end closer
    """
    return [DOWN] * 5 + [RIGHT] * 2 + [UP] * 4 + [DOWN] * 14
