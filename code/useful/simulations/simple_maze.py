"""simple_maze.py; Maze class with a few obstacle"""

import numpy as np
from random import randint, choice
from matplotlib.colors import ListedColormap
from useful.simulations import Maze

EPSILON = 1e-10
LEVELS = {
    "easy": 0.01,
    "medium": 0.1,
    "hard": 0.4
}


class SimpleMaze(Maze):
    """
    Simple Maze Class, same as a Maze, but walls are just a few obstacle
    """
    def __init__(self, size: int, obstacles: float or str):
        super().__init__(size)
        if type(obstacles) == str:
            try:
                obstacles = LEVELS[obstacles]
            except KeyError:
                raise KeyError("There is no level named {}, available are: easy, medium and hard".format(obstacles))
        if obstacles > 1.0 or obstacles < 0.0:
            raise ValueError(
                "Obstacle is a percentage and allow a value between 0 and 1 (not recommended). "
                "Given value: {}".format(obstacles)
            )
        self.obstacles = ((size - 1) * (3 * size - 1)) * obstacles

    def generate(self) -> None:
        """
        Generate the maze adding obstacles for it

        :return: None
        """
        self._maze = self._generate_border(self._maze)
        self._maze[1:-1, 1:-1] = self._generate_obstacles(self._maze[1:-1, 1:-1])
        self._generate_doors()
        return

    def _generate_obstacles(self, maze: np.ndarray) -> np.ndarray:
        """
        Generates obstacles on maze
        This replace the recursion method

        :maze: Maze without borders
        :return: Maze with walls and opens added
        """
        if not abs(maze.sum()) <= EPSILON:
            raise ValueError("Not empty maze passed")
        out_maze = maze.copy()
        candidates = list()
        for x in range(0, out_maze.shape[0], 2):
            for y in range(1, out_maze.shape[0], 2):
                candidates.append((x, y))
            if x + 1 >= out_maze.shape[0]:
                pass
            else:
                for y in range(0, out_maze.shape[0]):
                    candidates.append((x + 1, y))
        for _ in range(int(self.obstacles)):
            token = randint(0, len(candidates) - 1)
            out_maze[candidates.pop(token)] = 4.0
        return out_maze


if __name__ == '__main__':
    SimpleMaze(4, 1.1)