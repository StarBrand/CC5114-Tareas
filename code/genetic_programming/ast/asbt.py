"""asbt.py: BinaryAST class, or Abstract Syntax BiTree"""

from random import choice, uniform
from genetic_programming.ast import AST
from genetic_programming.ast.nodes import BinaryNode, Node
from genetic_programming.ast.nodes import AddNode, SubNode, MultNode, MaxNode, TerminalNode

POSSIBLE_NODES = [AddNode, SubNode, MultNode, MaxNode]


def _diff(node: BinaryNode, expected: float) -> float:
    return - abs(node.evaluate() - expected)


class BinaryAST(AST):
    """
    BinaryAST class, it represents an Abstract Syntax Binary Tree
    with two or none child per nodes
    """

    def __init__(self, number_expected: float, depth: int, prob_terminal: float, mutation_rate: float,
                 values_allowed: [float] or None = None):
        self.values_allowed = values_allowed
        root = self.generate_tree(depth, prob_terminal)
        super().__init__(prob_terminal, mutation_rate, root, depth=depth)
        self._fitness_function = _diff
        self.number_expected = number_expected

    def generate_tree(self, depth: int, prob_terminal: float) -> Node:
        """
        Generate a binary tree

        :param depth: Maximum depth
        :param prob_terminal: Probability of every Node to be TerminalNode
        :return: A Node
        """
        values = self.values_allowed
        if self.values_allowed is None:
            values = list(range(-100, 100))

        def _generate_tree(d: int, p: float) -> Node:
            if d == 0 or uniform(0, 1) < p:
                return TerminalNode(choice(values))
            else:
                left = _generate_tree(d - 1, p)
                right = _generate_tree(d - 1, p)
                this = choice(POSSIBLE_NODES)
                return this(left, right)

        return _generate_tree(depth, prob_terminal)

    def generate_individual(self) -> AST:
        """
        Generate individual

        :return: BinaryAST
        """
        return BinaryAST(self.number_expected, self.depth, self.prob_terminal, self.mutation_rate,
                         values_allowed=self.values_allowed)

    def fitness(self) -> float:
        """
        Fitness

        :return: Fitness, difference
                 between expected number and result (or evaluate)
        """
        return super(AST, self).fitness(node=self.root, expected=self.number_expected)
