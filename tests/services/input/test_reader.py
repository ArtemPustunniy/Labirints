import unittest
from unittest.mock import Mock
import sys
from io import StringIO
from src.services.input.reader import Reader


class TestReader(unittest.TestCase):

    def setUp(self):
        self.original_stdout = sys.stdout
        sys.stdout = StringIO()
        self.info_method_mock = Mock()

    def tearDown(self):
        sys.stdout = self.original_stdout

    def test_input_value_valid_input(self):
        self.info_method_mock.side_effect = [5]
        result = Reader.input_value(self.info_method_mock, min_value=1, max_value=10)
        self.assertEqual(result, 5)

    def test_input_value_out_of_bounds(self):
        self.info_method_mock.side_effect = [15, 5]
        result = Reader.input_value(self.info_method_mock, min_value=1, max_value=10)
        self.assertEqual(result, 5)
        output = sys.stdout.getvalue()
        self.assertIn("Ошибка: введите допустимое значение", output)

    def test_input_value_value_error(self):
        self.info_method_mock.side_effect = [ValueError, 5]
        result = Reader.input_value(self.info_method_mock, min_value=1, max_value=10)
        self.assertEqual(result, 5)
        output = sys.stdout.getvalue()
        self.assertIn("Ошибка: введите допустимое значение", output)


if __name__ == "__main__":
    unittest.main()
