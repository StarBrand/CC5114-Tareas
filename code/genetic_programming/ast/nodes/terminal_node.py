"""terminal_node.py: TerminalNode class """

from genetic_programming.ast.nodes import Node, NullNode


class TerminalNode(Node):
    """Terminal nodes, represent leaves of tree"""

    def __init__(self, value: object):
        super().__init__(NullNode().function, 0)
        self.value = value
        if isinstance(value, bool):
            self.type = bool
        elif isinstance(value, float):
            self.type = float

    def evaluate(self) -> object:
        """
        Evaluate this terminal nodes
        :return:
        """
        return self.value

    def __eq__(self, other: Node) -> bool:
        if isinstance(other, TerminalNode):
            if self.value == other.value:
                return True
        return False

    def __repr__(self) -> str:
        return "({})".format(str(self.value))
