from src.services.solvers.astar_solver import AstarSolver  # Importing the A* solver
from src.services.solvers.bfs_solver import BfsSolver  # Importing the BFS solver
from src.services.solvers.djkstra_solver import (
    DjkstraSolver,
)  # Importing the Dijkstra solver
from src.services.solvers.solver import (
    AvailableSolvers,
)  # Importing the enum representing available solvers


# Factory class for creating instances of different solvers based on the selected type
class SolverFactory:
    # Static method to get the appropriate solver instance based on the solver type
    @staticmethod
    def get_solver(solver_type):
        # Match the solver type and return the corresponding solver instance
        if solver_type == AvailableSolvers.BfsSolver.value:
            return BfsSolver()  # Return BFS solver instance
        elif solver_type == AvailableSolvers.AstarSolver.value:
            return AstarSolver()  # Return A* solver instance
        elif solver_type == AvailableSolvers.DjkstraSolver.value:
            return DjkstraSolver()  # Return Dijkstra solver instance
        else:
            # Raise an error if an unknown solver type is provided
            raise ValueError(f"Unknown generator type: {solver_type}")

    # Constructor is disabled to prevent instantiation of this class
    def __init__(self):
        raise NotImplementedError(
            "This class cannot be instantiated"
        )  # Prevent instantiation
