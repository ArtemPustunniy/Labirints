import unittest
from unittest.mock import patch, call
import sys
from io import StringIO
from src.entities.maze import Maze
from src.services.renders.default_render import (
    DefaultRender,
)  # Assuming DefaultRender is saved in src.services.renders.default_render


class TestDefaultRender(unittest.TestCase):
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
        self.renderer = DefaultRender()

    @patch("sys.stdout", new_callable=StringIO)
    @patch("src.utils.utils.move_cursor")
    def test_render_output(self, mock_move_cursor, mock_stdout):
        self.renderer.render(self.maze, self.user_choice_of_type_of_maze)

        # Verify the start and end symbols are correctly set
        self.assertEqual(
            self.maze.grid[self.maze.start[1]][self.maze.start[0]].symbol, "A"
        )
        self.assertEqual(self.maze.grid[self.maze.end[1]][self.maze.end[0]].symbol, "B")

        # Verify the output contains the expected symbols
        output = mock_stdout.getvalue()
        for row in self.maze.grid:
            expected_row = "".join(point.symbol for point in row) + "\n"
            self.assertIn(expected_row, output)


if __name__ == "__main__":
    unittest.main()
