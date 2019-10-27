"""max_node.py: MaxNode class"""

from genetic_programming.ast.nodes import BinaryNode, Node


def _max(left: float, right: float) -> float:
    return max(left, right)


class MaxNode(BinaryNode):
    """
    MaxNode class, return maximum between left and right
    """
    def __init__(self, left: Node, right: Node):
        super().__init__(_max, left, right)

    def __repr__(self) -> str:
        return super().__repr__().format("max")
