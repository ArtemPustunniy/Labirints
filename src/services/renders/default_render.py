import sys  # Importing the system module to interact with standard input and output

from src.services.renders.render import (
    Render,
)  # Importing the base Render class for rendering the maze
from src.utils.utils import (
    move_cursor,
)  # Importing a utility function to move the cursor in the terminal


# Class responsible for rendering the maze in its default form
class DefaultRender(Render):
    # Method to render the maze along with the user's choice of maze type and optionally a path
    def render(self, maze, user_choice_of_type_of_maze, path: [] = None):
        # Set the symbol 'A' for the starting point of the maze
        maze.grid[maze.start[1]][maze.start[0]].symbol = "A"
        # Set the symbol 'B' for the ending point of the maze
        maze.grid[maze.end[1]][maze.end[0]].symbol = "B"

        # Iterate over each row of the maze grid
        for y, row in enumerate(maze.grid):
            # Move the cursor to the appropriate position for rendering each row
            move_cursor(maze.delta + 1, y + 1)
            # Render the symbols for each point in the row and write them to the output
            sys.stdout.write("".join(point.symbol for point in row) + "\n")
        # Flush the output to ensure the maze is fully rendered on the screen
        sys.stdout.flush()
