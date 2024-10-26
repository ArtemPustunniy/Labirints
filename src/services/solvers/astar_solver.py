import heapq

from src.entities.directions import Directions
from src.services.solvers.solver import Solver


class AstarSolver(Solver):
    """
    Class implementing the A* algorithm to solve a maze.
    """

    def solve(self, maze) -> list:
        """
        Solves the maze using the A* pathfinding algorithm.

        Args:
            maze: The maze object to solve.

        Returns:
            list: The path from start to end in the maze.
        """
        def heuristic(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        start, end = maze.start, maze.end
        queue = []
        heapq.heappush(queue, (0, start))
        parent = {start: None}
        cost = {start: 0}

        while queue:
            _, current = heapq.heappop(queue)

            if current == end:
                break

            for direction in Directions:
                x, y = current[0] + direction.dx, current[1] + direction.dy

                if (0 <= x < maze.width and 0 <= y < maze.height and
                    (maze.grid[y][x].symbol == " " or maze.grid[y][x].symbol == "A" or maze.grid[y][x].symbol == "B")):
                    new_cost = cost[current] + 1
                    if (x, y) not in cost or new_cost < cost[(x, y)]:
                        cost[(x, y)] = new_cost
                        priority = new_cost + heuristic(end, (x, y))
                        heapq.heappush(queue, (priority, (x, y)))
                        parent[(x, y)] = current

        path = []
        current = end
        while current is not None:
            path.append(current[::-1])
            current = parent[current]
        path.reverse()

        return path
