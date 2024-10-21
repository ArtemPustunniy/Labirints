import os
import unittest
from unittest.mock import patch, call
import sys
from io import StringIO
from src.utils.utils import (
    clear_screen,
    clear_input_line,
    move_cursor,
)  # Assuming these functions are saved in src.utils.utils


class TestUtilsFunctions(unittest.TestCase):
    @patch("os.system")
    def test_clear_screen(self, mock_os_system):
        clear_screen()
        if os.name == "nt":
            mock_os_system.assert_called_with("cls")
        else:
            mock_os_system.assert_called_with("clear")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("src.utils.utils.move_cursor")
    def test_clear_input_line(self, mock_move_cursor, mock_stdout):
        clear_input_line()
        output = mock_stdout.getvalue()
        self.assertIn("                                         ", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_move_cursor(self, mock_stdout):
        move_cursor(10, 5)
        output = mock_stdout.getvalue()
        self.assertIn("\033[5;10H", output)


if __name__ == "__main__":
    unittest.main()
