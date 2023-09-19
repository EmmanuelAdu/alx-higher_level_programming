#!/usr/bin/python3

import unittest
import os
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import sys
import json

class TestSquare(unittest.TestCase):
    """Test class for Square class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_10_0(self):
        """Test Square class: check for attributes."""

        s0 = Square(1)
        self.assertEqual(s0.id, 1)
        s1 = Square(5, 3, 4)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.id, 2)

    def test_10_1(self):
        """Test __str__ representation."""

        s1 = Square(9, 4, 5, 6)
        self.assertEqual(str(s1), "[Square] (6) 4/5 - 9")

    def test_10_2(self):
        """Test Square class: check for inheritance."""

        s1 = Square(6)
        self.assertTrue(isinstance(s1, Rectangle))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertFalse(isinstance(Square, Rectangle))
        self.assertTrue(isinstance(s1, Base))
        self.assertTrue(issubclass(Square, Base))
        self.assertFalse(isinstance(Square, Base))

    # def test_10_3(self):
    #     """Test Square class: check for missing args."""

    #     with self.assertRaises(TypeError) as x:
    #         s1 = Square()
    #     self.assertEqual(
    #         "__init__() missing 1 required positional argument: 'size'", str(
    #             x.exception))

    def test_10_4(self):
        """Test Square for methods inherited from Rectangle."""

        s1 = Square(9)
        self.assertEqual(s1.area(), 81)
        s2 = Square(4, 1, 2, 5)

if __name__ == "__main__":
    unittest.main()
