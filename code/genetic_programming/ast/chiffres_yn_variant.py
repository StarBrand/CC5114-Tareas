"""chiffres_yn_variant.py: French TV Show game variant, when numbers can (not) be used just one"""

from __future__ import annotations
from copy import deepcopy
from math import ceil, log2
from random import choice
from genetic_programming.ast import BinaryAST, AST
from genetic_programming.ast.asbt import POSSIBLE_NODES, _diff
from genetic_programming.ast.nodes import Node, YesNoNode


class ChiffresYesNoVariant(BinaryAST):
    """
    Binary AST adapted to guess a equation using numbers one or none time
    """
    def __init__(self, number_expected: float, values: [float], mutation_rate: float):
        self.values_allowed = values
        node = self.generate_tree(0, 0)
        super(BinaryAST, self).__init__(0, mutation_rate, node, depth=self.depth)
        self._fitness_function = _diff
        self.number_expected = number_expected

    def generate_tree(self, depth: int, prob_terminal: float) -> Node:
        """
        Generate a binary tree with restricted terminals

        :param depth: Maximum depth
        :param prob_terminal: Probability of every Node to be TerminalNode
        :return: A Node
        """
        values = deepcopy(self.values_allowed)
        self.depth = ceil(log2(len(values)))

        def _generate_tree(d: int) -> Node:

            def _terminal(_r: int) -> Node:
                return YesNoNode(values.pop(0), choice([True, False]))

            def _internal(_l: Node, _r: Node) -> Node:
                this = choice(POSSIBLE_NODES)
                return this(_l, _r)

            r = len(values)
            if d == 0:
                return _terminal(r - 1)
            elif d == 1 or r <= 2:
                if r >= 2:
                    left = _terminal(r - 1)
                    right = _terminal(r - 2)
                    return _internal(left, right)
                elif 1 <= r <= 2:
                    return _terminal(r - 1)
            else:
                left = _generate_tree(d - 1)
                right = _generate_tree(d - 1)
                return _internal(left, right)

        return _generate_tree(self.depth)

    def crossover(self, partner: ChiffresYesNoVariant) -> ChiffresYesNoVariant:
        """
        Crossover between Chiffres, inplace

        :param partner: Another Chiffres
        :return: A new Chiffres
        """
        chiasma = choice(partner._map)
        to_cross = partner.get_node(chiasma)
        child = deepcopy(self)
        child.root = self.replace_on_position(chiasma, to_cross)
        child.mutate()
        return child

    def mutate(self) -> None:
        """
        Mutate this Chiffres, inplace

        :return: None (change self.root)
        """
        if self.mutation_rate > 0:
            level_to_mutate = int((1 - self.mutation_rate) * self.depth)
            new_node = self.generate_individual()
            available_positions = list()
            for position in self._map:
                if len(position) == level_to_mutate + 1:
                    available_positions.append(position)
            position = choice(available_positions)
            new_node = new_node.get_node(position)
            self.root = self.replace_on_position(position, new_node)
        return

    def generate_individual(self) -> AST:
        """
        Generate a new ChiffresYesNoVariant individual

        :return: ChiffresYesNoVariant
        """
        return ChiffresYesNoVariant(self.number_expected, self.values_allowed, self.mutation_rate)
