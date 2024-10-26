import sys

from src.services.renders.render import Render
from src.utils.utils import move_cursor


class DefaultRender(Render):
    """Class responsible for rendering the maze in its default form."""

    def render(self, maze, diff_types_of_surfaces, path: [] = None) -> None:
        """
        Renders the maze along with the user's choice of maze type and optionally a path.

        Args:
            maze: The maze object to render.
            diff_types_of_surfaces: The user's choice regarding the type of maze.
            path (list, optional): The path to render within the maze.
        """
        maze.grid[maze.start[1]][maze.start[0]].symbol = "A"
        maze.grid[maze.end[1]][maze.end[0]].symbol = "B"

        for y, row in enumerate(maze.grid):
            move_cursor(maze.delta + 1, y + 1)
            sys.stdout.write("".join(point.symbol for point in row) + "\n")
        sys.stdout.flush()
