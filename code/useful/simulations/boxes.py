"""boxes.py: simulate the 5 boxes of the UnboundKnapsack problem"""


class Box:
    """
    Box of UnboundKnapsack
    """
    def __init__(self, weight: float, value: float, name: str):
        self.weight = weight
        self.value = value
        self._name = name

    def __repr__(self):
        return self._name

    def __str__(self):
        return self._name


NullBox = Box(0, 0, "None")
BOX1 = Box(12, 4, "Box1")
BOX2 = Box(2, 2, "Box2")
BOX3 = Box(1, 2, "Box3")
BOX4 = Box(1, 1, "Box4")
BOX5 = Box(4, 10, "Box5")
