"""nodes.py: Node abstract class (or interface)"""

from __future__ import annotations
from copy import deepcopy
from abc import ABC, abstractmethod


class Node(ABC):
    """
    Node class, an element of a tree
    """
    def __init__(self, function: callable, number_of_arguments: int):
        self.function = function
        self.number_of_arguments = number_of_arguments
        self.arguments = list()
        self._is_node = True
        self.type = None

    @abstractmethod
    def evaluate(self) -> object:
        """
        Evaluate recursive all nodes child of this one

        :return: Value
        """
        pass

    def replace_node(self, other: Node, position: int) -> None:
        """
        Replace one nodes with another

        :param other: Node to replace this one
        :param position: Position of nodes to replace
        :return: None (replace nodes itself)
        """
        try:
            self.arguments[position] = deepcopy(other)
        except IndexError:
            raise AttributeError("No nodes on the {} position, "
                                 "this nodes has {} sub nodes".format(position, self.number_of_arguments))

    def __eq__(self, other: Node) -> bool:
        """For test purpose"""
        try:
            if not other._is_node:
                return False
        except AttributeError:
            return False
        if self.function != other.function:
            return False
        if self.number_of_arguments != other.number_of_arguments:
            return False
        for arg1, arg2 in zip(self.arguments, other.arguments):
            if arg1 != arg2:
                return False
        return True

    def __repr__(self) -> str:
        children = ""
        for child in self.arguments:
            children += "\n|-{}".format(str(child))
        return "({})" + children.replace("\n", "\n  ")
