import math
import random

from src.entities.directions import Directions
from src.entities.maze import Maze, DiffTypesOfSurfaces
from src.entities.point import common_elem, gran_elem, central_elem, symbols, weights
from src.services.generators.generator import Generator


class DfsGenerator(Generator):
    """
    A class that implements a Depth-First Search (DFS) based maze generation algorithm.
    This generator creates mazes using a randomized DFS approach to create paths.
    """

    def generate(
        self,
        width: int,
        height: int,
        cords: tuple,
        density,
        diff_types_of_surfaces: DiffTypesOfSurfaces,
    ) -> Maze:
        """
        Generates a maze using the DFS algorithm.

        Args:
            width (int): The width of the maze.
            height (int): The height of the maze.
            cords (tuple): A tuple containing the start and end coordinates of the maze.
            density (float): The density of walls or obstacles in the maze.
            diff_types_of_surfaces (DiffTypesOfSurfaces): Indicates whether the maze should contain different surfaces.

        Returns:
            Maze: The generated maze object.
        """
        maze = Maze(width, height, cords, density, diff_types_of_surfaces)

        stack = [maze.start]
        maze.grid[maze.start[1]][maze.start[0]].symbol = common_elem.symbol
        maze.grid[maze.start[1]][maze.start[0]].weight = common_elem.weight

        maze.grid[maze.end[1]][maze.end[0]].symbol = common_elem.symbol
        maze.grid[maze.end[1]][maze.end[0]].weight = common_elem.weight

        while stack:
            current = stack[-1]
            x, y = current
            neighbors = []

            for direction in Directions:
                ny, nx = y + 2 * direction.dy, x + 2 * direction.dx
                if 0 < ny < maze.height - 1 and 0 < nx < maze.width - 1:
                    if (
                        maze.grid[ny][nx].symbol == gran_elem.symbol
                        or maze.grid[ny][nx].symbol == central_elem.symbol
                    ):
                        neighbors.append((nx, ny))

            if neighbors:
                next_cell = random.choice(neighbors)
                nx, ny = next_cell

                if diff_types_of_surfaces == DiffTypesOfSurfaces.YES.value:
                    choice = random.randint(0, 3)
                    maze.grid[ny][nx].symbol = symbols[choice]
                    maze.grid[(y + ny) // 2][(x + nx) // 2].symbol = symbols[choice]
                    maze.grid[ny][nx].weight = weights[choice]
                    maze.grid[(y + ny) // 2][(x + nx) // 2].weight = weights[choice]
                else:
                    maze.grid[ny][nx].symbol = common_elem.symbol
                    maze.grid[(y + ny) // 2][(x + nx) // 2].symbol = common_elem.symbol
                    maze.grid[ny][nx].weight = common_elem.weight
                    maze.grid[(y + ny) // 2][(x + nx) // 2].weight = common_elem.weight

                stack.append(next_cell)
            else:
                stack.pop()

        koef = math.ceil((maze.width * maze.height) * (1 - maze.density + 0.1))
        for _ in range(koef):
            rand_y = random.randint(1, maze.height - 2)
            rand_x = random.randint(1, maze.width - 2)
            maze.grid[rand_y][rand_x].symbol = common_elem.symbol
            maze.grid[rand_y][rand_x].weight = 1

        return maze
