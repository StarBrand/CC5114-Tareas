"""not_node.py: NotNode class"""

from genetic_programming.ast.nodes import BooleanNode, TerminalNode


def _not(_value: bool) -> bool or [bool]:
    return not _value


class NotNode(BooleanNode):
    """
    NotNode class, a program that return not a bool
    """
    def __init__(self, node: BooleanNode or TerminalNode):
        if node.type is not bool:
            raise ValueError("Need a boolean node as argument")
        super().__init__(_not, 1, [node])

    def evaluate(self, **kwargs) -> bool or [bool]:
        """
        Evaluate a boolean as his negation

        :return: Not input node
        """
        try:
            ready, variables, values = self._receive_values(**kwargs)
            answer = list()
            args = self.arguments[0].evaluate(ready=ready, values=(variables, values))
            for a in args:
                answer.append(self.function(a))
            return answer
        except ValueError:
            return self.function(self.arguments[0].evaluate())

    def __repr__(self) -> str:
        return super().__repr__().format("not")

    @classmethod
    def get_arguments(cls) -> int:
        """
        :return: 2 arguments
        """
        return 1
