"""greater_node.py: GreaterNode class"""

from genetic_programming.ast.nodes import BooleanNode, Node, BinaryNode


def _greater(left: float, right: float) -> bool or [bool]:
    return left > right


class GreaterNode(BooleanNode, BinaryNode):
    """
    GreaterNode, implements '>' function
    """
    def __init__(self, left: Node, right: Node):
        BooleanNode.__init__(self, _greater, 2, [left, right])

    def evaluate(self, **kwargs) -> bool or [bool]:
        """
        Evaluate node '>'

        :return: Bool indicating whether left has greater value than right
        """
        return super().evaluate(**kwargs)

    def __repr__(self) -> str:
        return super().__repr__().format(">")
