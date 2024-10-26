from collections import deque

from src.entities.directions import Directions
from src.entities.point import common_elem
from src.services.solvers.solver import Solver


class BfsSolver(Solver):
    """
    Class implementing the BFS (Breadth-First Search) algorithm to solve a maze.
    """

    def solve(self, maze) -> list:
        """
        Solves the maze using the BFS algorithm.

        Args:
            maze: The maze object to solve.

        Returns:
            list: The path from start to end in the maze.
        """
        start, end = maze.start, maze.end
        queue = deque([start])
        visited = {start}
        parent = {start: None}

        while queue:
            current = queue.popleft()

            if current == end:
                break

            for direction in Directions:
                y, x = current[1] + direction.dy, current[0] + direction.dx

                if (0 <= y < maze.height) and (0 <= x < maze.width):
                    if (
                        maze.grid[y][x].symbol == common_elem.symbol
                        and (x, y) not in visited
                    ) or (
                        maze.grid[y][x].symbol in ("A", "B") and (x, y) not in visited
                    ):
                        queue.append((x, y))
                        visited.add((x, y))
                        parent[(x, y)] = current

        path = []
        current = end
        while current is not None:
            path.append(current[::-1])
            current = parent[current]
        path.reverse()

        return path
