"""mult_node.py: MultNode class"""

from genetic_programming.ast.nodes import BinaryNode, Node


def _div(left: float, right: float) -> float:
    return left / right


class DivNode(BinaryNode):
    """
    MultNode, multiply left and right
    """
    def __init__(self, left: Node, right: Node):
        super().__init__(_div, left, right)

    def __repr__(self) -> str:
        return super().__repr__().format("/")
