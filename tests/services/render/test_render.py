import unittest
from src.services.renders.render import (
    Render,
)  # Assuming Render is saved in src.services.renders.render


class TestRenderAbstract(unittest.TestCase):

    def test_subclass_implementation(self):
        class TestConcreteRender(Render):
            def render(self, maze, user_choice_of_type_of_maze, path: [] = None):
                return True

        renderer = TestConcreteRender()
        result = renderer.render(None, None)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
