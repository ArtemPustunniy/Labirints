import unittest
from src.entities.point import (
    common_elem,
    symbols,
)
from src.services.generators.dfs_generator import (
    DfsGenerator,
)  # Assuming DfsGenerator is saved in src.services.generators.dfs_generator


class TestDfsGenerator(unittest.TestCase):
    def setUp(self):
        self.width = 7
        self.height = 7
        self.cords = (1, 1, 5, 5)
        self.density = 0.5
        self.user_choice_of_type_of_maze = "Нет"
        self.generator = DfsGenerator()
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
            self.maze.user_choice_of_type_of_maze, self.user_choice_of_type_of_maze
        )

    def test_start_and_end_points(self):
        self.assertEqual(
            self.maze.grid[self.maze.start[1]][self.maze.start[0]].symbol,
            common_elem.symbol,
        )
        self.assertEqual(
            self.maze.grid[self.maze.end[1]][self.maze.end[0]].symbol,
            common_elem.symbol,
        )
        self.assertEqual(
            self.maze.grid[self.maze.start[1]][self.maze.start[0]].weight,
            common_elem.weight,
        )
        self.assertEqual(
            self.maze.grid[self.maze.end[1]][self.maze.end[0]].weight,
            common_elem.weight,
        )

    def test_path_generation(self):
        path_count = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.maze.grid[i][j].symbol == common_elem.symbol:
                    path_count += 1
        self.assertGreater(path_count, 0, "Path should be generated in the maze.")

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
