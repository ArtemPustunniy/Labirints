import unittest
from unittest.mock import patch
from io import StringIO
from src.entities.maze import Maze
from src.services.renders.render_path import RenderPath


class TestRenderPath(unittest.TestCase):
    def setUp(self):
        self.width = 5
        self.height = 5
        self.cords = (1, 1, 3, 3)
        self.density = 0.5
        self.user_choice_of_type_of_maze = "Да"
        self.maze = Maze(
            self.width,
            self.height,
            self.cords,
            self.density,
            self.user_choice_of_type_of_maze,
        )
        self.path = [(1, 2), (2, 2), (3, 2)]
        self.renderer = RenderPath()

    @patch("sys.stdout", new_callable=StringIO)
    @patch("src.utils.utils.move_cursor")
    @patch("time.sleep", return_value=None)  # To avoid delay during testing
    def test_render(self, mock_sleep, mock_move_cursor, mock_stdout):
        # Test basic rendering
        self.renderer.render(self.maze, self.user_choice_of_type_of_maze, self.path)

        # Verify the output contains the expected symbols
        output = mock_stdout.getvalue()
        for x, y in self.path:
            if (y, x) == self.maze.start or (y, x) == self.maze.end:
                continue
            if self.maze.grid[x][y].symbol == " ":
                self.assertIn("\033[31m*\033[0m", output)
            else:
                self.assertIn(f"\033[31m{self.maze.grid[x][y].symbol}\033[0m", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_empty_path(self, mock_stdout):
        # Test rendering with an empty path
        empty_path = []
        self.renderer.render(self.maze, self.user_choice_of_type_of_maze, empty_path)

        output = mock_stdout.getvalue()
        self.assertNotIn("\033[31m*\033[0m", output)  # No path should be rendered

    @patch("sys.stdout", new_callable=StringIO)
    def test_render_minimal_maze(self, mock_stdout):
        # Test rendering with a minimal 2x2 maze
        small_maze = Maze(2, 2, (0, 0, 1, 1), 0.0, "Нет")
        small_path = [(0, 1), (1, 1)]
        self.renderer.render(small_maze, "Нет", small_path)

        output = mock_stdout.getvalue()
        self.assertIn("\033[31m*\033[0m", output)  # Path should be rendered in minimal maze


if __name__ == "__main__":
    unittest.main()
