#!/usr/bin/python3
"""Define function that returns list of available attributes"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object

    Args:
         obj - the object
    """
    return (dir(obj))
