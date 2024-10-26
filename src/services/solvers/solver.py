from abc import ABC, abstractmethod
from enum import Enum


class Solver(ABC):
    """
    Abstract base class for a maze-solving algorithm.
    """

    @abstractmethod
    def solve(self, maze) -> None:
        """
        Abstract method that must be implemented by all subclasses to solve the maze.
        """
        pass


class AvailableSolvers(Enum):
    """
    Enum representing the available solvers (algorithms) for solving the maze.

    Attributes:
        BfsSolver (int): Breadth-First Search (BFS) algorithm.
        AstarSolver (int): A* search algorithm.
        DjkstraSolver (str): Dijkstra's algorithm (represented by 'Да' for specific user input handling).
    """
    BfsSolver = 1
    AstarSolver = 2
    DjkstraSolver = "Да"
