from src.services.solvers.astar_solver import AstarSolver
from src.services.solvers.bfs_solver import BfsSolver
from src.services.solvers.djkstra_solver import DjkstraSolver
from src.services.solvers.solver import AvailableSolvers, Solver


class SolverFactory:
    """
    Factory class for creating instances of different solvers based on the selected type.
    """

    @staticmethod
    def get_solver(solver_type) -> Solver:
        """
        Returns the appropriate solver instance based on the solver type.

        Args:
            solver_type: The type of solver to create.

        Returns:
            An instance of the solver corresponding to the solver_type.

        Raises:
            ValueError: If an unknown solver type is provided.
        """
        if solver_type == AvailableSolvers.BfsSolver.value:
            return BfsSolver()
        elif solver_type == AvailableSolvers.AstarSolver.value:
            return AstarSolver()
        elif solver_type == AvailableSolvers.DjkstraSolver.value:
            return DjkstraSolver()
        else:
            raise ValueError(f"Unknown generator type: {solver_type}")

    def __init__(self):
        """
        Disables instantiation of this class.
        """
        raise NotImplementedError("This class cannot be instantiated")
