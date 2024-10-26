import sys


class Point:
    """
    A class to represent a point on a 2D grid, which can have a weight and a symbol.

    Attributes:
        x (int): The x-coordinate of the point.
        y (int): The y-coordinate of the point.
        weight (int): The weight of the point, used to represent cost or difficulty in navigation.
        symbol (str): The visual representation of the point on the grid.
    """

    def __init__(self, x: int, y: int, weight: int = 1, symbol: str = " "):
        """
        Initializes the point with its x, y coordinates, weight, and symbol.

        Args:
            x (int): The x-coordinate of the point.
            y (int): The y-coordinate of the point.
            weight (int, optional): The weight or cost associated with this point. Default is 1.
            symbol (str, optional): The symbol representing this point. Default is a space ' '.
        """
        self.x = x
        self.y = y
        self.weight = weight
        self.symbol = symbol

    def __lt__(self, other):
        """
        Compares two points based on their weight for sorting purposes.

        Args:
            other (Point): The other point to compare with.

        Returns:
            bool: True if this point has a lower weight than the other point.
        """
        return self.weight < other.weight

    def __repr__(self) -> str:
        """
        Returns a string representation of the point, showing its weight and symbol.

        Returns:
            str: A string representation of the point.
        """
        return f"Point(weight={self.weight}, symbol={self.symbol})"


gran_elem = Point(0, 0, sys.maxsize, "█")
central_elem = Point(
    0, 0, sys.maxsize, "#"
)
hill_elem = Point(
    0, 0, 5, "^"
)
swamp_elem = Point(
    0, 0, 3, "~"
)
forest_elem = Point(
    0, 0, 2, "@"
)
common_elem = Point(
    0, 0, 1, " "
)

symbols = [hill_elem.symbol, swamp_elem.symbol, forest_elem.symbol, common_elem.symbol]
weights = [hill_elem.weight, swamp_elem.weight, forest_elem.weight, common_elem.weight]
