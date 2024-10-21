import unittest
from abc import ABC, abstractmethod
from src.services.renders.render import (
    Render,
)  # Assuming Render is saved in src.services.renders.render


class TestRenderAbstract(unittest.TestCase):
    def test_abstract_render_method(self):
        with self.assertRaises(TypeError):
            render = (
                Render()
            )  # Attempting to instantiate an abstract class should raise a TypeError

    def test_subclass_implementation(self):
        class TestConcreteRender(Render):
            def render(self, maze, user_choice_of_type_of_maze, path: [] = None):
                return True

        renderer = TestConcreteRender()
        result = renderer.render(None, None)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
