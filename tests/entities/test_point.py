import unittest
import sys

from src.entities.point import Point


# Assuming the Point class is saved in point_module.py


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.point1 = Point(1, 1, 2, "@")
        self.point2 = Point(2, 2, 3, "~")
        self.point3 = Point(3, 3, 1, " ")

    def test_initialization(self):
        self.assertEqual(self.point1.x, 1)
        self.assertEqual(self.point1.y, 1)
        self.assertEqual(self.point1.weight, 2)
        self.assertEqual(self.point1.symbol, "@")

    def test_lt_comparison(self):
        self.assertTrue(self.point3 < self.point1)
        self.assertFalse(self.point2 < self.point1)

    def test_repr(self):
        self.assertEqual(repr(self.point1), "Point(weight=2, symbol=@)")
        self.assertEqual(repr(self.point3), "Point(weight=1, symbol= )")

    def test_gran_elem(self):
        gran_elem = Point(0, 0, sys.maxsize, "█")
        self.assertEqual(gran_elem.weight, sys.maxsize)
        self.assertEqual(gran_elem.symbol, "█")

    def test_common_elem(self):
        common_elem = Point(0, 0, 1, " ")
        self.assertEqual(common_elem.weight, 1)
        self.assertEqual(common_elem.symbol, " ")


if __name__ == "__main__":
    unittest.main()
