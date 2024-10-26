from abc import ABC, abstractmethod


class Render(ABC):
    """Abstract base class for rendering the maze."""

    @abstractmethod
    def render(self, maze, diff_types_of_surfaces, path: [] = None) -> None:
        """
        Abstract method that must be implemented by subclasses to render the maze.

        Args:
            maze: The maze object to render.
            diff_types_of_surfaces: The user's choice regarding the type of maze.
            path (list, optional): The path to render within the maze.
        """
        pass
