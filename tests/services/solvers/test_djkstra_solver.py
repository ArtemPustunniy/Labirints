import unittest
import sys
from src.services.generators.generator_factory import GeneratorFactory
from src.services.solvers.djkstra_solver import DjkstraSolver


class TestDijkstraSolver(unittest.TestCase):

    def setUp(self):
        self.width = 11
        self.height = 11
        self.cords = (2, 2, 5, 5)
        self.density = 0.5
        self.user_choice_of_type_of_maze = "Да"
        generation_algo = 1
        self.generator = GeneratorFactory.get_generator(generator_type=generation_algo)
        self.maze = self.generator.generate(
            self.width,
            self.height,
            self.cords,
            self.density,
            self.user_choice_of_type_of_maze,
        )
        self.solver = DjkstraSolver()

    def test_initialize_costs(self):
        costs = self.solver.initialize_costs(
            self.maze, self.maze.start, self.maze.height, self.maze.width
        )
        self.assertEqual(costs[self.maze.start[0]][self.maze.start[1]], 0)
        self.assertEqual(costs[1][1], sys.maxsize)

    def test_initialize_priority_queue(self):
        queue = self.solver.initialize_priority_queue(self.maze.start)
        self.assertEqual(len(queue), 1)
        self.assertEqual(queue[0].x, self.maze.start[0])
        self.assertEqual(queue[0].y, self.maze.start[1])
        self.assertEqual(queue[0].weight, 0)

    def test_is_valid_position(self):
        self.assertTrue(
            self.solver.is_valid_position(
                self.maze.grid, 1, 1, self.maze.height, self.maze.width
            )
        )
        self.assertTrue(
            self.solver.is_valid_position(
                self.maze.grid, 2, 2, self.maze.height, self.maze.width
            )
        )  # Obstacle
        self.assertFalse(
            self.solver.is_valid_position(
                self.maze.grid, -1, 0, self.maze.height, self.maze.width
            )
        )  # Out of bounds

    def test_process_queue(self):
        costs = self.solver.initialize_costs(
            self.maze, self.maze.start, self.maze.height, self.maze.width
        )
        queue = self.solver.initialize_priority_queue(self.maze.start)
        result = self.solver.process_queue(self.maze, costs, queue, self.maze.end)

        # Checking if the end point has a valid cost
        self.assertNotEqual(result[self.maze.end[0]][self.maze.end[1]], sys.maxsize)

    def test_restore_path(self):
        costs = self.solver.initialize_costs(
            self.maze, self.maze.start, self.maze.height, self.maze.width
        )
        queue = self.solver.initialize_priority_queue(self.maze.start)
        self.solver.process_queue(self.maze, costs, queue, self.maze.end)
        path = self.solver.restore_path(
            self.maze.grid,
            self.maze.start,
            self.maze.end,
            costs,
            self.maze.width,
            self.maze.height,
        )

        self.assertEqual(path[-1], self.maze.end)


if __name__ == "__main__":
    unittest.main()
