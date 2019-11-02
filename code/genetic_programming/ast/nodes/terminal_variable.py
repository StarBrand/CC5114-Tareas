"""terminal_variable.py: TerminalVariable class"""

from genetic_programming.ast.nodes import TerminalNode


class TerminalVariable(TerminalNode):
    """
    Terminal that represents a variable
    """
    def __init__(self, variable: str, to_be_replaced_by: type):
        super().__init__(variable)
        self.type = to_be_replaced_by

    def evaluate(self, **kwargs) -> [float or bool]:
        """
        Evaluate with variables

        :param: **kwargs: values of variables
        :return: List of results
        """
        _, variables, values = self._receive_values(**kwargs)
        try:
            x = variables.index(self.value)
        except ValueError:
            raise ValueError("Variable {} not on provided dictionary of values".format(self.value))
        answer = list()
        for value in values:
            answer.append(value[x])
        return answer

    @classmethod
    def get_arguments(cls) -> int:
        """
        :return: 1 argument
        """
        return 2
