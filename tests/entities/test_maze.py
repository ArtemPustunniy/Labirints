import unittest
import sys
from src.entities.point import gran_elem, central_elem
from src.entities.maze import (
    Maze,
)  # Assuming the Maze class is saved in src.entities.maze


class TestMaze(unittest.TestCase):
    def setUp(self):
        self.width = 5
        self.height = 5
        self.cords = (1, 1, 3, 3)
        self.density = 0.5
        self.user_choice_of_type_of_maze = "Нет"
        self.maze = Maze(
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
        self.assertEqual(self.maze.end, (3, 3))
        self.assertEqual(self.maze.density, self.density)
        self.assertEqual(
            self.maze.user_choice_of_type_of_maze, self.user_choice_of_type_of_maze
        )
        self.assertEqual(self.maze.delta, 100)

    def test_grid_initialization(self):
        # Test that grid boundary points are set to gran_elem
        for i in range(self.height):
            for j in range(self.width):
                if i == 0 or i == self.height - 1 or j == 0 or j == self.width - 1:
                    self.assertEqual(self.maze.grid[i][j].symbol, gran_elem.symbol)
                    self.assertEqual(self.maze.grid[i][j].weight, sys.maxsize)
                else:
                    self.assertEqual(self.maze.grid[i][j].symbol, central_elem.symbol)
                    self.assertEqual(self.maze.grid[i][j].weight, sys.maxsize)

    def test_start_and_end_points(self):
        self.assertEqual(self.maze.start, (1, 1))
        self.assertEqual(self.maze.end, (3, 3))


if __name__ == "__main__":
    unittest.main()
