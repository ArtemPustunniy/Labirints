import unittest
from src.services.generators.generator_factory import GeneratorFactory
from src.services.solvers.astar_solver import (
    AstarSolver,
)  # Assuming AstarSolver is saved in src.services.solvers.astar_solver


class TestAstarSolver(unittest.TestCase):
    def setUp(self):
        self.width = 11
        self.height = 11
        self.cords = (2, 2, 5, 5)
        self.density = 0.5
        self.user_choice_of_type_of_maze = "Нет"
        generation_algo = 1
        self.generator = GeneratorFactory.get_generator(generator_type=generation_algo)
        self.maze = self.generator.generate(
            self.width,
            self.height,
            self.cords,
            self.density,
            self.user_choice_of_type_of_maze,
        )
        self.solver = AstarSolver()

    def test_solve(self):
        result = self.solver.solve(self.maze)
        self.assertEqual(result[0], (2, 2))
        self.assertEqual(result[-1], (5, 5))

    def test_heuristic(self):
        def heuristic(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        self.assertEqual(heuristic((0, 0), (1, 1)), 2)
        self.assertEqual(heuristic((2, 3), (5, 1)), 5)
        self.assertEqual(heuristic((0, 0), (0, 0)), 0)
        self.assertEqual(heuristic((-1, -1), (1, 1)), 4)


if __name__ == "__main__":
    unittest.main()
