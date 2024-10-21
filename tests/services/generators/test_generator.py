import unittest
from src.services.generators.generator import (
    Generator,
)  # Assuming Generator is saved in src.services.generators.generator


class TestGenerator(unittest.TestCase):
    def test_abstract_generate_method(self):
        with self.assertRaises(TypeError):
            generator = (
                Generator()
            )  # Attempting to instantiate an abstract class should raise a TypeError

    def test_subclass_implementation(self):
        class TestConcreteGenerator(Generator):
            def generate(
                self, width, height, cords, density, user_choice_of_type_of_maze
            ):
                return True

        generator = TestConcreteGenerator()
        result = generator.generate(5, 5, (1, 1, 3, 3), 0.5, "Нет")
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
