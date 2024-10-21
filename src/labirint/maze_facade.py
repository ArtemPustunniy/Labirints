from src.services.generators.generator_factory import GeneratorFactory
from src.services.input.input import *
from src.services.renders.default_render import DefaultRender
from src.services.renders.render_path import RenderPath
from src.services.solvers.solver_factory import SolverFactory


class MazeCascade:
    """
    A class to handle the process of creating, rendering, and solving a maze through various steps.

    Attributes:
        input_handler (InputHandler): An instance of InputHandler to handle user input.
    """

    def __init__(self):
        """
        Initializes the MazeCascade class and sets up the input handler.
        """
        self.input_handler = InputHandler()

    def initialize_labirint(self):
        """
        Manages the entire flow for creating, rendering, and solving a maze.
        The method takes user input for maze configuration, generates the maze, and then solves it.
        """
        # Get maze dimensions from user input
        width, height = self.input_handler.input_sizes()
        clear_screen()

        # Get start and end coordinates from user input
        cords = self.input_handler.input_cords_of_letters(width, height)
        clear_screen()

        # Get maze density from user input
        density = self.input_handler.input_density()
        clear_screen()

        # Get the type of maze (with or without different terrain types)
        user_choice_of_type_of_maze = self.input_handler.input_type_of_maze()
        clear_screen()

        # Get the maze generation algorithm from user input
        generation_algo = self.input_handler.input_generation_algo()
        clear_screen()

        # Generate the maze using the selected algorithm
        generator = GeneratorFactory.get_generator(generator_type=generation_algo)
        maze = generator.generate(
            width, height, cords, density, user_choice_of_type_of_maze
        )

        # Render the generated maze
        default_render = DefaultRender()
        default_render.render(
            maze=maze, user_choice_of_type_of_maze=user_choice_of_type_of_maze
        )

        # Get the maze solving algorithm from user input
        solve_algo = self.input_handler.input_solve_algo(
            user_choice_of_type_of_maze=user_choice_of_type_of_maze
        )

        # Solve the maze using the selected algorithm
        solver = SolverFactory.get_solver(solve_algo)
        path = solver.solve(maze)

        # Render the path on the maze
        path_render = RenderPath()
        path_render.render(
            maze=maze,
            user_choice_of_type_of_maze=user_choice_of_type_of_maze,
            path=path,
        )
