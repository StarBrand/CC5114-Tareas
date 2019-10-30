"""yes_no_node.py: YesNoNode Class"""

from genetic_programming.ast.nodes import TerminalNode
from useful.math_functions import SuperNeutral


class YesNoNode(TerminalNode):
    """
    YesNoNode: A Node that does (not) have a value
    """
    def __init__(self, value: object, exist: bool):
        if exist:
            super().__init__(value)
        else:
            super().__init__(SuperNeutral())
        self.type = float

    @classmethod
    def get_arguments(cls) -> int:
        """
        :return: 2 argument
        """
        return 2
