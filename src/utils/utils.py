import os  # Importing os module to interact with the operating system
import sys  # Importing sys module to interact with standard input and output


# Function to clear the terminal screen based on the operating system
def clear_screen():
    # If the operating system is Windows ('nt'), use 'cls', otherwise use 'clear' for UNIX-based systems
    os.system("cls" if os.name == "nt" else "clear")


# Function to clear specific input lines in the terminal by overwriting them with spaces
def clear_input_line():
    # Move the cursor to the specified position and overwrite the line with spaces
    move_cursor(2, 3)
    sys.stdout.write("                                         ")
    # Move the cursor to the next line and overwrite it with spaces
    move_cursor(3, 4)
    sys.stdout.write("                                         ")


# Function to move the cursor to a specific position (x, y) in the terminal
def move_cursor(x, y):
    # Use ANSI escape sequences to position the cursor at the specified coordinates (y, x)
    sys.stdout.write(f"\033[{y};{x}H")
