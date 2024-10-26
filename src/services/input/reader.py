import sys

from src.utils.utils import clear_screen, move_cursor


class Reader:
    """Class for handling user input with value validation."""

    @staticmethod
    def input_value(
        info_method,
        min_value=None,
        max_value=None,
        error_message="Ошибка: введите допустимое значение",
    ):
        """
        Gets a value from the user with optional minimum and maximum validation.

        Args:
            info_method (callable): Method to obtain input from the user (e.g., input()).
            min_value (optional): Minimum acceptable value.
            max_value (optional): Maximum acceptable value.
            error_message (str): Message displayed when the input is invalid.

        Returns:
            The validated user input.
        """
        while True:
            try:
                value = info_method()
                if (min_value is None or value >= min_value) and (
                    max_value is None or value <= max_value
                ):
                    return value
                else:
                    clear_screen()
                    move_cursor(0, 1)
                    sys.stdout.write(error_message + "\n")
            except ValueError:
                clear_screen()
                move_cursor(0, 1)
                sys.stdout.write(error_message + "\n")
