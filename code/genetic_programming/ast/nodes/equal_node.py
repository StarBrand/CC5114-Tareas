"""equal_node.py: EqualNode Class"""

from genetic_programming.ast.nodes import BooleanNode, Node


def _equal(left: float, right: float) -> bool:
    return left == right


class EqualNode(BooleanNode):
    """
    Equal Node, program that calculates '=' function
    """
    def __init__(self, left: Node, right: Node):
        super().__init__(_equal, 2, [left, right])

    def evaluate(self) -> bool:
        """
        Evaluate node

        :return: Bool indicating whether left has same value than right
        """
        return self.function(self.arguments[0].evaluate(),
                             self.arguments[1].evaluate())

    def __repr__(self) -> str:
        return super().__repr__().format("=")
