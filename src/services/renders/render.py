from abc import (
    ABC,
    abstractmethod,
)  # Importing Abstract Base Class (ABC) and abstractmethod for defining an abstract base class
from typing import List  # Importing List for type hinting when needed


# Abstract base class for rendering the maze
class Render(ABC):
    # Abstract method that must be implemented by subclasses to render the maze
    # Takes the maze, user's choice of maze type, and an optional path as parameters
    @abstractmethod
    def render(self, maze, user_choice_of_type_of_maze, path: [] = None):
        pass  # This method will be defined in concrete subclasses
