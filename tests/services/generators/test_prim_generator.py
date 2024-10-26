import unittest
import random
from src.entities.point import common_elem, symbols
from src.services.generators.prim_generator import (
    PrimGenerator,
)  # Assuming PrimGenerator is saved in src.services.generators.prim_generator


class TestPrimGenerator(unittest.TestCase):
    def setUp(self):
        random.seed(0)  # Setting seed for reproducibility
        self.width = 7
        self.height = 7
        self.cords = (1, 1, 5, 5)
        self.density = 0.5
        self.user_choice_of_type_of_maze = "Нет"
        self.generator = PrimGenerator()
        self.maze = self.generator.generate(
            self.width,
            self.height,
            self.cords,
            self.density,
            self.user_choice_of_type_of_maze,
        )

    def test_initialization(self):
        self.assertEqual(self.maze.width, self.width)
        self.assertEqual(self.maze.height, self.height)
        self.assertEqual(self.maze.start, (1, 1))
        self.assertEqual(self.maze.end, (5, 5))
        self.assertEqual(self.maze.density, self.density)
        self.assertEqual(
            self.maze.diff_types_of_surfaces, self.user_choice_of_type_of_maze
        )

    def test_maze_connectivity(self):
        visited = set()
        stack = [self.maze.start]

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                x, y = current
                neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
                for nx, ny in neighbors:
                    if 0 <= ny < self.height and 0 <= nx < self.width:
                        if self.maze.grid[ny][nx].symbol == common_elem.symbol:
                            stack.append((nx, ny))

        self.assertIn(
            self.maze.end, visited, "End point should be reachable from start point."
        )

    def test_user_choice_of_type_of_maze(self):
        if self.user_choice_of_type_of_maze == "Да":
            unique_symbols = set(symbols)
            generated_symbols = {
                self.maze.grid[i][j].symbol
                for i in range(self.height)
                for j in range(self.width)
            }
            self.assertTrue(
                unique_symbols & generated_symbols,
                "Maze should contain different types of surfaces when user_choice_of_type_of_maze is 'Да'.",
            )


if __name__ == "__main__":
    unittest.main()
