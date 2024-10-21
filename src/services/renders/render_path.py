import sys  # Importing system module to interact with input and output
import time  # Importing time module for adding delays during rendering

from src.entities.maze import (
    PossibleChoiceOfTypeOfMaze,
)  # Importing enumeration for different types of mazes
from src.entities.point import (
    common_elem,
)  # Importing common element (such as walls or floors) from the point entity
from src.services.renders.render import Render  # Importing base Render class
from src.utils.utils import (
    move_cursor,
)  # Importing utility function to move the cursor in the terminal

# Class responsible for rendering the path through the maze


class RenderPath(Render):
    # Method to render the path in the maze based on the user's choice of maze type and optional path
    def render(self, maze, user_choice_of_type_of_maze, path: [] = None):
        # If no path is provided, exit the method
        if path is None:
            return
        # Iterate over each coordinate in the path
        for x, y in path:
            # Skip the start and end points of the maze
            if (y, x) == maze.start or (y, x) == maze.end:
                continue
            # Check if the user chose to render different types of surfaces in the maze
            if user_choice_of_type_of_maze == PossibleChoiceOfTypeOfMaze.YES.value:
                # Move the cursor to the appropriate position
                move_cursor(y + maze.delta + 1, x + 1)
                # Check if the current point is a common element (like a wall), and render it in red ('*')
                if maze.grid[x][y].symbol == common_elem.symbol:
                    sys.stdout.write(
                        "\033[31m*\033[0m"
                    )  # Write red '*' to represent the path
                else:
                    # Otherwise, render the current point's symbol in red
                    sys.stdout.write(f"\033[31m{maze.grid[x][y].symbol}\033[0m")
                # Flush the output to immediately show the change
                sys.stdout.flush()
                # Add a small delay to create a visual effect of the path being drawn
                time.sleep(0.05)
            else:
                # If the user didn't choose different surfaces, render the path with red '*' as the default symbol
                move_cursor(y + maze.delta + 1, x + 1)
                sys.stdout.write("\033[31m*\033[0m")  # Write red '*' for the path
                sys.stdout.flush()
                time.sleep(0.05)  # Add delay for visual effect
