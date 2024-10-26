import os
import sys


def clear_screen():
    """
    Clears the terminal screen based on the operating system.
    """
    os.system("cls" if os.name == "nt" else "clear")


def clear_input_line():
    """
    Clears specific input lines in the terminal by overwriting them with spaces.
    """
    move_cursor(2, 3)
    sys.stdout.write("                                         ")
    move_cursor(3, 4)
    sys.stdout.write("                                         ")


def move_cursor(x, y):
    """
    Moves the cursor to a specific position (x, y) in the terminal.
    """
    sys.stdout.write(f"\033[{y};{x}H")
