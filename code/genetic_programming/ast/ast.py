"""ast.py: AST class"""

from __future__ import annotations
from abc import ABC, abstractmethod
from copy import deepcopy
from random import choice
from genetic_algorithm.individuals import MultiObjectiveIndividual, Individual
from genetic_programming.ast.nodes import Node


class AST(MultiObjectiveIndividual, ABC):
    """
    AST class, represents an Abstract Syntax Tree
    """
    def __init__(self, prob_terminal: float, mutation_rate: float, root: Node, depth: int = 0):
        super().__init__(None, None, 0, mutation_rate)
        self.root = deepcopy(root)
        if depth != 0:
            self.depth = depth
        else:
            self.depth = self._calculate_depth()
        self.prob_terminal = prob_terminal
        self._map = self._do_map()
        self._is_ast = True

    def _calculate_depth(self) -> (int, int):
        """
        Calculate depth of the Node on root

        :return: Depth of this AST and number of Nodes
        """
        def _get_depth(node: Node) -> (int, int):
            if len(node.arguments) == 0:
                return 0
            else:
                depths = list()
                for child in node.arguments:
                    depths.append(_get_depth(child))
                return 1 + max(depths)
        return _get_depth(self.root)

    def _do_map(self) -> [(int, ...)]:
        """
        Maps this AST

        :return: List with tuples indicating where the nodes are
        """
        def _a_map(node: Node, my_position: (int, ...), current_position: int) -> [(int, ...)]:
            if len(node.arguments) == 0:
                return [my_position + (current_position, )]
            else:
                mini_map = [my_position + (current_position, )]
                for position, child in enumerate(node.arguments):
                    mini_map.extend(_a_map(child, my_position + (current_position, ), position))
                return mini_map
        return _a_map(self.root, tuple(), 0)

    @abstractmethod
    def fitness(self) -> float:
        """
        Fitness

        :return: fitness
        """
        pass

    @abstractmethod
    def generate_tree(self, depth: int, prob_terminal: float) -> Node:
        """
        Generate a new Tree (node)

        :param depth: Maximum depth of tree
        :param prob_terminal: Probability of make a child, with less high
                            than depth, a terminal node
        :return: Node
        """
        pass

    def crossover(self, partner: AST) -> AST:
        """
        Crossover between AST

        :param partner: Another AST
        :return: A new AST
        """
        chiasma = choice(partner._map)
        to_cross = partner.get_node(chiasma)
        a_map = list()
        for p in self._map:
            if len(p) == len(chiasma):
                a_map.append(p)
        chiasma = choice(a_map)
        child = deepcopy(self)
        child.root = self.replace_on_position(chiasma, to_cross)
        child._map = child._do_map()
        child.mutate()
        child._map = child._do_map()
        return child

    def replace_on_position(self, position: (int, ...), other: Node) -> Node:
        """
        Replace

        :param position: Position to be replaced
        :param other: Node to replaced on position
        :return: Another node equal to root replaced
        """
        to_replace = deepcopy(self.root)  # Not reference, it is the output
        reference = to_replace
        use = list(position)
        if use == [0]:
            return deepcopy(other)
        use.pop(0)
        while len(use) > 1:
            reference = reference.arguments[use.pop(0)]
        reference.replace_node(other, use[0])
        return deepcopy(to_replace)

    def get_node(self, position: (int, ...)) -> Node:
        """
        Looks recursive for a Node in a specific position

        :param position: A tuple indicating where the nodes is
        :return: The Node looked for
        """
        to_export = deepcopy(self.root)
        use = list(position)
        use.pop(0)
        while len(use) > 0:
            to_export = deepcopy(to_export.arguments[use.pop(0)])
        return to_export

    def mutate(self) -> None:
        """
        Mutate this AST

        :return: None (change self.root)
        """
        if self.mutation_rate > 0:
            level_to_mutate = int((1 - self.mutation_rate) * self.depth)
            new_node = self.generate_tree(self.depth - level_to_mutate, self.prob_terminal)
            available_positions = list()
            for position in self._map:
                if len(position) == level_to_mutate + 1:
                    available_positions.append(position)
            position = choice(available_positions)
            self.root = self.replace_on_position(position, new_node)
        return

    def copy(self) -> AST:
        """
        Return an independent copy (not a reference) of this AST

        :return: Same AST
        """
        return deepcopy(self)

    def __repr__(self) -> str:
        return str(self.root)

    def __len__(self) -> int:
        return len(self._map)

    def __eq__(self, other: AST):
        """For test purpose"""
        try:
            if not other._is_ast:
                return False
        except AttributeError:
            return False
        if self.root != other.root:
            return False
        if self.depth != other.depth:
            return False
        if self.prob_terminal != other.prob_terminal:
            return False
        if not super().__eq__(other):
            return False
        return True
