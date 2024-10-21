import unittest
from abc import ABC, abstractmethod
from src.services.solvers.solver import (
    Solver,
)  # Предполагается, что Solver сохранен в src.services.solvers.solver


class TestSolverAbstract(unittest.TestCase):
    def test_abstract_solve_method(self):
        with self.assertRaises(TypeError):
            solver = (
                Solver()
            )  # Попытка создать экземпляр абстрактного класса должна вызвать TypeError

    def test_subclass_implementation(self):
        class TestConcreteSolver(Solver):
            def solve(self, maze):
                return True

        solver = TestConcreteSolver()
        result = solver.solve(None)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
