import unittest
from src.services.generators.dfs_generator import DfsGenerator
from src.services.generators.kruskal_generator import KruskalGenerator
from src.services.generators.prim_generator import PrimGenerator
from src.services.generators.generator_factory import (
    GeneratorFactory,
)  # Assuming GeneratorFactory is saved in src.services.generators.generator_factory


class TestGeneratorFactory(unittest.TestCase):
    def test_get_generator_dfs(self):
        generator = GeneratorFactory.get_generator(1)
        self.assertIsInstance(generator, DfsGenerator)

    def test_get_generator_prim(self):
        generator = GeneratorFactory.get_generator(2)
        self.assertIsInstance(generator, PrimGenerator)

    def test_get_generator_kruskal(self):
        generator = GeneratorFactory.get_generator(3)
        self.assertIsInstance(generator, KruskalGenerator)

    def test_get_generator_invalid_type(self):
        with self.assertRaises(ValueError):
            GeneratorFactory.get_generator(4)

    def test_factory_class_instantiation(self):
        with self.assertRaises(NotImplementedError):
            GeneratorFactory()


if __name__ == "__main__":
    unittest.main()
