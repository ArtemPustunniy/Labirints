import heapq
import sys

from src.entities.directions import Directions
from src.entities.point import Point
from src.services.solvers.solver import Solver
from src.utils.utils import move_cursor


class DjkstraSolver(Solver):
    """
    Class implementing Dijkstra's algorithm to solve the maze.
    """

    def solve(self, maze) -> list:
        """
        Solves the maze using Dijkstra's algorithm.

        Args:
            maze: The maze object to solve.

        Returns:
            list: The path from the start to the end of the maze.
        """
        costs = self.initialize_costs(maze, maze.start, maze.height, maze.width)
        queue = self.initialize_priority_queue(maze.start)

        result = self.process_queue(maze, costs, queue, maze.end)

        if result[maze.end[0]][maze.end[1]] == sys.maxsize:
            move_cursor(0, 4)
            sys.stdout.write("An impassable maze was generated")
            return

        return self.restore_path(
            maze.grid, maze.start, maze.end, result, maze.width, maze.height
        )

    def initialize_costs(self, maze, start, height, width) -> list:
        """
        Initializes the cost grid with infinite values and sets the cost of the start point to zero.

        Args:
            maze: The maze object.
            start: The starting coordinates.
            height: The height of the maze.
            width: The width of the maze.

        Returns:
            list: A 2D list representing the cost grid.
        """
        costs = [
            [sys.maxsize for _ in range(height)] for _ in range(width)
        ]
        costs[start[0]][start[1]] = 0
        return costs

    def initialize_priority_queue(self, start) -> list:
        """
        Initializes the priority queue with the start point.

        Args:
            start: The starting coordinates.

        Returns:
            list: The priority queue initialized with the start point.
        """
        queue = []
        heapq.heappush(queue, Point(start[0], start[1], 0, " "))
        return queue

    def process_queue(self, maze, costs, queue, finish) -> list:
        """
        Processes the priority queue to compute the shortest path costs.

        Args:
            maze: The maze object.
            costs: The cost grid.
            queue: The priority queue.
            finish: The ending coordinates.

        Returns:
            list: The updated cost grid after processing.
        """
        height = maze.height
        width = maze.width

        while queue:
            current = heapq.heappop(queue)

            if (current.x, current.y) == finish:
                break

            for direction in Directions:
                newX = current.x + direction.dx
                newY = current.y + direction.dy

                if self.is_valid_position(maze.grid, newY, newX, height, width):
                    new_cost = costs[current.x][current.y] + maze.grid[newY][newX].weight

                    if new_cost < costs[newX][newY]:
                        costs[newX][newY] = new_cost
                        heapq.heappush(queue, maze.grid[newY][newX])
        return costs

    def is_valid_position(self, grid, newY, newX, height, width) -> bool:
        """
        Checks if a given position in the maze is valid (within bounds and not a wall).

        Args:
            grid: The maze grid.
            newY: The y-coordinate to check.
            newX: The x-coordinate to check.
            height: The height of the maze.
            width: The width of the maze.

        Returns:
            bool: True if the position is valid, False otherwise.
        """
        return (
            (0 <= newX < width)
            and (0 <= newY < height)
            and (grid[newY][newX].symbol not in ("█", "#"))
        )

    def restore_path(self, grid, start, finish, costs, width, height):
        """
        Restores the shortest path from the finish point to the start point.

        Args:
            grid: The maze grid.
            start: The starting coordinates.
            finish: The ending coordinates.
            costs: The cost grid.
            width: The width of the maze.
            height: The height of the maze.

        Returns:
            list: The path from start to finish.
        """
        path = []
        x, y = finish

        while (x, y) != start:
            path.append((y, x))
            min_cost = costs[x][y]
            next_y, next_x = None, None

            for direction in Directions:
                newY, newX = y + direction.dy, x + direction.dx
                if 0 <= newY < height and 0 <= newX < width:
                    if costs[newX][newY] < min_cost:
                        min_cost = costs[newX][newY]
                        next_y, next_x = newY, newX

            if next_y is None or next_x is None:
                move_cursor(0, 4)
                sys.stdout.write("An impassable maze was generated")
                return

            y, x = next_y, next_x

        path.append(start)
        return path[::-1]
