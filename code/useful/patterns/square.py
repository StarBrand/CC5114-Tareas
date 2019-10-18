"""square.py: Square Class"""
from useful.patterns import Pattern


class Square(Pattern):
    """Square pattern"""

    def __init__(self, face: float, center: (float, float), x_range: (float, float), y_range: (float, float)):
        face = abs(face)
        x_min = center[0] - (face / 2)
        x_max = center[0] + (face / 2)
        y_min = center[1] - (face / 2)
        y_max = center[1] + (face / 2)
        assert x_range[0] <= x_min and x_max <= x_range[1]
        assert y_range[0] <= y_min and y_max <= y_range[1]
        super().__init__(x_range, y_range, "Square")
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def x_to_y(self, x: float) -> [float]:
        """
        Gives y values from x value

        :param x: abscissa coordinate
        :return: ordinate coordinate
        """
        if self.x_min > x or x > self.x_max:
            return []
        return [self.y_min, self.y_max]

    def y_to_x(self, y: float) -> [float]:
        """
        Gives x values from y value

        :param y: ordinate coordinate
        :return: abscissa coordinate
        """
        if self.y_min > y or y > self.y_max:
            return []
        return [self.x_min, self.x_max]

    # outside
    def is_above(self, x: float, y: float) -> bool:
        """
        Return if a given point is outside pattern

        :param x: x coordinate
        :param y: y coordinate
        :return: Whether the point is outside
        """
        return len(self.x_to_y(x)) == 0 or len(self.y_to_x(y)) == 0

    def graph(self) -> ([float], [float]):
        """
        Gives values to be graph

        :return: Two arrays to be used for graphic pattern
        """
        return ([self.x_min, self.x_max, self.x_max, self.x_min, self.x_min],
                [self.y_max, self.y_max, self.y_min, self.y_min, self.y_max])
