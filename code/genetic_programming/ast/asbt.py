"""asbt.py: BinaryAST class, or Abstract Syntax BiTree"""

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
                 allowed_values: [float] or None = None):
        if allowed_values is None:
            allowed_values = list(range(-100, 100))
        super().__init__(POSSIBLE_NODES, allowed_values, prob_terminal, mutation_rate, depth=depth)
        self._fitness_function = _diff
        self.number_expected = number_expected

    def generate_individual(self) -> AST:
        """
        Generate individual

        :return: BinaryAST
        """
        return BinaryAST(self.number_expected, self.depth, self.prob_terminal, self.mutation_rate,
                         allowed_values=self.allowed_values)

    def fitness(self) -> float:
        """
        Fitness

        :return: Fitness, difference
                 between expected number and result (or evaluate)
        """
        return super(AST, self).fitness(node=self.root, expected=self.number_expected)
