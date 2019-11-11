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

    def evaluate(self, **kwargs) -> object or [object]:
        """
        Evaluate this terminal nodes

        :return: value
        """
        if "values" in kwargs.keys():
            try:
                return [self.value] * len(kwargs["values"][1])
            except KeyError:
                length = 1
                if len(kwargs["values"].values()) == 0:
                    length = length * 0
                for a_list in kwargs["values"].values():
                    length *= len(a_list)
                return [self.value] * length
        return self.value

    def __eq__(self, other: Node) -> bool:
        if isinstance(other, TerminalNode):
            if self.value == other.value:
                return True
        return False

    def __repr__(self) -> str:
        return "({})".format(str(self.value))

    @classmethod
    def get_arguments(cls) -> int:
        """
        :return: 1 argument
        """
        return 1
