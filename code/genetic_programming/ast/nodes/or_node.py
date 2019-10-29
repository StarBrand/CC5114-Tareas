"""or_node.py: OrNode Class"""

from genetic_programming.ast.nodes import BooleanNode


def _or(left: bool, right: bool) -> bool:
    return left or right


class OrNode(BooleanNode):
    """
    Or Node, program that calculates or boolean function
    """
    def __init__(self, left: BooleanNode, right: BooleanNode):
        if left.type is not bool or right.type is not bool:
            raise ValueError("Both nodes given has to have boolean values")
        super().__init__(_or, 2, [left, right])

    def evaluate(self) -> bool:
        """
        Or of arguments

        :return: Or boolean operation
        """
        return self.function(self.arguments[0].evaluate(),
                             self.arguments[1].evaluate())

    def __repr__(self) -> str:
        return super().__repr__().format("or")
