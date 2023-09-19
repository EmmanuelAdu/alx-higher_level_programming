#!/usr/bin/python3
"""Defines unittests for rectangle.py

Unittest classes:
    TestRectangle_instantiation
"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
import io
import sys


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

    def test_width_getter(self):
        R = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, R.width)

    def test_width_setter(self):
        R = Rectangle(5, 7, 7, 5, 1)
        R.width = 10
        self.assertEqual(10, R.width)

    def test_height_getter(self):
        R = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, R.height)

    def test_height_setter(self):
        R = Rectangle(5, 7, 7, 5, 1)
        R.height = 10
        self.assertEqual(5, R.height)

    def test_x_getter(self):
        R = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, R.x)

    def test_x_setter(self):
        R = Rectangle(5, 7, 7, 5, 1)
        R.x = 10
        self.assertEqual(10, R.x)

    def test_y_getter(self):
        R = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, R.y)

    def test_y_setter(self):
        R = Rectangle(5, 7, 7, 5, 1)
        R.y = 10
        self.assertEqual(10, R.y)

class TestRectangle_width(unittest.TestCase):
    """Testing initialization of Rectangle width attribute"""
    
    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 2)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 2)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)

    def test_frozenset_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3, 1}), 2)

    def test_range_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(5), 2)

    def test_bytes_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Python', 2)

class TestRectangle_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Rectangle class."""

    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()
