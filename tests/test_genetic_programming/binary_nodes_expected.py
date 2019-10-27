"""binary_nodes_expected.py: Binary Nodes expected for test purpose"""

from genetic_programming.ast.nodes import AddNode, SubNode, MultNode, MaxNode, TerminalNode

values = list(range(1, 11))
expected_individual = (values[0] - values[1]) + (max(values[2], values[3] + values[4]) * (values[5]))
expected_stable_one = (values[6] * max(values[7], values[8] + values[9]))

individual = AddNode(
    SubNode(
        TerminalNode(values[0]),
        TerminalNode(values[1])
    ), MultNode(
        MaxNode(
            TerminalNode(values[2]), AddNode(
                TerminalNode(values[3]), TerminalNode(values[4])
            )
        ), TerminalNode(values[5])
    )
)
stable_one = MultNode(
    TerminalNode(values[6]), MaxNode(
        TerminalNode(values[7]), AddNode(
            TerminalNode(values[8]), TerminalNode(values[9])
        )
    )
)
