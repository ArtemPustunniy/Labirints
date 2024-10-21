import sys

from src.utils.utils import move_cursor


# Класс для вывода информации пользователю о выборе алгоритмов и координат
class OutputInfoHandler:
    # Метод для вывода интерфейса выбора алгоритма генерации лабиринта
    def print_input(self):
        move_cursor(0, 1)  # Перемещение курсора на одну строку вниз
        sys.stdout.write("Выберите алгоритм генерации лабиринта:")  # Вывод заголовка
        move_cursor(0, 2)
        sys.stdout.write("1. DFS (поиск в глубину)")  # Вывод первого варианта
        move_cursor(0, 3)
        sys.stdout.write("2. Прим")  # Вывод второго варианта
        move_cursor(0, 4)
        sys.stdout.write("3. Краскал")  # Вывод третьего варианта
        move_cursor(0, 5)
        # Получение выбора пользователя
        choice = int(input("Ваш выбор (1/2/3): "))
        return choice

    # Метод для вывода ошибки при неверном вводе при выборе алгоритма генерации
    def print_input_error(self):
        move_cursor(0, 1)
        sys.stdout.write("Пожалуйста введите валидное число")  # Сообщение об ошибке
        move_cursor(0, 2)
        sys.stdout.write("1. DFS (поиск в глубину)")
        move_cursor(0, 3)
        sys.stdout.write("2. Прим")
        move_cursor(0, 4)
        sys.stdout.write("3. Краскал")
        move_cursor(0, 5)
        # Повторный ввод выбора
        choice = int(input("Ваш выбор (1/2/3): "))
        return choice

    # Метод для вывода интерфейса выбора алгоритма решения лабиринта
    def print_output(self):
        move_cursor(0, 1)
        sys.stdout.write(
            "1. BFS (поиск в ширину)"
        )  # Вывод первого варианта алгоритма решения
        move_cursor(0, 2)
        sys.stdout.write(
            "2. A* (поиск A-star)"
        )  # Вывод второго варианта алгоритма решения
        move_cursor(0, 3)
        # Получение выбора пользователя
        choice = int(input("Ваш выбор (1/2): "))
        return choice

    # Метод для вывода интерфейса выбора алгоритма решения с использованием взвешенного пути
    def print_output_weight(self):
        move_cursor(0, 1)
        sys.stdout.write(
            "Djkstra (алгоритм Дейкстры)"
        )  # Вывод информации об алгоритме Дейкстры
        move_cursor(0, 2)
        # Получение ввода пользователя для подтверждения
        choice = input("Введите Да, чтобы посмотреть оптимальный путь в лабиринте ")
        return choice

    # Метод для вывода ошибки при неправильном вводе при выборе алгоритма Дейкстры
    def print_output_weight_error(self):
        move_cursor(0, 1)
        sys.stdout.write("Введите именно Да")  # Сообщение об ошибке
        move_cursor(0, 2)
        sys.stdout.write(
            "Djkstra (алгоритм Дейкстры)"
        )  # Повторное сообщение об алгоритме
        move_cursor(0, 3)
        # Повторный ввод подтверждения
        choice = input("Введите Да, чтобы посмотреть оптимальный путь в лабиринте ")
        return choice

    # Метод для вывода ошибки при неверном вводе при выборе алгоритма решения лабиринта
    def print_output_error(self):
        move_cursor(0, 1)
        sys.stdout.write("Пожалуйста введите валидное число")  # Сообщение об ошибке
        move_cursor(0, 2)
        sys.stdout.write("1. BFS (поиск в ширину)")
        move_cursor(0, 3)
        sys.stdout.write("2. A* (поиск A-star)")
        move_cursor(0, 4)
        # Повторный ввод выбора
        choice = int(input("Ваш выбор (1/2): "))
        return choice

    # Метод для вывода инструкции по вводу начальных координат
    def print_start_cords(self):
        move_cursor(0, 1)
        sys.stdout.write(
            "Выберите расположение начальной и конечной точек"
        )  # Сообщение об установке начальной точки
        move_cursor(0, 2)
        sys.stdout.write(
            "Координаты начальной точки:"
        )  # Сообщение о вводе координат начальной точки
        move_cursor(0, 3)

    # Метод для вывода инструкции по вводу конечных координат
    def print_end_cords(self):
        move_cursor(0, 1)
        sys.stdout.write(
            "Выберите расположение начальной и конечной точек"
        )  # Сообщение об установке конечной точки
        move_cursor(0, 2)
        sys.stdout.write(
            "Координаты конечной точки:"
        )  # Сообщение о вводе координат конечной точки
        move_cursor(0, 3)
