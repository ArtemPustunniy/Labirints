from abc import (
    ABC,
    abstractmethod,
)  # Importing ABC and abstractmethod to define an abstract base class
from enum import Enum  # Importing Enum to define a set of named constants


# Abstract base class for a maze-solving algorithm
class Solver(ABC):
    # Abstract method that must be implemented by all subclasses to solve the maze
    @abstractmethod
    def solve(self, maze):
        pass  # To be defined by concrete solver classes


# Enum representing the available solvers (algorithms) for solving the maze
class AvailableSolvers(Enum):
    BfsSolver = 1  # Breadth-First Search (BFS) algorithm
    AstarSolver = 2  # A* search algorithm
    DjkstraSolver = "Да"  # Dijkstra's algorithm (represented by "Да" for a specific reason, perhaps for user input)
