from enum import Enum


class Directions(Enum):
    """
    Enum class to represent cardinal directions (NORTH, SOUTH, EAST, WEST).
    Each direction is associated with a 2D vector (dx, dy) that represents
    movement along the x and y axes on a grid.

    Attributes:
        _dx (int): The movement along the x-axis.
        _dy (int): The movement along the y-axis.
    """

    NORTH = (0, -1)
    SOUTH = (0, 1)
    EAST = (1, 0)
    WEST = (-1, 0)

    def __init__(self, dx: int, dy: int):
        """
        Initializes the direction with its associated dx and dy values.

        Args:
            dx (int): The movement along the x-axis.
            dy (int): The movement along the y-axis.
        """
        self._dx = dx
        self._dy = dy

    @property
    def dx(self) -> int:
        """
        Returns the movement along the x-axis (dx) for the direction.

        Returns:
            int: The dx value.
        """
        return self._dx

    @property
    def dy(self) -> int:
        """
        Returns the movement along the y-axis (dy) for the direction.

        Returns:
            int: The dy value.
        """
        return self._dy
