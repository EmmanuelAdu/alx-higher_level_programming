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

if __name__ == "__main__":
    unittest.main()
