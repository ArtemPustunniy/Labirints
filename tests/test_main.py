import unittest
from unittest.mock import patch
import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


class TestMazeFacade(unittest.TestCase):
    @patch("platform.python_version", return_value="3.10.0")
    @patch("src.labirint.maze_facade.MazeCascade.initialize_labirint")
    def test_main(self, mock_initialize_labirint, mock_python_version):
        with patch("logging.Logger.info") as mock_logger_info:
            from src.main import main  # Assuming the main function is saved in src.main

            main()

            # Check if the correct Python version is logged
            mock_logger_info.assert_called_with("3.10.0")
            # Check if the initialize_labirint method is called
            mock_initialize_labirint.assert_called_once()


if __name__ == "__main__":
    unittest.main()
