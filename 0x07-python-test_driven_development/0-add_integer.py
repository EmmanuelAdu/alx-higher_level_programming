#!/usr/bin/python3
"""Defining function that adds int

Paramaters:
-----------
a : int or float
    The first number.

b : int or float
    optional.
"""


def add_integer(a, b=98):
    """Return the result of the sum of a and b
    Float arg is typecast to int before the function is implemented

    Raises:
            TypeError: if either a or b is a not an int or float
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
