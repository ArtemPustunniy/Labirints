from src.services.generators.dfs_generator import DfsGenerator
from src.services.generators.generator import AvailableGenerators, Generator
from src.services.generators.kruskal_generator import KruskalGenerator
from src.services.generators.prim_generator import PrimGenerator


class GeneratorFactory:
    """
    A factory class to create instances of maze generators based on the provided generator type.
    This class provides a static method to return an appropriate generator instance.
    """

    @staticmethod
    def get_generator(generator_type: int) -> Generator:
        """
        Returns an instance of the generator based on the given generator type.

        Args:
            generator_type (int): An integer representing the type of maze generator.

        Returns:
            Generator: An instance of a maze generator (e.g., DfsGenerator, PrimGenerator, KruskalGenerator).

        Raises:
            ValueError: If an unknown generator type is provided.
        """
        if generator_type == AvailableGenerators.DfsGenerator.value:
            return DfsGenerator()
        elif generator_type == AvailableGenerators.PrimGenerator.value:
            return PrimGenerator()
        elif generator_type == AvailableGenerators.KruskalGenerator.value:
            return KruskalGenerator()
        else:
            raise ValueError(f"Unknown generator type: {generator_type}")

    def __init__(self):
        """
        Prevents instantiation of the GeneratorFactory class.
        """
        raise NotImplementedError("This class cannot be instantiated")
