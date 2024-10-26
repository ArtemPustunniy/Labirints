import enum

from src.entities.maze import DiffTypesOfSurfaces
from src.services.input.reader import Reader
from src.utils.utils import clear_input_line, move_cursor
from src.services.input.output_info import OutputInfoHandler
import sys


MIN_SIZE_OF_LABIRINT = 4
MIN_VALUE_FOR_LETTER_CORD = 1


class GenerationAlgorithm(enum.IntEnum):
    DFS = 1
    PRIM = 2
    KRUSKAL = 3


class SolveAlgorithm(enum.IntEnum):
    BFS = 1
    ASTAR = 2


class DENSITY(enum.IntEnum):
    MIN_VALUE_DENSITY = 0
    MAX_VALUE_DENSITY = 1


class InputHandler:
    def __init__(self):
        """
        Initializes the InputHandler class.
        Creates an OutputInfoHandler object to handle user information output.
        """
        self.output_handler = OutputInfoHandler()

    def input_sizes(self) -> tuple:
        """
        Method to obtain the maze dimensions.
        The user inputs the maze's width and height (both values must be odd numbers greater than 3).

        Returns:
            tuple: the width and height of the maze.
        """
        return Reader.input_value(
            lambda: int(input("Введите ширину лабиринта (нечетное число > 3): ")),
            MIN_SIZE_OF_LABIRINT,
            None,
            "Ошибка: введите нечетное число больше 3.",
        ), Reader.input_value(
            lambda: int(input("Введите высоту лабиринта (нечетное число > 3): ")),
            MIN_SIZE_OF_LABIRINT,
            None,
            "Ошибка: введите нечетное число больше 3.",
        )

    def input_cords_of_letters(self, width, height) -> tuple:
        """
        Method to obtain the coordinates of two points (letters 'A' and 'B') in the maze.

        Args:
            width (int): the maze's width.
            height (int): the maze's height.

        Returns:
            tuple: the (x, y) coordinates for letters 'A' and 'B'.
        """
        self.output_handler.print_start_cords()
        letter_a_x = Reader.input_value(
            lambda: int(input("x: ")),
            MIN_VALUE_FOR_LETTER_CORD,
            width - 2,
            f"Ошибка: координаты должны быть в диапазоне от 1 до {width - 2}.",
        )
        letter_a_y = Reader.input_value(
            lambda: int(input("y: ")),
            MIN_VALUE_FOR_LETTER_CORD,
            height - 2,
            f"Ошибка: координаты должны быть в диапазоне от 1 до {height - 2}.",
        )
        clear_input_line()
        self.output_handler.print_end_cords()
        letter_b_x = Reader.input_value(
            lambda: int(input("x: ")),
            MIN_VALUE_FOR_LETTER_CORD,
            width - 2,
            f"Ошибка: координаты должны быть в диапазоне от 1 до {width - 2}.",
        )
        letter_b_y = Reader.input_value(
            lambda: int(input("y: ")),
            MIN_VALUE_FOR_LETTER_CORD,
            height - 2,
            f"Ошибка: координаты должны быть в диапазоне от 1 до {height - 2}.",
        )

        return letter_a_x, letter_a_y, letter_b_x, letter_b_y

    def input_density(self) -> float:
        """
        Method to obtain the maze density coefficient (a number greater than 0 and less than 1).

        Returns:
            float: the maze density coefficient.
        """
        move_cursor(0, 1)
        sys.stdout.write(
            "Выберите коэффициент заполненности лабиринта (число больше 0 и меньше 1):\n"
        )
        move_cursor(0, 2)
        return Reader.input_value(
            lambda: float(input("density: ")), DENSITY.MIN_VALUE_DENSITY, DENSITY.MAX_VALUE_DENSITY, "Ошибка: введите число от 0 до 1."
        )

    def input_type_of_maze(self) -> DiffTypesOfSurfaces:
        """
        Method to obtain the maze type.
        The user chooses whether to add different types of surfaces to the maze.

        Returns:
            str: 'Да' or 'Нет'.
        """
        return Reader.input_value(
            lambda: input(
                "Хотите ли вы добавить различные типы поверхностей в лабиринт? (Да/Нет) "
            ),
            error_message="Ошибка: введите Да или Нет.",
        )

    def input_generation_algo(self) -> int:
        """
        Method to select the maze generation algorithm.

        Returns:
            int: the number of the selected algorithm (from 1 to 3).
        """
        return Reader.input_value(
            lambda: self.output_handler.print_input(),
            GenerationAlgorithm.DFS,
            GenerationAlgorithm.PRIM,
            "Ошибка: введите число от 1 до 3.",
        )

    def input_solve_algo(self, diff_types_of_surfaces) -> int:
        """
        Method to select the maze solving algorithm.
        If the user did not choose to add surface types, algorithms without considering surface types are offered.

        Args:
            user_choice_of_type_of_maze (DiffTypesOfSurfaces): the user's choice about adding surface types.

        Returns:
            int: the number of the selected algorithm or confirmation of choice ('Да').
        """
        if diff_types_of_surfaces == DiffTypesOfSurfaces.NO:
            return Reader.input_value(
                lambda: self.output_handler.print_output(),
                SolveAlgorithm.BFS,
                SolveAlgorithm.ASTAR,
                "Ошибка: введите число от 1 до 2.",
            )
        else:
            return Reader.input_value(
                lambda: self.output_handler.print_output_weight(),
                error_message="Ошибка: введите Да.",
            )
