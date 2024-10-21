import unittest
from unittest.mock import patch
from io import StringIO
import sys
from src.services.input.input import InputHandler
from src.entities.maze import PossibleChoiceOfTypeOfMaze


class TestInputHandler(unittest.TestCase):

    def setUp(self):
        self.handler = InputHandler()
        self.original_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.original_stdout

    @patch("builtins.input", side_effect=["5", "5"])
    def test_input_sizes(self, mock_input):
        width, height = self.handler.input_sizes()
        self.assertEqual(width, 5)
        self.assertEqual(height, 5)

    @patch("builtins.input", side_effect=["1", "1", "3", "3"])
    def test_input_cords_of_letters(self, mock_input):
        result = self.handler.input_cords_of_letters(5, 5)
        self.assertEqual(result, (1, 1, 3, 3))

    @patch("builtins.input", side_effect=["0.5"])
    def test_input_density(self, mock_input):
        result = self.handler.input_density()
        self.assertEqual(result, 0.5)

    @patch("builtins.input", side_effect=["Да"])
    def test_input_type_of_maze_yes(self, mock_input):
        result = self.handler.input_type_of_maze()
        self.assertEqual(result, "Да")

    @patch("builtins.input", side_effect=["Нет"])
    def test_input_type_of_maze_no(self, mock_input):
        result = self.handler.input_type_of_maze()
        self.assertEqual(result, "Нет")

    @patch("builtins.input", side_effect=["2"])
    def test_input_generation_algo(self, mock_input):
        result = self.handler.input_generation_algo()
        self.assertEqual(result, 2)

    @patch("builtins.input", side_effect=["1"])
    def test_input_solve_algo_no(self, mock_input):
        result = self.handler.input_solve_algo(PossibleChoiceOfTypeOfMaze.NO.value)
        self.assertEqual(result, 1)

    @patch("builtins.input", side_effect=["Да"])
    def test_input_solve_algo_yes(self, mock_input):
        result = self.handler.input_solve_algo(PossibleChoiceOfTypeOfMaze.YES.value)
        self.assertEqual(result, "Да")


if __name__ == "__main__":
    unittest.main()
