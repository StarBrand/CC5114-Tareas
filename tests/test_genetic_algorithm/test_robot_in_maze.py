"""test_robot_in_maze.py: Unittest of RobotInMaze class"""

from unittest import main
from random import seed
from math import sqrt
from genetic_algorithm.individuals import RobotInMaze
from test_genetic_algorithm import MultiIndividualTest
from test_utils import tester_maze, tester_robot_wrong, tester_robot_wrong_closer, tester_robot_out
from utils.simulations import LEFT, RIGHT, UP, Maze

EPSILON = 1e-10


class RobotInMazeTest(MultiIndividualTest):

    def setUp(self) -> None:
        """
        Sets up unit test
        """
        maze = tester_maze()
        self.chromosome_size = (len(maze) ** 2) + 1
        self.individual = RobotInMaze(0.1, maze)
        self.stable_one = RobotInMaze(0.0, maze)

    def test_exception_constructor(self):
        maze = Maze(5)
        self.assertRaises(InterruptedError, RobotInMaze, 0.0, maze)

    def test_constructor(self):
        self.std_test_constructor(self.chromosome_size, self.chromosome_size)

    def test_generate_individual(self):
        self.std_test_generate_individual(self.chromosome_size, self.chromosome_size)

    def test_crossover(self):
        seed(10)
        first_one = self.individual.generate_individual()
        first_expected = self.individual.chromosome[0: 21] + first_one.chromosome[21: self.chromosome_size]
        """mutate"""
        first_expected[6] = UP
        first_expected[9] = RIGHT
        """"""
        second_one = self.stable_one.generate_individual()
        second_expected = self.stable_one.chromosome[0: 20] + second_one.chromosome[20: self.chromosome_size]
        self.std_test_crossover(first_expected, second_expected, first_one, second_one)

    def test_get_allele(self):
        self.std_test_get_allele("step2")

    def test_fitness(self):
        self.expected_individuals()
        dist_individual = sqrt(4**2 + 2**2)
        dist_stable_one = sqrt(0**2 + 2**2)
        self.assertGreaterEqual(EPSILON, abs(self.individual.multi_fitness[0] + dist_individual),
                                "Wrong distance individual")
        self.assertGreaterEqual(EPSILON, abs(self.individual.multi_fitness[1] + 11), "Wrong path individual")
        self.assertGreaterEqual(EPSILON, abs(self.stable_one.multi_fitness[0] + dist_stable_one),
                                "Wrong distance stable one")
        self.assertGreaterEqual(EPSILON, abs(self.stable_one.multi_fitness[1] + 15), "Wrong path stable one")
        self.assertGreaterEqual(EPSILON, abs(self.individual.my_fitness + 11), "Wrong fitness individual")
        self.assertGreaterEqual(EPSILON, abs(self.stable_one.my_fitness + 15), "Wrong fitness stable one")

    def test_comparing(self):
        self.expected_individuals()
        self.std_test_greater_than(self.individual, self.stable_one, 0)
        self.std_test_greater_than(self.stable_one, self.individual, 2)
        robot_out = self.individual.generate_individual()
        robot_out.chromosome = tester_robot_out()
        robot_out.fitness()
        self.std_test_greater_than(robot_out, self.stable_one, 1)
        self.std_test_greater_than(robot_out, self.individual, 1)

    def expected_individuals(self):
        """
        Generate individual with known performance on Maze
        """
        self.individual.chromosome = tester_robot_wrong()
        self.stable_one.chromosome = tester_robot_wrong_closer()
        self.individual.fitness()
        self.stable_one.fitness()


if __name__ == '__main__':
    main()
