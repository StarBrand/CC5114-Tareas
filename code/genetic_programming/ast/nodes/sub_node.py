"""sub_node.py: SubNode class"""

from genetic_programming.ast.nodes import BinaryNode, Node


def _sub(left: float, right: float) -> float:
    return left - right


class SubNode(BinaryNode):
    """
    SubNode class, subtracts right to left
    """
    def __init__(self, left: Node, right: Node):
        super().__init__(_sub, left, right)

    def __repr__(self) -> str:
        return super().__repr__().format("-")
