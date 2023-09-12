#!/usr/bin/python3
"""Defines an inherited class checking function"""


def inherits_from(obj, a_class):
    """Returns True if object is an inherited-class instance

    Args:
         obj - object to compare
         a_class - class to check
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
