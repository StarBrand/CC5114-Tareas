"""super_neutral.py: A float that always return the other one"""


class SuperNeutral(float):
    """
    A number that always return the other one
    (Pass max not min)
    """

    def __init__(self):
        super().__init__()

    def __repr__(self) -> str:
        return "super_neutral"

    def __str__(self) -> str:
        return "super_neutral"

    def __add__(self, other: float) -> float:
        return other

    def __sub__(self, other: float) -> float:
        return other

    def __gt__(self, other: float) -> bool:
        return False

    def __ge__(self, other: float) -> bool:
        return False

    def __lt__(self, other: float) -> bool:
        return True

    def __le__(self, other: float) -> bool:
        return True

    def __eq__(self, other: float) -> bool:
        return str(other) == "super_neutral"

    def __mul__(self, other: float) -> float:
        return other

    def __rmul__(self, other: float) -> float:
        return other
