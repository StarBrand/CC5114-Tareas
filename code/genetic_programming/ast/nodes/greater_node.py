"""greater_node.py: GreaterNode class"""

from genetic_programming.ast.nodes import BooleanNode, Node


def _greater(left: float, right: float) -> bool:
    return left > right


class GreaterNode(BooleanNode):
    """
    GreaterNode, implements '>' function
    """
    def __init__(self, left: Node, right: Node):
        super().__init__(_greater, 2, [left, right])

    def evaluate(self) -> bool:
        """
        Evaluate ">"

        :return: Whether left is greater
        """
        return self.function(self.arguments[0].evaluate(),
                             self.arguments[1].evaluate())

    def __repr__(self) -> str:
        return super().__repr__().format(">")
