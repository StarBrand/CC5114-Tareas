"""moves.py: Moves of robot in maze"""

import numpy as np


class Move:
    """
    Move class to simulate moves on maze
    """
    def __init__(self, x: int, y: int, name: str):
        self._move = np.array((x, y), dtype='int')
        self._name = name

    def step(self) -> np.ndarray:
        """
        Return the step of the move (to make sure there is no wall)

        :return: Step
        """
        return self._move // 2

    def __add__(self, location: np.ndarray) -> np.ndarray:
        return location + self._move

    def __radd__(self, location: np.ndarray) -> np.ndarray:
        return location + self._move

    def __repr__(self):
        return self._name

    def __str__(self):
        return self._name


UP = Move(-2, 0, "UP")
DOWN = Move(2, 0, "DOWN")
LEFT = Move(0, -2, "LEFT")
RIGHT = Move(0, 2, "RIGHT")
