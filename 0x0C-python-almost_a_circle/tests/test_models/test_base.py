#!/usr/bin/python3
"""Defines a testing or unittests for base.py

Unittest Classes:
    TestBase_instantiation
"""

import unittest
import os
from models.base import Base

class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing the Base class instantiation
    """

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id -1)

    def test_no_arg_3(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_id_None(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_with_id(self):
        self.assertEqual(13, Base(13).id)

    def test_with_id_and_no_arg(self):
        b1 = Base()
        b2 = Base(15)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_public_id(self):
        b1 = Base(14)
        b1.id = 12
        self.assertEqual(12, b1.id)

    def test_raise_error(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_objects)
