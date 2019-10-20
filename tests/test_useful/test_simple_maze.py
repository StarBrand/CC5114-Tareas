"""test_simple_maze.py: Unittest of Simple Maze"""

from unittest import TestCase, main
from useful.simulations import SimpleMaze
from useful.simulations.simple_maze import LEVELS, EPSILON

SIZE = 20
OBSTACLES = (SIZE - 1) * (3 * SIZE - 1)


class MazeTest(TestCase):

    def setUp(self) -> None:
        """
        Sets up unit test

        :return: None
        """
        self.easy_maze = SimpleMaze(SIZE, "easy")
        self.medium_maze = SimpleMaze(SIZE, "medium")
        self.hard_maze = SimpleMaze(SIZE, "hard")
        self.robot = []
        return

    def test_init(self):
        self.assertGreaterEqual(EPSILON, abs(OBSTACLES * LEVELS["easy"] - self.easy_maze.obstacles),
                                "Wrong number of obstacles (easy)")
        self.assertGreaterEqual(EPSILON, abs(OBSTACLES * LEVELS["medium"] - self.medium_maze.obstacles),
                                "Wrong number of obstacles (medium)")
        self.assertGreaterEqual(EPSILON, abs(OBSTACLES * LEVELS["hard"] - self.hard_maze.obstacles),
                                "Wrong number of obstacles (hard)")

    def test_obstacle(self):
        self.easy_maze.generate()
        self.medium_maze.generate()
        self.hard_maze.generate()
        self.std_test_obstacle(self.easy_maze, LEVELS["easy"])
        self.std_test_obstacle(self.medium_maze, LEVELS["medium"])
        self.std_test_obstacle(self.hard_maze, LEVELS["hard"])

    def std_test_obstacle(self, maze: SimpleMaze, percentage: float) -> None:
        """
        An standard for test number of obstacles

        :param maze: Maze generated to test
        :param percentage: Percentage of obstacles
        :return: Test number of obstacles on simple maze
        """
        # Walls
        walls = maze._maze.sum()
        # Borders
        borders = maze.size * 4 - 4  # Four times size plus the corners (counted twice)
        # Obstacles: all walls minus borders
        obstacles = walls - (4 * borders)  # Every wall is a 4
        obstacles += (2 + 2)  # start and exit are 2's so 2 each was over-counted
        obstacles //= 4  # number of obstacles instead of sum of values
        # Expected
        expected = OBSTACLES * percentage
        self.assertLessEqual(EPSILON, abs(obstacles - expected), "Obstacles generated miscalculated")

    def test_init_exceptions(self):
        self.assertRaises(KeyError, SimpleMaze, SIZE, "not-easy")
        self.assertRaises(ValueError, SimpleMaze, SIZE, - EPSILON)
        self.assertRaises(ValueError, SimpleMaze, SIZE, 1.0 + EPSILON)


if __name__ == '__main__':
    main()
