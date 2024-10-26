import math
import random

from src.entities.directions import Directions
from src.entities.maze import Maze, DiffTypesOfSurfaces
from src.entities.point import (
    gran_elem,
    central_elem,
    hill_elem,
    swamp_elem,
    forest_elem,
    common_elem,
    symbols,
    weights,
)
from src.services.generators.generator import Generator


class PrimGenerator(Generator):
    """
    A class that implements a Prim's algorithm-based maze generation.
    This generator uses a randomized version of Prim's algorithm to generate a maze.
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
        Generates a maze using Prim's algorithm.

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

        maze.grid[maze.start[1]][maze.start[0]].symbol = common_elem.symbol

        walls = [
            (maze.start[0] + direction.dx, maze.start[1] + direction.dy)
            for direction in Directions
            if 0 <= maze.start[0] + direction.dx < maze.width
            and 0 <= maze.start[1] + direction.dy < maze.height
        ]

        random.shuffle(walls)

        while walls:
            wx, wy = walls.pop()
            if (
                0 < wx < maze.width - 1
                and 0 < wy < maze.height - 1
                and (
                    maze.grid[wy][wx].symbol == gran_elem.symbol
                    or maze.grid[wy][wx].symbol == central_elem.symbol
                )
            ):

                neighbors = [
                    (wx + direction.dx, wy + direction.dy)
                    for direction in Directions
                    if 0 <= wx + direction.dx < maze.width
                    and 0 <= wy + direction.dy < maze.height
                    and maze.grid[wy + direction.dy][wx + direction.dx].symbol
                    in (
                        [
                            hill_elem.symbol,
                            swamp_elem.symbol,
                            forest_elem.symbol,
                            common_elem.symbol,
                        ]
                        if diff_types_of_surfaces == DiffTypesOfSurfaces.YES
                        else [common_elem.symbol]
                    )
                ]

                if len(neighbors) == 1:
                    if (
                        diff_types_of_surfaces
                        == DiffTypesOfSurfaces.YES
                    ):
                        choice = random.randint(0, len(symbols) - 1)
                        maze.grid[wy][wx].symbol = symbols[choice]
                        maze.grid[wy][wx].weight = weights[choice]
                    else:
                        maze.grid[wy][wx].symbol = common_elem.symbol
                        maze.grid[wy][wx].weight = common_elem.weight

                    walls.extend(
                        [
                            (wx + direction.dx, wy + direction.dy)
                            for direction in Directions
                            if 0 <= wx + direction.dx < maze.width
                            and 0 <= wy + direction.dy < maze.height
                            and (
                                maze.grid[wy + direction.dy][wx + direction.dx].symbol
                                == gran_elem.symbol
                                or maze.grid[wy + direction.dy][
                                    wx + direction.dx
                                ].symbol
                                == central_elem.symbol
                            )
                        ]
                    )
                    random.shuffle(walls)

        koef = math.ceil((maze.width * maze.height) * (1 - maze.density + 0.1))
        for _ in range(koef):
            rand_y = random.randint(1, maze.height - 2)
            rand_x = random.randint(1, maze.width - 2)
            maze.grid[rand_y][rand_x].symbol = common_elem.symbol
            maze.grid[rand_y][rand_x].weight = common_elem.weight

        return maze
