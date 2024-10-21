import heapq  # Importing heapq to use a priority queue for the A* algorithm

from src.entities.directions import (
    Directions,
)  # Importing directions (e.g., up, down, left, right) for maze navigation
from src.services.solvers.solver import Solver  # Importing the base Solver class


# Class implementing the A* algorithm to solve a maze
class AstarSolver(Solver):
    # Method that solves the maze using the A* pathfinding algorithm
    def solve(self, maze):
        # Inner function to calculate the heuristic (Manhattan distance) between two points
        def heuristic(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        # Start and end points of the maze
        start, end = maze.start, maze.end
        queue = []  # Priority queue to store nodes to explore
        heapq.heappush(
            queue, (0, start)
        )  # Initialize the queue with the start point and zero cost
        parent = {
            start: None
        }  # Dictionary to track the parent of each node for path reconstruction
        cost = {start: 0}  # Dictionary to store the cost of reaching each node

        # Loop until all nodes are processed or the end point is reached
        while queue:
            _, current = heapq.heappop(
                queue
            )  # Get the node with the lowest priority (cost + heuristic)

            # If the end point is reached, exit the loop
            if current == end:
                break

            # Explore each possible direction from the current node
            for direction in Directions:
                x, y = (
                    current[0] + direction.dx,
                    current[1] + direction.dy,
                )  # Calculate the new coordinates
                # Check if the new coordinates are valid (within bounds and on a walkable cell)
                if (
                    0 <= x < maze.width
                    and 0 <= y < maze.height
                    and (
                        maze.grid[y][x].symbol == " "
                        or maze.grid[y][x].symbol == "A"
                        or maze.grid[y][x].symbol == "B"
                    )
                ):
                    new_cost = (
                        cost[current] + 1
                    )  # Calculate the cost of moving to the new cell
                    # If the new cell hasn't been visited or a cheaper path is found
                    if (x, y) not in cost or new_cost < cost[(x, y)]:
                        cost[(x, y)] = new_cost  # Update the cost to reach this cell
                        priority = new_cost + heuristic(
                            end, (x, y)
                        )  # Calculate the priority using cost + heuristic
                        heapq.heappush(
                            queue, (priority, (x, y))
                        )  # Add the new cell to the queue with its priority
                        parent[(x, y)] = (
                            current  # Record the current cell as the parent of the new cell
                        )

        # Reconstruct the path by tracing back from the end point to the start point
        path = []
        current = end
        while current is not None:
            path.append(
                current[::-1]
            )  # Add the current node to the path, reversing the coordinates (for proper display)
            current = parent[current]  # Move to the parent of the current node
        path.reverse()  # Reverse the path to get the correct order from start to end

        return path  # Return the final path from start to end
