from collections import deque  # Importing deque for efficient queue operations

from src.entities.directions import (
    Directions,
)  # Importing directions (up, down, left, right) for maze traversal
from src.entities.point import (
    common_elem,
)  # Importing common element (such as walls or floors) for checking cell types
from src.services.solvers.solver import Solver  # Importing base Solver class


# Class implementing the BFS (Breadth-First Search) algorithm to solve a maze
class BfsSolver(Solver):
    # Method to solve the maze using the BFS algorithm
    def solve(self, maze):
        # Initializing start and end points of the maze
        start, end = maze.start, maze.end
        queue = deque(
            [start]
        )  # Queue for BFS traversal, initialized with the start point
        visited = {
            start
        }  # Set to track visited nodes, initialized with the start point
        parent = {
            start: None
        }  # Dictionary to track parent nodes for path reconstruction

        # BFS loop that runs until the queue is empty or the end point is reached
        while queue:
            current = queue.popleft()  # Dequeue the first element in the queue

            # If the current node is the end point, break the loop
            if current == end:
                break

            # Explore each possible direction from the current node
            for direction in Directions:
                y, x = (
                    current[1] + direction.dy,
                    current[0] + direction.dx,
                )  # Calculate new coordinates

                # Check if the new coordinates are within maze bounds
                if (0 <= y < maze.height) and (0 <= x < maze.width):
                    # Check if the new cell is a walkable space (common element) or the start/end points, and hasn't been visited
                    if (
                        maze.grid[y][x].symbol == common_elem.symbol
                        and (x, y) not in visited
                    ) or (
                        maze.grid[y][x].symbol in ("A", "B") and (x, y) not in visited
                    ):
                        queue.append((x, y))  # Enqueue the new cell
                        visited.add((x, y))  # Mark the new cell as visited
                        parent[(x, y)] = (
                            current  # Set the current cell as the parent of the new cell
                        )

        # Reconstruct the path by tracing back from the end point to the start point
        path = []
        current = end
        while current is not None:
            path.append(
                current[::-1]
            )  # Add the current node to the path, reversing coordinates (for proper display)
            current = parent[current]  # Move to the parent of the current node
        path.reverse()  # Reverse the path to get the correct order from start to end

        return path  # Return the final path from start to end
