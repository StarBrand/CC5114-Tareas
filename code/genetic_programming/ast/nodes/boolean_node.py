"""boolean_node.py: BooleanNode class"""

from abc import ABC
from copy import deepcopy
from genetic_programming.ast.nodes import Node


class BooleanNode(Node, ABC):
    """
    BinaryNode class, a Node with two arguments
    """
    def __init__(self, function: callable, arguments: int, nodes: [Node]):
        super().__init__(function, arguments)
        for node in nodes:
            self.arguments.append(deepcopy(node))
        self.type = bool

    def __repr__(self) -> str:
        children = ""
        for child in self.arguments:
            children += "\n|-{}".format(str(child))
        return "({})" + children.replace("\n", "\n  ")

    @classmethod
    def get_arguments(cls) -> int:
        """
        To be override for exceptions

        :return: 2 arguments
        """
        return 2
