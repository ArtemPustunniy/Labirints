import unittest
from src.services.solvers.astar_solver import AstarSolver
from src.services.solvers.bfs_solver import BfsSolver
from src.services.solvers.djkstra_solver import DjkstraSolver
from src.services.solvers.solver_factory import (
    SolverFactory,
)  # Assuming SolverFactory is saved in src.services.solvers.solver_factory


class TestSolverFactory(unittest.TestCase):
    def test_get_solver_bfs(self):
        solver = SolverFactory.get_solver(1)
        self.assertIsInstance(solver, BfsSolver)

    def test_get_solver_astar(self):
        solver = SolverFactory.get_solver(2)
        self.assertIsInstance(solver, AstarSolver)

    def test_get_solver_djkstra(self):
        solver = SolverFactory.get_solver("Да")
        self.assertIsInstance(solver, DjkstraSolver)

    def test_get_solver_invalid_type(self):
        with self.assertRaises(ValueError):
            SolverFactory.get_solver(3)

    def test_factory_class_instantiation(self):
        with self.assertRaises(NotImplementedError):
            SolverFactory()


if __name__ == "__main__":
    unittest.main()
