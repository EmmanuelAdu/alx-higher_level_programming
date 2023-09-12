#!/usr/bin/python3
"""Defines a class and an inherited class checking function"""


def is_kind_of_class(obj, a_class):
    """Returns True if an object is an instance or inherited instance

    Args:
         obj - object to check
         a_class - class to compare the object to
    """
    if isinstance(obj, a_class):
        return (True)
    return (False)
