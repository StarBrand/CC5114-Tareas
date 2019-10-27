"""mult_node.py: MultNode class"""

from genetic_programming.ast.nodes import BinaryNode, Node


def _mult(left: float, right: float) -> float:
    return left * right


class MultNode(BinaryNode):
    """
    MultNode, multiply left and right
    """
    def __init__(self, left: Node, right: Node):
        super().__init__(_mult, left, right)

    def __repr__(self) -> str:
        return super().__repr__().format("*")
