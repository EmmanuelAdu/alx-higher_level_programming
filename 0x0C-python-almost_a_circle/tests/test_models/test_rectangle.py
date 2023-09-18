#!/usr/bin/python3
"""Defines unittests for rectangle.py

Unittest classes:
    TestRectangle_instantiation
"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Represents Unittest for Rectangle instantiation"""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(5, 3), Base)

    def test_no_arg(self):
        self.assertRaises(TypeError, Rectangle)

    def test_one_argument(self):
        self.assertRaises(TypeError, Rectangle, 1)

    def test_two_args(self):
        r1 = Rectangle(4, 2)
        r2 = Rectangle(7, 5)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_argument(self):
        r1 = Rectangle(5, 2, 1)
        r2 = Rectangle(8, 3, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(7, 6, 5, 4)
        r2 = Rectangle(4, 5, 6, 7)
        self.assertEqual(r1.id, r2.id - 1)

    def test_check_id_five_args(self):
        r1 = Rectangle(8, 5, 3, 2, 7)
        self.assertEqual(7, r1.id)

    def test_more_than_five(self):
        with self.assertRaises(TypeError):
            Rectangle(6, 5, 4, 3, 2, 1, 0)

    def test_private_width(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(6, 4, 3, 0, 1).__width)

    def test_private_height(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(6, 4, 3, 0, 1).__height)

    def test_private_x(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(6, 4, 3, 0, 1).__x)

    def test_private_y(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(6, 4, 3, 0, 1).__y)
