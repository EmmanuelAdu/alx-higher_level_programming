#!/usr/bin/python3

"""Define unittest for class Square

Unittest classes:
    TestSquare
    TestSquare_size
    TestSquare_y
    TestSquare_x
    TestSquare_order_of_initialization
    TestSquare_area
    TestSquare_update_args
    TestSquare_update_kwargs
    TestSquare_stdout
    TestSquare_to_dictionary
"""
import unittest
import os
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json

class TestSquare(unittest.TestCase):
    """Unittest for the Class Square"""
    
    def test_is_base(self):
        self.assertIsInstance(Square(5), Base)
    
    def test_is_rectangle(self):
        self.assertIsInstance(Square(5), Rectangle)

    def test_no_argument(self):
        with self.assertRaises(TypeError):
            s = Square()
    
    def test_one_arg(self):
        s = Square(3)
        s1 = Square(5)
        self.assertEqual(s.id, s1.id - 1)
    
    def test_two_args(self):
        s1 = Square(4, 5)
        s2 = Square(5, 7)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(3, 4, 5)
        s2 = Square(6, 7, 8)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        self.assertEqual(6, Square(3, 5, 4, 6).id)

    #ERROR
    def test_above_four_args(self):
        with self.assertRaises(TypeError):
            Square(5, 4, 6, 8, 2)
    #ERROR
    def test_private_size(self):
        with self.assertRaises(AttributeError):
            print(Square(2, 3, 4, 5).__size)

    def test_size_getter(self):
        self.assertEqual(5, Square(5, 4, 3, 2).size)

    def test_size_setter(self):
        s1 = Square(5, 4, 3, 2)
        s1.size = 8
        self.assertEqual(8, s1.size)

    def test_width_setter(self):
        s = Square(5, 4, 3, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_height_setter(self):
        s = Square(5, 4, 3, 2)
        s.size = 9
        self.assertEqual(9, s.height)

    def test_x_setter(self):
        s = Square(5, 4, 3, 2)
        s.x = 7
        self.assertEqual(7, s.x)

    def test_x_getter(self):
        self.assertEqual(0, Square(5).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(6).y)

#Testing For Errors
class TestSquare_size(unittest.TestCase):
    """Unittest for testing the size"""

    def test_size_None(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)
    
    def test_size_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("string")

    def test_size_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(20.68)
    
    def test_size_complex(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(67))

    def test_size_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({'Jason': 23, 'Eric': 4})

    def test_size_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 4, 5, 2)

    def test_size_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(["Joseph", 5], 7, 8, 9)

    def test_size_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({3, 4}, 6, 7)

    def test_size_frozen_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({'Kennedy', 'Akos'}), 3, 4, 6)

    def test_size_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((8, 4), 5, 7)

    def test_range_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(5))

    def test_nan_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    def test_size_mem_view(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'abcd'))

    def test_size_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_size_bytearray(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'abcde'))

    def test_size_bytes(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'BEEW')

    #ErrorChecking For Negative Numbers
    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-4, 5, 6)
    
    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 5, 8)

class TestSquare_x(unittest.TestCase):
    """Unittest for x -coordinates of a square"""
    def test_x_None(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, None)
    
    def test_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, "string")

    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, 20.68, 6)
    
    def test_x_complex(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, complex(67))

    def test_x_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, {'Jason': 23, 'Eric': 4})

    def test_x_bool(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, True, 5, 2)

    def test_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(6, ["Joseph", 5], 8, 9)

    def test_x_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, {3, 4}, 6, 7)

    def test_x_frozen_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, frozenset({'Kennedy', 'Akos'}), 4, 6)

    def test_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(9, (8, 4), 5, 7)

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, range(5))

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, float('nan'))

    def test_x_mem_view(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(6, memoryview(b'abcd'))

    def test_x_inf(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(6, float('inf'))

    def test_x_bytearray(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(7, bytearray(b'abcde'))

    def test_x_bytes(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(7, b'BEEW')

    #ErrorChecking For Negative Numbers
    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(4, -5, 6)

class TestSquare_y(unittest.TestCase):
    """Unittest for y -coordinates of a square"""
    def test_y_None(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, None)
    
    def test_y_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 3, "string")

    def test_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 5, 20.68, 6)
    
    def test_y_complex(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 3, complex(67))

    def test_y_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 5, {'Jason': 23, 'Eric': 4})

    def test_y_bool(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 5, True, 5)

    def test_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(9, 6, ["Joseph", 5], 8)

    def test_y_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 5, {3, 4}, 7)

    def test_y_frozen_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 3, frozenset({'Kennedy', 'Akos'}), 4)

    def test_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(6, 9, (8, 4), 5)

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 4, range(5))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 4, float('nan'))

    def test_y_mem_view(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(8, 6, memoryview(b'abcd'))

    def test_y_inf(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 6, float('inf'))

    def test_y_bytearray(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 7, bytearray(b'abcde'))

    def test_y_bytes(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 7, b'BEEW')

    #ErrorChecking For Negative Numbers
    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(7, 4, -5, 6)
     

if __name__ == "__main__":
    unittest.main()
