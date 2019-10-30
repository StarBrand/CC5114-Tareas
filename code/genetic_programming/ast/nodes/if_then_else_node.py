"""if_then_else_node.py: IfThenElseNode program as a node of a AST"""

from genetic_programming.ast.nodes import Node, BooleanNode


def _if_then_else(condition: bool, then: object, other: object) -> object:
    if condition:
        return then
    else:
        return other


class IfThenElseNode(Node):
    """
    IfThenElseNode, a conditional program for genetic programming
    """
    def __init__(self, condition: BooleanNode, then_node: Node, else_node: Node):
        if condition.type is not bool:
            raise ValueError("Condition must be a boolean node")
        super().__init__(_if_then_else, 3)
        self.arguments.append(condition)
        self.arguments.append(then_node)
        self.arguments.append(else_node)
        self.type = None

    def evaluate(self) -> object:
        """
        Return then_node value if condition evaluate as true,
        or else_node otherwise

        :return: Value of then_node or else_node
        """
        out_value = self.function(self.arguments[0].evaluate(),
                                  self.arguments[1].evaluate(),
                                  self.arguments[2].evaluate())
        if isinstance(out_value, bool):
            self.type = bool
        elif isinstance(out_value, float):
            self.type = float
        return out_value

    def replace_node(self, other: Node, position: int) -> None:
        """
        Replace node inherit for node, but with an exception added

        :param other: Node to replace
        :param position: Position to replace
        :return: None (change self.arguments)
        """
        if position == 0 and other.type is not bool:
            raise ValueError("Condition must be a boolean node, {} node given".format(other.type))
        super().replace_node(other, position)
        return

    def __repr__(self) -> str:
        return super().__repr__().format("if")

    @classmethod
    def get_arguments(cls) -> int:
        """
        :return: 2 arguments
        """
        return 3
