from src.entities.maze import PossibleChoiceOfTypeOfMaze
from src.services.input.reader import Reader
from src.utils.utils import *
from src.services.input.output_info import OutputInfoHandler
import sys


class InputHandler:
    def __init__(self):
        """
        Инициализация класса InputHandler.
        Создается объект класса OutputInfoHandler для обработки вывода информации пользователю.
        """
        self.output_handler = OutputInfoHandler()

    def input_sizes(self):
        """
        Метод для получения размеров лабиринта.
        Пользователь вводит ширину и высоту лабиринта (оба значения должны быть нечетными числами больше 3).

        Возвращает:
            tuple: ширина и высота лабиринта.
        """
        return Reader.input_value(
            lambda: int(input("Введите ширину лабиринта (нечетное число > 3): ")),
            4,
            None,
            "Ошибка: введите нечетное число больше 3.",
        ), Reader.input_value(
            lambda: int(input("Введите высоту лабиринта (нечетное число > 3): ")),
            4,
            None,
            "Ошибка: введите нечетное число больше 3.",
        )

    def input_cords_of_letters(self, width, height):
        """
        Метод для получения координат двух точек (буквы 'A' и 'B') в лабиринте.

        Аргументы:
            width (int): ширина лабиринта.
            height (int): высота лабиринта.

        Возвращает:
            tuple: координаты (x, y) для буквы 'A' и 'B'.
        """
        self.output_handler.print_start_cords()
        letter_a_x = Reader.input_value(
            lambda: int(input("x: ")),
            1,
            width - 2,
            f"Ошибка: координаты должны быть в диапазоне от 1 до {width - 2}.",
        )
        letter_a_y = Reader.input_value(
            lambda: int(input("y: ")),
            1,
            height - 2,
            f"Ошибка: координаты должны быть в диапазоне от 1 до {height - 2}.",
        )
        clear_input_line()
        self.output_handler.print_end_cords()
        letter_b_x = Reader.input_value(
            lambda: int(input("x: ")),
            1,
            width - 2,
            f"Ошибка: координаты должны быть в диапазоне от 1 до {width - 2}.",
        )
        letter_b_y = Reader.input_value(
            lambda: int(input("y: ")),
            1,
            height - 2,
            f"Ошибка: координаты должны быть в диапазоне от 1 до {height - 2}.",
        )

        return letter_a_x, letter_a_y, letter_b_x, letter_b_y

    def input_density(self):
        """
        Метод для получения коэффициента заполненности лабиринта (число больше 0 и меньше 1).

        Возвращает:
            float: коэффициент заполненности лабиринта.
        """
        move_cursor(0, 1)
        sys.stdout.write(
            "Выберите коэффициент заполненности лабиринта (число больше 0 и меньше 1):\n"
        )
        move_cursor(0, 2)
        return Reader.input_value(
            lambda: float(input("density: ")), 0, 1, "Ошибка: введите число от 0 до 1."
        )

    def input_type_of_maze(self):
        """
        Метод для получения типа лабиринта.
        Пользователь выбирает, хочет ли он добавить различные типы поверхностей в лабиринт.

        Возвращает:
            str: Да или Нет.
        """
        return Reader.input_value(
            lambda: input(
                "Хотите ли вы добавить различные типы поверхностей в лабиринт? (Да/Нет) "
            ),
            error_message="Ошибка: введите Да или Нет.",
        )

    def input_generation_algo(self):
        """
        Метод для выбора алгоритма генерации лабиринта.

        Возвращает:
            int: номер выбранного алгоритма (от 1 до 3).
        """
        return Reader.input_value(
            lambda: self.output_handler.print_input(),
            1,
            3,
            "Ошибка: введите число от 1 до 3.",
        )

    def input_solve_algo(self, user_choice_of_type_of_maze):
        """
        Метод для выбора алгоритма решения лабиринта.
        Если пользователь не выбрал тип поверхности, предлагаются алгоритмы без учета типов поверхностей.

        Аргументы:
            user_choice_of_type_of_maze (str): выбор пользователя о добавлении типов поверхностей.

        Возвращает:
            int: номер выбранного алгоритма или подтверждение выбора (Да).
        """
        if user_choice_of_type_of_maze == PossibleChoiceOfTypeOfMaze.NO.value:
            return Reader.input_value(
                lambda: self.output_handler.print_output(),
                1,
                2,
                "Ошибка: введите число от 1 до 2.",
            )
        else:
            return Reader.input_value(
                lambda: self.output_handler.print_output_weight(),
                error_message="Ошибка: введите Да.",
            )
