"""result_DesChiffresEtDesLettres.py: Result of the game found.
This was written by hand to show results found as equation"""

from genetic_programming.ast.nodes import Node, BinaryNode, AddNode, SubNode, MultNode, MaxNode, TerminalNode, YesNoNode
from useful.math_functions.super_neutral import SuperNeutral


def as_equation(node: Node) -> str:
    """
    Get the node as an equation

    :param node: Node to show
    :return: String that represents the node
    """
    def _symbol(symbol_node: BinaryNode) -> str:
        if isinstance(symbol_node, AddNode):
            return "+"
        elif isinstance(symbol_node, SubNode):
            return "-"
        elif isinstance(symbol_node, MultNode):
            return "*"
        else:
            raise ValueError("Input {} is not valid".format(node))
    if node.number_of_arguments == 0:
        return str(node).replace("(", "").replace(")", "")
    elif isinstance(node, MaxNode):
        return "max({}, {})".format(as_equation(node.arguments[0]),
                                    as_equation(node.arguments[1]))
    else:
        return "({} {} {})".format(as_equation(node.arguments[0]),
                                   _symbol(node),
                                   as_equation(node.arguments[1]))


def simplify(node: BinaryNode) -> BinaryNode:
    """
    Simplify a node, by deleting max nodes

    :param node: A node to simplify
    :return: Node without MaxNodes
    """
    if node.number_of_arguments > 0:
        if node.arguments[0].evaluate() == SuperNeutral():
            return node.arguments[1]
        elif node.arguments[1].evaluate() == SuperNeutral():
            return node.arguments[0]
    if isinstance(node, MaxNode):
        if node.arguments[0].evaluate() >= node.arguments[1].evaluate():
            return simplify(node.arguments[0])
        else:
            return simplify(node.arguments[1])
    elif node.number_of_arguments == 0:
        return node
    else:
        node.replace_node(simplify(node.arguments[0]), 0)
        node.replace_node(simplify(node.arguments[1]), 1)
        return node


""" Unbound version """
unbound_answer = AddNode(
    MultNode(
        MaxNode(
            SubNode(
                AddNode(TerminalNode(100), TerminalNode(7)),
                MultNode(TerminalNode(100), TerminalNode(25))
            ),
            AddNode(
                AddNode(TerminalNode(2), TerminalNode(8)),
                AddNode(TerminalNode(100), TerminalNode(100))
            )
        ),
        SubNode(
            AddNode(
                AddNode(TerminalNode(100), TerminalNode(25)),
                SubNode(TerminalNode(7), TerminalNode(8))
            ),
            MultNode(
                SubNode(TerminalNode(2), TerminalNode(4)),
                SubNode(TerminalNode(100), TerminalNode(7))
            )
        )
    ),
    AddNode(
        MaxNode(
            AddNode(
                MaxNode(TerminalNode(7), TerminalNode(7)),
                MaxNode(TerminalNode(8), TerminalNode(7))
            ),
            SubNode(
                AddNode(
                    TerminalNode(25), TerminalNode(25)
                ),
                MultNode(
                    TerminalNode(7), TerminalNode(2)
                )
            )
        ),
        MaxNode(
            SubNode(
                AddNode(TerminalNode(25), TerminalNode(7)),
                MultNode(TerminalNode(100), TerminalNode(25))
            ),
            AddNode(
                AddNode(TerminalNode(2), TerminalNode(8)),
                AddNode(TerminalNode(100), TerminalNode(100))
            )
        )
    )
)

y_n_answer = MultNode(
    MultNode(
        MultNode(TerminalNode(25), TerminalNode(7)),
        MaxNode(YesNoNode(8, False), TerminalNode(100))
    ),
    MaxNode(TerminalNode(4), TerminalNode(2))
)


if __name__ == '__main__':
    def _print(answer: BinaryNode) -> None:
        """
        Print answer (to avoid duplicate code)

        :param answer: Node with the answer
        :return: Print answer
        """
        print("\tAs tree:")
        print(answer)
        print("\tAs equation:")
        print("{} = {}".format(as_equation(answer), answer.evaluate()))
        print("\t Simplifying:")
        simplified = simplify(answer)
        print("\t\tAs tree:")
        print(simplified)
        print("\t\tAs equation:")
        print("{} = {}".format(as_equation(simplified), simplified.evaluate()))
        return

    print("Unbound answer:")
    _print(unbound_answer)
    print("Yes-or-No answer:")
    _print(y_n_answer)
