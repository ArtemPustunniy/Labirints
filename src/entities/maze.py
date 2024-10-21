import sys
from enum import Enum

from src.entities.point import Point, gran_elem, central_elem


class Maze:
    """
    A class to represent a maze grid. Each cell in the maze is represented by a Point object,
    and the maze has configurable size, start and end points, density, and a user choice for
    the type of maze.

    Attributes:
        width (int): The width of the maze.
        height (int): The height of the maze.
        grid (list): A 2D list representing the maze grid, where each cell is a Point.
        start (tuple): The coordinates (x, y) of the start point of the maze.
        end (tuple): The coordinates (x, y) of the end point of the maze.
        density (int): The density of obstacles or walls in the maze.
        user_choice_of_type_of_maze (PossibleChoiceOfTypeOfMaze): The user's choice
            for generating the type of maze.
        delta (int): A constant value representing some variation or factor for the maze, default is 100.
    """

    def __init__(
        self,
        width: int,
        height: int,
        cords: tuple,
        density,
        user_choice_of_type_of_maze,
    ):
        """
        Initializes the maze with its width, height, start/end coordinates, density, and user choice.

        Args:
            width (int): The width of the maze.
            height (int): The height of the maze.
            cords (tuple): A tuple containing the start (x, y) and end (x, y) coordinates.
            density (int): The density of obstacles or walls in the maze.
            user_choice_of_type_of_maze (Enum): Enum indicating if the user wants to customize the maze type.
        """
        self.width = width
        self.height = height
        # Initialize the maze grid with Point objects and set the boundary as 'gran_elem'.
        self.grid = [
            [Point(j, i, sys.maxsize, central_elem.symbol) for j in range(width)]
            for i in range(height)
        ]
        for i in range(height):
            for j in range(width):
                if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                    self.grid[i][j] = Point(j, i, sys.maxsize, gran_elem.symbol)

        self.start = (cords[0], cords[1])  # Set the start point of the maze.
        self.end = (cords[2], cords[3])  # Set the end point of the maze.
        self.density = density  # Set the density of obstacles.
        self.user_choice_of_type_of_maze = (
            user_choice_of_type_of_maze  # User's choice for maze type.
        )
        self.delta = 100  # Constant value (purpose not specified in this code).


class PossibleChoiceOfTypeOfMaze(Enum):
    """
    Enum class to represent the user's possible choices for maze customization.

    Attributes:
        YES (str): Option for 'Yes' in Russian ("Да").
        NO (str): Option for 'No' in Russian ("Нет").
    """

    YES = "Да"
    NO = "Нет"
