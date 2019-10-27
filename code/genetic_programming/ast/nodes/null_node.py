"""null_node.py: NullNode class"""

from genetic_programming.ast.nodes import Node


def _null_function():
    return None


class NullNode(Node):
    """Node with null functionality, for complement and test purpose"""

    def __init__(self):
        super().__init__(_null_function, 0)

    def evaluate(self) -> object:
        """
        Evaluate nodes

        :return: None
        """
        return self.function()
