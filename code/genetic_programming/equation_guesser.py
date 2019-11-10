"""equation_guesser.py: EquationGuesser class"""

from genetic_programming.ast import AST
from genetic_programming.ast.nodes import AddNode, SubNode, MultNode, BinaryNode

OPERATIONS = [AddNode, SubNode, MultNode]


def _mean_diff(node: BinaryNode, equation: callable, values: list) -> float:
    actual = node.evaluate(values={"x": values})
    diff = list()
    for value, found in zip(values, actual):
        diff.append(abs(equation(value) - found))
    try:
        return - sum(diff) / len(diff)
    except ZeroDivisionError:
        raise ZeroDivisionError("Values must be given, a 0 length array was given")


class EquationGuesser(AST):
    """
    Equation Guesser class, to guess a given equation
    """
    def __init__(self, equation_to_guess: callable, values: [float] or None, variable_type: type, prob_terminal: float,
                 depth: int, mutation_rate: float):
        self.equation = equation_to_guess
        super().__init__(OPERATIONS, values, prob_terminal, mutation_rate, None, depth, variable_type=variable_type)
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
        return EquationGuesser(self.equation, self.allowed_values, self.variable_type, self.prob_terminal, self.depth, self.mutation_rate)
