"""add_node.py: AddNode class"""

from genetic_programming.ast.nodes import BinaryNode, Node


def _add(left: float, right: float) -> float:
    return left + right


class AddNode(BinaryNode):
    """
    AddNode class, add first and second argument
    """
    def __init__(self, left: Node, right: Node):
        super().__init__(_add, left, right)

    def __repr__(self) -> str:
        return super().__repr__().format("+")
