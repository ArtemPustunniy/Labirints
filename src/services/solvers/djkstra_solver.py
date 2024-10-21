import heapq  # Importing heapq for using a priority queue
import sys  # Importing sys to use system-specific parameters and functions

from src.entities.directions import (
    Directions,
)  # Importing directions for maze navigation
from src.entities.point import (
    Point,
)  # Importing the Point class representing each cell in the maze
from src.services.solvers.solver import Solver  # Importing base Solver class
from src.utils.utils import (
    move_cursor,
)  # Importing utility function to move the cursor in the terminal


# Class implementing Dijkstra's algorithm to solve the maze
class DjkstraSolver(Solver):
    # Method to solve the maze using Dijkstra's algorithm
    def solve(self, maze):
        # Initialize costs for all cells and priority queue with the start point
        costs = self.initialize_costs(maze, maze.start, maze.height, maze.width)
        queue = self.initialize_priority_queue(maze.start)

        # Process the priority queue to calculate the shortest path
        result = self.process_queue(maze, costs, queue, maze.end)

        # If the end point is unreachable, display an error message
        if result[maze.end[0]][maze.end[1]] == sys.maxsize:
            move_cursor(0, 4)
            sys.stdout.write(
                "Был сгенерирован непроходимый лабиринт"
            )  # "An impassable maze was generated"
            return

        # Restore and return the path from the start to the end
        return self.restore_path(
            maze.grid, maze.start, maze.end, result, maze.width, maze.height
        )

    # Method to initialize the cost grid with infinite values and set the cost of the start point to 0
    def initialize_costs(self, maze, start, height, width):
        costs = [
            [sys.maxsize for _ in range(height)] for _ in range(width)
        ]  # Initialize all costs to infinity
        costs[start[0]][start[1]] = 0  # Set the cost of the start point to 0
        return costs

    # Method to initialize the priority queue with the start point
    def initialize_priority_queue(self, start):
        queue = []
        heapq.heappush(
            queue, Point(start[0], start[1], 0, " ")
        )  # Push the start point into the queue with 0 cost
        return queue

    # Method to process the priority queue and compute the shortest path costs
    def process_queue(self, maze, costs, queue, finish):
        height = maze.height
        width = maze.width

        # Continue processing while there are nodes in the queue
        while queue:
            current = heapq.heappop(queue)  # Pop the node with the lowest cost

            # If the current node is the finish point, break out of the loop
            if (current.x, current.y) == finish:
                break

            # Explore all neighboring cells based on the possible directions
            for direction in Directions:
                newX = current.x + direction.dx
                newY = current.y + direction.dy

                # Check if the new position is valid (within bounds and not blocked)
                if self.is_valid_position(maze.grid, newY, newX, height, width):
                    # Calculate the new cost for moving to the neighboring cell
                    new_cost = (
                        costs[current.x][current.y] + maze.grid[newY][newX].weight
                    )

                    # If the new cost is lower than the current cost for the cell, update it and push the cell into the queue
                    if new_cost < costs[newX][newY]:
                        costs[newX][newY] = new_cost
                        heapq.heappush(queue, maze.grid[newY][newX])
        return costs  # Return the final cost grid

    # Method to check if a given position in the maze is valid (within bounds and not a wall)
    def is_valid_position(self, grid, newY, newX, height, width):
        return (
            (0 <= newX < width)
            and (0 <= newY < height)
            and (grid[newY][newX].symbol not in ("█", "#"))
        )  # Ensure the cell is walkable

    # Method to restore the shortest path from the finish point to the start point
    def restore_path(self, grid, start, finish, costs, width, height):
        path = []
        x, y = finish

        # Trace back from the finish point to the start point using the cost grid
        while (x, y) != start:
            path.append((y, x))  # Append the current point to the path
            min_cost = costs[x][y]
            next_y, next_x = None, None

            # Check all neighboring cells to find the one with the lowest cost
            for direction in Directions:
                newY, newX = y + direction.dy, x + direction.dx
                if 0 <= newY < height and 0 <= newX < width:
                    if costs[newX][newY] < min_cost:
                        min_cost = costs[newX][newY]
                        next_y, next_x = newY, newX

            # If no valid next step is found, display an error message and return
            if next_y is None or next_x is None:
                move_cursor(0, 4)
                sys.stdout.write(
                    "Был сгенерирован непроходимый лабиринт"
                )  # "An impassable maze was generated"
                return

            # Move to the next point in the path
            y, x = next_y, next_x

        path.append(start)  # Add the start point to the path
        return path[::-1]  # Return the reversed path (from start to finish)
