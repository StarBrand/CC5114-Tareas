"""equation_guesser.py: EquationGuesser class"""

from math import isnan
from genetic_programming.ast import AST
from genetic_programming.ast.nodes import AddNode, SubNode, MultNode, BinaryNode, DivNode, Node

OPERATIONS = [AddNode, SubNode, MultNode]


def _mean_diff(node: BinaryNode, equation: callable, values: list) -> float:
    actual = node.evaluate(values={"x": values})
    diff = list()
    for value, found in zip(values, actual):
        try:
            expected = equation(value)
            if isnan(found):
                diff.append(float("Inf"))
            else:
                diff.append(abs(expected - found))
        except ZeroDivisionError:
            if isnan(found):
                diff.append(0)
            else:
                diff.append(abs(found))
    if len(diff) is not 0:
        return - sum(diff) / len(diff)
    else:
        raise ZeroDivisionError("Values must be given, a 0 length array was given")


class EquationGuesser(AST):
    """
    Equation Guesser class, to guess a given equation
    """
    def __init__(self, equation_to_guess: callable, values: [float] or None, variable_type: type, prob_terminal: float,
                 depth: int, mutation_rate: float, division: bool = False):
        self.equation = equation_to_guess
        operations = OPERATIONS
        if division:
            operations += [DivNode]
        super().__init__(operations, values, prob_terminal, mutation_rate, None, depth, variable_type=variable_type)
        self._fitness_function = _mean_diff

    def fitness(self, **kwargs) -> float:
        """
        Calculate, store and return fitness as the mean of difference between given and found

        :param kwargs: values to calculate function given and found
        :return: Mean of difference
        """
        try:
            values = kwargs["values"]
            return super(AST, self).fitness(node=self.root, equation=self.equation, values=values)
        except KeyError:
            raise KeyError("Values must be given to calculate fitness")

    def generate_individual(self) -> AST:
        """
        Generate and return an EquationGuesser

        :return: EquationGuesser with different node but same parameters
        """
        return EquationGuesser(self.equation, self.allowed_values, self.variable_type, self.prob_terminal, self.depth,
                               self.mutation_rate)

    def generate_tree(self, depth: int, prob_terminal: float) -> Node:
        """
        Generates tree adding variable "x" to allowed values

        :param depth: Depth of tree
        :param prob_terminal: Probability of been a terminal
        :return: A operation tree
        """
        self.allowed_values = self.allowed_values + ["x"]
        return super().generate_tree(depth, prob_terminal)
