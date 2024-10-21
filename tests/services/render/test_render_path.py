import unittest
from unittest.mock import patch
from io import StringIO
from src.entities.maze import Maze
from src.services.renders.render_path import (
    RenderPath,
)  # Assuming RenderPath is saved in src.services.renders.render_path


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
    def test_render_path(self, mock_sleep, mock_move_cursor, mock_stdout):
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


if __name__ == "__main__":
    unittest.main()
