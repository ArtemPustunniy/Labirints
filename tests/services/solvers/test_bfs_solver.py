import unittest

from src.entities.maze import Maze
from src.services.generators.generator_factory import GeneratorFactory
from src.services.solvers.bfs_solver import BfsSolver


class TestBfsSolver(unittest.TestCase):
    def setUp(self):
        self.width = 11
        self.height = 11
        self.cords = (2, 2, 5, 5)
        self.density = 0.5
        self.user_choice_of_type_of_maze = "Нет"
        self.maze = Maze(
            self.width,
            self.height,
            self.cords,
            self.density,
            self.user_choice_of_type_of_maze,
        )
        generation_algo = 1
        self.generator = GeneratorFactory.get_generator(generator_type=generation_algo)
        self.maze = self.generator.generate(
            self.width,
            self.height,
            self.cords,
            self.density,
            self.user_choice_of_type_of_maze,
        )
        self.solver = BfsSolver()

    def test_solve(self):
        result = self.solver.solve(self.maze)
        self.assertEqual(result[0], (2, 2))
        self.assertEqual(result[-1], (5, 5))


if __name__ == "__main__":
    unittest.main()
