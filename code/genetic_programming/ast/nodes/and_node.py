"""and_node.py: AndNode Class"""

from genetic_programming.ast.nodes import BooleanNode, BinaryNode, TerminalNode


def _and(left: bool, right: bool) -> bool or [bool]:
    return left and right


class AndNode(BooleanNode, BinaryNode):
    """
    And Node, program that calculates and boolean function
    """
    def __init__(self, left: BooleanNode or TerminalNode, right: BooleanNode or TerminalNode):
        if left.type is not bool or right.type is not bool:
            raise ValueError("Both nodes given has to have boolean values")
        super().__init__(_and, 2, [left, right])

    def evaluate(self, **kwargs) -> bool or [bool]:
        """
        And of arguments

        :return: And boolean operation
        """
        return super().evaluate(**kwargs)

    def __repr__(self) -> str:
        return super().__repr__().format("and")
