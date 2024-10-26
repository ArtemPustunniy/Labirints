import sys
import time

from src.entities.maze import DiffTypesOfSurfaces
from src.entities.point import common_elem
from src.services.renders.render import Render
from src.utils.utils import move_cursor


class RenderPath(Render):
    """Class responsible for rendering the path through the maze."""

    def render(self, maze, diff_types_of_surfaces, path: [] = None) -> None:
        """
        Renders the path in the maze based on the user's choice of maze type and an optional path.

        Args:
            maze: The maze object to render.
            diff_types_of_surfaces: The user's choice regarding different types of surfaces in the maze.
            path (list, optional): The path to render within the maze.
        """
        if path is None:
            return

        for x, y in path:
            if (y, x) == maze.start or (y, x) == maze.end:
                continue
            if diff_types_of_surfaces == DiffTypesOfSurfaces.YES:
                move_cursor(y + maze.delta + 1, x + 1)
                if maze.grid[x][y].symbol == common_elem.symbol:
                    sys.stdout.write("\033[31m*\033[0m")  # Write red '*' to represent the path
                else:
                    sys.stdout.write(f"\033[31m{maze.grid[x][y].symbol}\033[0m")
                sys.stdout.flush()
                time.sleep(0.05)
            else:
                move_cursor(y + maze.delta + 1, x + 1)
                sys.stdout.write("\033[31m*\033[0m")  # Write red '*' for the path
                sys.stdout.flush()
                time.sleep(0.05)
