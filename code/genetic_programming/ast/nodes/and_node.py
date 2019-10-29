"""and_node.py: AndNode Class"""

from genetic_programming.ast.nodes import BooleanNode


def _and(left: bool, right: bool) -> bool:
    return left and right


class AndNode(BooleanNode):
    """
    And Node, program that calculates and boolean function
    """
    def __init__(self, left: BooleanNode, right: BooleanNode):
        if left.type is not bool or right.type is not bool:
            raise ValueError("Both nodes given has to have boolean values")
        super().__init__(_and, 2, [left, right])

    def evaluate(self) -> bool:
        """
        And of arguments

        :return: And boolean operation
        """
        return self.function(self.arguments[0].evaluate(),
                             self.arguments[1].evaluate())

    def __repr__(self) -> str:
        return super().__repr__().format("and")
