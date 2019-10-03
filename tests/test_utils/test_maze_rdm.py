"""test_maze_rdm.py: Unittest of Maze"""

import numpy as np
from unittest import TestCase, main
from utils.simulations import Maze, UP, DOWN, RIGHT, Move

SIZE = 20
LONG_NUMBER = 11  # must be odd
EPSILON = 1e-10


class MazeTest(TestCase):

    def setUp(self) -> None:
        """
        Sets up unit test

        :return: None
        """
        self.non_maze = Maze(SIZE)
        self.non_maze.generate()
        self.maze = Maze(SIZE)
        self.robot = []
        return

    def _test_nothing_generated(self):
        self.assertFalse(self.maze.is_generated(), "Maze was generated")
        self.assertFalse(self.maze.has_robot(), "It has a robot")
        self.assertTrue((self.maze.start == self.maze.exit).all(), "Start and exit generated")

    def test_initialization(self):
        self._test_nothing_generated()

    def test_reset(self):
        self.maze.generate()
        self.maze.reset()
        self._test_nothing_generated()
        self.maze.generate()
        self.maze.enter_robot(self.robot)
        self.maze.reset()
        self._test_nothing_generated()

    def test_exceptions(self):
        self.assertRaises(AttributeError, self.maze.long_of_path)
        self.assertRaises(AttributeError, self.maze.found_exit)
        self.maze.enter_robot(self.robot)
        self.assertRaises(AttributeError, self.maze.long_of_path)
        self.assertRaises(AttributeError, self.maze.found_exit)

    def test_long_of_path(self):
        toy_maze = self._tester_maze()
        toy_maze.enter_robot(self._tester_robot_out())
        right_path = toy_maze.long_of_path()
        self.assertEqual(10, right_path, "Right path miscalculated")
        toy_maze.enter_robot(self._tester_robot_wrong())
        wrong_path = toy_maze.long_of_path()
        self.assertEqual(11, wrong_path, "Wrong path miscalculated")

    def test_found_exit(self):
        toy_maze = self._tester_maze()
        toy_maze.enter_robot(self._tester_robot_out())
        self.assertTrue(toy_maze.found_exit(), "Not found")
        toy_maze.enter_robot(self._tester_robot_wrong())
        self.assertFalse(toy_maze.found_exit(), "Found")

    # Static method
    def test_get_start_and_exit(self):
        actual_start, actual_exit = Maze._get_start_and_exit(SIZE)
        self.assertIn(1, actual_start, "Start not on up or left wall")
        self.assertGreaterEqual(SIZE * 2, actual_start[0], "First coordinate of start outside maze")
        self.assertGreaterEqual(SIZE * 2, actual_start[1], "Second coordinate of start outside maze")
        self.assertIn(SIZE * 2 - 1, actual_exit, "End not on down or right wall")
        self.assertGreaterEqual(SIZE * 2, actual_exit[0], "First coordinate of exit outside maze")
        self.assertGreaterEqual(SIZE * 2, actual_exit[1], "Second coordinate of exit outside maze")

    def test_generate_border(self):
        mini_size = 5
        blank = np.zeros((mini_size, mini_size))
        with_borders = Maze._generate_border(blank)
        wall_weight = mini_size * 4
        self.assertLessEqual(abs(wall_weight - sum(with_borders[0])), EPSILON, "Not border on up wall")
        self.assertLessEqual(abs(wall_weight - sum(with_borders[mini_size - 1])), EPSILON, "Not border on down wall")
        self.assertLessEqual(abs(wall_weight - sum(with_borders[..., 0])), EPSILON, "Not border on left wall")
        self.assertLessEqual(abs(wall_weight - sum(with_borders[..., mini_size - 1])), EPSILON,
                             "Not border on right wall")

    def test_recursion(self):
        a_maze = np.zeros((1, 1))
        self._std_recursion(a_maze, a_maze)
        a_maze = np.zeros((1, LONG_NUMBER))
        self._std_recursion(a_maze, a_maze)
        a_maze = np.zeros((3, 3))
        self._std_recursion(a_maze, 2 * 4)
        a_maze = np.zeros((LONG_NUMBER, 3))
        self._std_recursion(a_maze, (LONG_NUMBER - 1) * 4)
        a_maze = np.zeros((5, 5))
        self._std_recursion(a_maze, (5 * 2 - 4 + 2) * 4)
        a_maze = np.zeros((5, LONG_NUMBER))
        self._std_recursion(a_maze, (5 + LONG_NUMBER - 4 + LONG_NUMBER - 1) * 4)

    def test_length(self):
        self.assertEqual(SIZE, len(self.maze), "Wrong len")

    def _std_recursion(self, input_maze: np.ndarray, expected: np.ndarray or int):
        actual = Maze._recursion(input_maze)
        if type(expected) is int:
            self.assertLessEqual(actual.sum(), expected, "Wrong walls generated")
        else:
            self.assertTrue((expected == actual).all(), "Wrong conversion of maze")

    @staticmethod
    def _tester_maze() -> Maze:
        _toy_maze = Maze(5)
        _toy_maze._maze = Maze._generate_border(_toy_maze._maze)
        _toy_maze._maze[..., 2], _toy_maze._maze[..., 4], _toy_maze._maze[..., 6] = 4, 4, 4
        _toy_maze._maze[9, 2], _toy_maze._maze[9, 4], _toy_maze._maze[9, 6] = 0, 0, 0
        _toy_maze._maze[8, 3], _toy_maze._maze[8, 7:10] = 4, 4
        _toy_maze.start, _toy_maze.exit = np.array((1, 1)), np.array((9, 9))
        _toy_maze._start, _toy_maze._exit = np.array((0, 1)), np.array((9, 10))
        _toy_maze._maze[0, 1], _toy_maze._maze[9, 10] = 2, 2
        return _toy_maze

    @staticmethod
    def _tester_robot_out() -> [Move]:
        return [DOWN] * 5 + [RIGHT] * 20

    @staticmethod
    def _tester_robot_wrong() -> [Move]:
        return [DOWN] * 5 + [RIGHT] * 2 + [UP] * 18


if __name__ == '__main__':
    main()
