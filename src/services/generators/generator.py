from abc import ABC, abstractmethod
from enum import Enum

from src.entities.maze import DiffTypesOfSurfaces


class Generator(ABC):
    """
    Abstract base class for maze generators. Defines an interface that all concrete maze generators must implement.
    """

    @abstractmethod
    def generate(
        self,
        width: int,
        height: int,
        cords: tuple,
        density,
        diff_types_of_surfaces: DiffTypesOfSurfaces,
    ) -> None:
        """
        Abstract method to generate a maze.

        Args:
            width (int): The width of the maze.
            height (int): The height of the maze.
            cords (tuple): A tuple containing the start and end coordinates of the maze.
            density (float): The density of walls or obstacles in the maze.
            diff_types_of_surfaces (DiffTypesOfSurfaces): Indicates whether the maze should contain different surfaces.

        Returns:
            Maze: The generated maze object.
        """
        pass


class AvailableGenerators(Enum):
    """
    Enum class to represent the available types of maze generators.

    Attributes:
        DfsGenerator (int): Represents the Depth-First Search (DFS) generator.
        PrimGenerator (int): Represents the Prim's algorithm generator.
        KruskalGenerator (int): Represents the Kruskal's algorithm generator.
    """

    DfsGenerator = 1
    PrimGenerator = 2
    KruskalGenerator = 3
