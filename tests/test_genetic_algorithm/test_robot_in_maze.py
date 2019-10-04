"""test_robot_in_maze.py: Unittest of RobotInMaze class"""

from unittest import main
from random import seed
from genetic_algorithm.individuals import RobotInMaze
from test_genetic_algorithm import MultiIndividualTest
from test_utils import tester_maze, tester_robot_out, tester_robot_wrong


class RobotInMazeTest(MultiIndividualTest):

    def setUp(self) -> None:
        """
        Sets up unit test
        """
        maze = tester_maze()
        self.chromosome_size = (len(maze) ** 2) + 1
        self.individual = RobotInMaze(0.3, maze)
        self.stable_one = RobotInMaze(0.0, maze)

    def test_constructor(self):
        self.std_test_constructor(self.chromosome_size, self.chromosome_size)

    def test_generate_individual(self):
        self.std_test_generate_individual(self.chromosome_size, self.chromosome_size)

    def test_crossover(self):
        seed(10)
        first_one = self.individual.generate_individual()
        first_expected = self.individual.chromosome[0: self.chromosome_size]
        second_one = self.stable_one.generate_individual()
        second_expected = self.stable_one.chromosome[0: self.chromosome_size]
        self.std_test_crossover(first_expected, second_expected, first_one, second_one)

    def test_get_allele(self):
        self.std_test_get_allele("step2")

    def test_fitness(self):
        self.expected_individuals()
        print(self.individual.multi_fitness)
        print(self.stable_one.multi_fitness)
        print(self.individual.my_fitness)
        print(self.stable_one.my_fitness)

    def test_comparing(self):
        self.expected_individuals()
        self.std_test_greater_than(self.individual, self.stable_one, 0)
        self.std_test_greater_than(self.individual, self.stable_one, 1)
        self.std_test_greater_than(self.individual, self.stable_one, 2)

    def expected_individuals(self):
        """
        Generate individual with known performance on Maze
        """
        self.individual.chromosome = tester_robot_out()
        self.stable_one.chromosome = tester_robot_wrong()
        self.individual.fitness()
        self.stable_one.fitness()


if __name__ == '__main__':
    main()
