import unittest
from unittest.mock import patch
from io import StringIO
from src.services.input.output_info import (
    OutputInfoHandler,
)  # Assuming OutputHandler is saved in src.services.input.output


class TestOutputHandler(unittest.TestCase):
    def setUp(self):
        self.output_handler = OutputInfoHandler()

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value="1")
    @patch("src.utils.utils.move_cursor")
    def test_print_input(self, mock_move_cursor, mock_input, mock_stdout):
        choice = self.output_handler.print_input()
        self.assertEqual(choice, 1)
        output = mock_stdout.getvalue()
        self.assertIn("Выберите алгоритм генерации лабиринта:", output)
        self.assertIn("1. DFS (поиск в глубину)", output)
        self.assertIn("2. Прим", output)
        self.assertIn("3. Краскал", output)

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value="2")
    @patch("src.utils.utils.move_cursor")
    def test_print_output(self, mock_move_cursor, mock_input, mock_stdout):
        choice = self.output_handler.print_output()
        self.assertEqual(choice, 2)
        output = mock_stdout.getvalue()
        self.assertIn("1. BFS (поиск в ширину)", output)
        self.assertIn("2. A* (поиск A-star)", output)

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value="Да")
    @patch("src.utils.utils.move_cursor")
    def test_print_output_weight(self, mock_move_cursor, mock_input, mock_stdout):
        choice = self.output_handler.print_output_weight()
        self.assertEqual(choice, "Да")
        output = mock_stdout.getvalue()
        self.assertIn("Djkstra (алгоритм Дейкстры)", output)

    @patch("sys.stdout", new_callable=StringIO)
    @patch("src.utils.utils.move_cursor")
    def test_print_start_cords(self, mock_move_cursor, mock_stdout):
        self.output_handler.print_start_cords()
        output = mock_stdout.getvalue()
        self.assertIn("Выберите расположение начальной и конечной точек", output)
        self.assertIn("Координаты начальной точки:", output)

    @patch("sys.stdout", new_callable=StringIO)
    @patch("src.utils.utils.move_cursor")
    def test_print_end_cords(self, mock_move_cursor, mock_stdout):
        self.output_handler.print_end_cords()
        output = mock_stdout.getvalue()
        self.assertIn("Выберите расположение начальной и конечной точек", output)
        self.assertIn("Координаты конечной точки:", output)


if __name__ == "__main__":
    unittest.main()
