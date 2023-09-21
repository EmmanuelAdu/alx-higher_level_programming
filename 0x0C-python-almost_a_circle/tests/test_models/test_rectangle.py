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

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-23, 8)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 4)

class TestRectangle_height(unittest.TestCase):
    """Unittests for testing height of Rectangle"""

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, None)
         
    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "invalid")

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.5)

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, complex(5))

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {"a": 1, "b": 2})

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, [1, 2, 3])

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, {1, 2, 3})

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, (1, 2, 3))

    def test_frozenset_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, frozenset({1, 2, 3, 1}))

    def test_range_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, range(5))

    def test_bytes_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, b'Python')

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(23, -8)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)

class TestRectangle_x(unittest.TestCase):
    """Unittests for testing x-coordinate of Rectangle"""
     
    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, None, 5)
         
    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, "invalid", 8)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 3, 5.5, 10)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, complex(5), 8)

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 5, {"a": 1, "b": 2}, 5)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 3, [1, 2, 3], 9)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 7, {1, 2, 3}, 2)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 5, (1, 2, 3), 7)

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(6, 8, frozenset({1, 2, 3, 1}), 3)

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 5, range(5), 7)

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 7, b'Python', 12)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(9, 23, -8, 7)

class TestRectangle_y(unittest.TestCase):
    """Unittests for testing errors in y-coordinate"""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 2, 5, None)
         
    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 8, "invalid")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 3, 10, 5.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 8, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 5, 6, {"a": 1, "b": 2})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 3, 9, [1, 2, 3])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 7, 7, {1, 2, 3})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 5, 1, (1, 2, 3))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(6, 8, 12, frozenset({1, 2, 3, 1}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 5, 5, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 7, 3, b'Python')

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(9, 23, 7, -8)

class TestRectangle_order_of_initialization(unittest.TestCase):
    """Unittest for checking errors in order of initialization"""
     
    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, "invalid x")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, 3, "invalid y")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", "invalid x")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", 2, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid x", "invalid y")

class TestRectangle_area(unittest.TestCase):
    """Unittests for testing the area method of the Rectangle class."""

    def test_area_small(self):
        r = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, r.area())

    def test_large_area(self):
        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())

    def test_area_changed_attributes(self):
        r = Rectangle(2, 10, 1, 1, 1)
        r.width = 7
        r.height = 14
        self.assertEqual(98, r.area())

    def test_Error_area_one_arg(self):
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)

class TestRectangle_with_stdout(unittest.TestCase):
    """Unittests for capturing and comparing text printed to stdout"""

    @staticmethod
    def capture_to_stdout(rect, method):
        """Captures and compares text printed to stdout

        Args:
             rect(Rectangle) - an instance of a rectangle
             method(method) - a method that is either 'print' or 'display'
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture
    
    def test_str_mthd_print_width_height(self):
        R = Rectangle(4, 6)
        capture = TestRectangle_with_stdout.capture_to_stdout(R, "print")
        compare = "[Rectangle] ({}) 0/0 - 4/6\n".format(R.id)
        self.assertEqual(compare, capture.getvalue())

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
