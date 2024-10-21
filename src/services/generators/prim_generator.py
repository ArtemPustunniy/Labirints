import math
import random

from src.entities.directions import Directions
from src.entities.maze import Maze, PossibleChoiceOfTypeOfMaze
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
        user_choice_of_type_of_maze,
    ) -> Maze:
        """
        Generates a maze using Prim's algorithm.

        Args:
            width (int): The width of the maze.
            height (int): The height of the maze.
            cords (tuple): A tuple containing the start and end coordinates of the maze.
            density (float): The density of walls or obstacles in the maze.
            user_choice_of_type_of_maze (str): Indicates whether the maze should contain different terrains.

        Returns:
            Maze: The generated maze object.
        """
        # Initialize the maze object with the given properties.
        maze = Maze(width, height, cords, density, user_choice_of_type_of_maze)

        # Set the start point of the maze.
        maze.grid[maze.start[1]][maze.start[0]].symbol = common_elem.symbol

        # Create an initial list of walls to process, adjacent to the start point.
        walls = [
            (maze.start[0] + direction.dx, maze.start[1] + direction.dy)
            for direction in Directions
            if 0 <= maze.start[0] + direction.dx < maze.width
            and 0 <= maze.start[1] + direction.dy < maze.height
        ]

        # Shuffle the list of walls to randomize the generation.
        random.shuffle(walls)

        while walls:
            wx, wy = walls.pop()
            # Ensure the current wall is within bounds and is either a boundary or a central element.
            if (
                0 < wx < maze.width - 1
                and 0 < wy < maze.height - 1
                and (
                    maze.grid[wy][wx].symbol == gran_elem.symbol
                    or maze.grid[wy][wx].symbol == central_elem.symbol
                )
            ):

                # Find neighboring cells that are part of the maze.
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
                        if user_choice_of_type_of_maze == "Да"
                        else [common_elem.symbol]
                    )
                ]

                # If the wall has exactly one neighbor, it becomes part of the maze.
                if len(neighbors) == 1:
                    if (
                        user_choice_of_type_of_maze
                        == PossibleChoiceOfTypeOfMaze.YES.value
                    ):
                        # Randomly choose a terrain type for the wall.
                        choice = random.randint(0, len(symbols) - 1)
                        maze.grid[wy][wx].symbol = symbols[choice]
                        maze.grid[wy][wx].weight = weights[choice]
                    else:
                        # Set the wall to be a common element.
                        maze.grid[wy][wx].symbol = common_elem.symbol
                        maze.grid[wy][wx].weight = common_elem.weight

                    # Add neighboring walls of the newly added cell to the list.
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
                    # Shuffle the list to ensure randomness in maze generation.
                    random.shuffle(walls)

        # Add additional open cells based on the density setting.
        koef = math.ceil((maze.width * maze.height) * (1 - maze.density + 0.1))
        for _ in range(koef):
            rand_y = random.randint(1, maze.height - 2)
            rand_x = random.randint(1, maze.width - 2)
            maze.grid[rand_y][rand_x].symbol = common_elem.symbol
            maze.grid[rand_y][rand_x].weight = common_elem.weight

        return maze
