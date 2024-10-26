import sys

from src.utils.utils import move_cursor


class OutputInfoHandler:
    """Class for displaying information to the user about algorithm choices and coordinates."""

    def print_input_generation_algo(self):
        """
        Displays the maze generation algorithm selection menu to the user.

        Description:
            Shows the list of available generation algorithms:
            1. DFS (Depth-First Search)
            2. Prim's Algorithm
            3. Kruskal's Algorithm
            Then prompts the user to select an option, expecting input as a number (1, 2, or 3).

        Returns:
            int: The algorithm chosen by the user (1 for DFS, 2 for Prim, 3 for Kruskal).
        """
        sys.stdout.write("1. DFS (поиск в глубину)")
        move_cursor(0, 3)
        sys.stdout.write("2. Прим")
        move_cursor(0, 4)
        sys.stdout.write("3. Краскал")
        move_cursor(0, 5)
        choice = int(input("Ваш выбор (1/2/3): "))
        return choice

    def print_input_solve_algo(self):
        """
        Displays the maze-solving algorithm selection menu to the user.

        Description:
            Shows the list of available solving algorithms:
            1. BFS (Breadth-First Search)
            2. A* (A-star Search)
            Then prompts the user to select an option, expecting input as a number (1 or 2).

        Returns:
            int: The algorithm chosen by the user (1 for BFS, 2 for A*).
        """
        sys.stdout.write("1. BFS (поиск в ширину)")
        move_cursor(0, 3)
        sys.stdout.write("2. A* (поиск A-star)")
        move_cursor(0, 4)
        choice = int(input("Ваш выбор (1/2): "))
        return choice

    def print_input_weight_solve_algo(self):
        """
        Prompts the user to select an algorithm for finding the optimal path.

        Description:
            Displays Dijkstra's algorithm as available for finding the optimal path.
            Then asks the user for confirmation ("Да") to view the optimal path in the maze.

        Returns:
            str: The user's response (expects input "Да" for confirmation).
        """
        sys.stdout.write("Djkstra (алгоритм Дейкстры)")
        move_cursor(0, 3)
        choice = input("Введите Да, чтобы посмотреть оптимальный путь в лабиринте ")
        return choice

    def print_input(self) -> int:
        """
        Displays the interface for selecting a maze generation algorithm.

        Returns:
            int: The user's choice (1, 2, or 3).
        """
        move_cursor(0, 1)
        sys.stdout.write("Выберите алгоритм генерации лабиринта:")
        move_cursor(0, 2)
        choice = self.print_input_generation_algo()
        return choice

    def print_input_error(self) -> int:
        """
        Displays an error message when invalid input is entered during maze generation algorithm selection.

        Returns:
            int: The user's corrected choice (1, 2, or 3).
        """
        move_cursor(0, 1)
        sys.stdout.write("Пожалуйста введите валидное число")
        move_cursor(0, 2)
        choice = self.print_input_generation_algo()
        return choice

    def print_output(self) -> int:
        """
        Displays the interface for selecting a maze solving algorithm.

        Returns:
            int: The user's choice (1 or 2).
        """
        move_cursor(0, 1)
        sys.stdout.write("Выберите алгоритм решения лабиринта:")
        move_cursor(0, 2)
        choice = self.print_input_solve_algo()
        return choice

    def print_output_error(self) -> int:
        """
        Displays an error message when invalid input is entered during maze solving algorithm selection.

        Returns:
            int: The user's corrected choice (1 or 2).
        """
        move_cursor(0, 1)
        sys.stdout.write("Пожалуйста введите валидное число")
        move_cursor(0, 2)
        choice = self.print_input_solve_algo()
        return choice

    def print_output_weight(self) -> str:
        """
        Displays the interface for selecting the solving algorithm using a weighted path (Dijkstra's algorithm).

        Returns:
            str: The user's confirmation input (e.g., 'Да').
        """
        move_cursor(0, 1)
        sys.stdout.write("Выберите алгоритм решения лабиринта:")
        move_cursor(0, 2)
        choice = self.print_input_weight_solve_algo()
        return choice

    def print_output_weight_error(self) -> str:
        """
        Displays an error message when invalid input is entered during Dijkstra's algorithm selection.

        Returns:
            str: The user's corrected confirmation input (e.g., 'Да').
        """
        move_cursor(0, 1)
        sys.stdout.write("Введите именно Да")
        move_cursor(0, 2)
        choice = self.print_input_weight_solve_algo()
        return choice

    def print_start_cords(self) -> None:
        """
        Displays instructions for entering the starting coordinates.
        """
        move_cursor(0, 1)
        sys.stdout.write("Выберите расположение начальной и конечной точек")
        move_cursor(0, 2)
        sys.stdout.write("Координаты начальной точки:")
        move_cursor(0, 3)

    def print_end_cords(self) -> None:
        """
        Displays instructions for entering the ending coordinates.
        """
        move_cursor(0, 1)
        sys.stdout.write("Выберите расположение начальной и конечной точек")
        move_cursor(0, 2)
        sys.stdout.write("Координаты конечной точки:")
        move_cursor(0, 3)
