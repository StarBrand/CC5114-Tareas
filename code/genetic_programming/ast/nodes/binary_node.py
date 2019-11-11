"""binary_node.py: BinaryNode class"""

from copy import deepcopy
from genetic_programming.ast.nodes import Node


class BinaryNode(Node):
    """
    BinaryNode class, a Node with two arguments
    """
    def __init__(self, function: callable, left: Node, right: Node):
        super().__init__(function, 2)
        self.arguments.append(deepcopy(left))
        self.arguments.append(deepcopy(right))
        self.type = float

    def evaluate(self, **kwargs) -> float or [float]:
        """
        Evaluate Binary Node

        :return: Value of binary nodes
        """
        try:
            ready, variables, values = self._receive_values(**kwargs)
            answer = list()
            left = self.arguments[0].evaluate(ready=ready, values=(variables, values))
            right = self.arguments[1].evaluate(ready=ready, values=(variables, values))
            for l, r in zip(left, right):
                try:
                    answer.append(self.function(l, r))
                except ZeroDivisionError:
                    answer.append(float('NaN'))
            return answer
        except ValueError:
            return self.function(self.arguments[0].evaluate(),
                                 self.arguments[1].evaluate())

    def __repr__(self) -> str:
        first_child = "\n|-{}".format(str(self.arguments[0]))
        second_child = "\n|-{}".format(str(self.arguments[1]))
        return "({})" + (first_child + second_child).replace("\n", "\n  ")

    @classmethod
    def get_arguments(cls) -> int:
        """
        :return: 2 arguments
        """
        return 2
