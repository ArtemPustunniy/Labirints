from src.services.generators.generator_factory import GeneratorFactory
from src.services.input.input import InputHandler
from src.services.renders.default_render import DefaultRender
from src.services.renders.render_path import RenderPath
from src.services.solvers.solver_factory import SolverFactory
from src.utils.utils import clear_screen


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

    def initialize_labirint(self) -> None:
        """
        Manages the entire flow for creating, rendering, and solving a maze.
        The method takes user input for maze configuration, generates the maze, and then solves it.
        """
        width, height = self.input_handler.input_sizes()
        clear_screen()

        cords = self.input_handler.input_cords_of_letters(width, height)
        clear_screen()

        density = self.input_handler.input_density()
        clear_screen()

        diff_types_of_surfaces = self.input_handler.input_type_of_maze()
        clear_screen()

        generation_algo = self.input_handler.input_generation_algo()
        clear_screen()

        generator = GeneratorFactory.get_generator(generator_type=generation_algo)
        maze = generator.generate(
            width, height, cords, density, diff_types_of_surfaces
        )

        default_render = DefaultRender()
        default_render.render(
            maze=maze, diff_types_of_surfaces=diff_types_of_surfaces
        )

        solve_algo = self.input_handler.input_solve_algo(
            diff_types_of_surfaces=diff_types_of_surfaces
        )

        solver = SolverFactory.get_solver(solve_algo)
        path = solver.solve(maze)

        path_render = RenderPath()
        path_render.render(
            maze=maze,
            diff_types_of_surfaces=diff_types_of_surfaces,
            path=path,
        )
