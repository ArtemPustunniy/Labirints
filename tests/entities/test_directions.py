import unittest

from src.entities.directions import Directions


class TestDirections(unittest.TestCase):
    def test_directions_values(self):
        self.assertEqual(Directions.NORTH.value, (0, -1))
        self.assertEqual(Directions.SOUTH.value, (0, 1))
        self.assertEqual(Directions.EAST.value, (1, 0))
        self.assertEqual(Directions.WEST.value, (-1, 0))

    def test_dx_property(self):
        self.assertEqual(Directions.NORTH.dx, 0)
        self.assertEqual(Directions.SOUTH.dx, 0)
        self.assertEqual(Directions.EAST.dx, 1)
        self.assertEqual(Directions.WEST.dx, -1)

    def test_dy_property(self):
        self.assertEqual(Directions.NORTH.dy, -1)
        self.assertEqual(Directions.SOUTH.dy, 1)
        self.assertEqual(Directions.EAST.dy, 0)
        self.assertEqual(Directions.WEST.dy, 0)

    def test_direction_names(self):
        self.assertEqual(Directions.NORTH.name, "NORTH")
        self.assertEqual(Directions.SOUTH.name, "SOUTH")
        self.assertEqual(Directions.EAST.name, "EAST")
        self.assertEqual(Directions.WEST.name, "WEST")


if __name__ == "__main__":
    unittest.main()
