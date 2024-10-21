import sys  # Импорт модуля для взаимодействия с системным вводом/выводом

from src.utils.utils import (
    clear_screen,
    move_cursor,
)  # Импорт функций для очистки экрана и перемещения курсора

# Класс для обработки пользовательского ввода с проверкой значений


class Reader:
    @staticmethod
    # Метод для получения значения от пользователя с проверкой на минимальное и максимальное значение
    def input_value(
        info_method,
        min_value=None,
        max_value=None,
        error_message="Ошибка: введите допустимое значение",
    ):
        # Бесконечный цикл, продолжающийся до тех пор, пока не будет получено корректное значение
        while True:
            try:
                # Получение значения с помощью переданного метода (например, вызова функции input)
                value = info_method()
                # Проверка, что значение находится в заданном диапазоне, если он задан
                if (min_value is None or value >= min_value) and (
                    max_value is None or value <= max_value
                ):
                    return value  # Возврат корректного значения
                else:
                    # Очистка экрана и вывод сообщения об ошибке, если значение выходит за пределы допустимого диапазона
                    clear_screen()
                    move_cursor(0, 1)
                    sys.stdout.write(error_message + "\n")
            except ValueError:
                # Обработка исключений, если введенное значение не может быть преобразовано (например, при вводе нечислового значения)
                clear_screen()  # Очистка экрана
                move_cursor(0, 1)
                sys.stdout.write(error_message + "\n")  # Вывод сообщения об ошибке
