"""lesser_node.py: LesserNode Class"""

from genetic_programming.ast.nodes import BooleanNode, Node, BinaryNode


def _lesser(left: float, right: float) -> bool or [bool]:
    return left < right


class LesserNode(BooleanNode, BinaryNode):
    """
    Lesser Node, program that calculates '<' function
    """
    def __init__(self, left: Node, right: Node):
        super().__init__(_lesser, 2, [left, right])

    def evaluate(self, **kwargs) -> bool or [bool]:
        """
        Evaluate node

        :return: Bool indicating whether left has same value than right
        """
        return super().evaluate(**kwargs)

    def __repr__(self) -> str:
        return super().__repr__().format("<")
