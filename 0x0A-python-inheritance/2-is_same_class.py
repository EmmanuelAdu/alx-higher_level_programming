#!/usr/bin/python3
"""Define is_same_class function"""


def is_same_class(obj, a_class):
    """Returns True if an object isinstance of a given class

    Args:
         obj - object to check the class
         a_class - the class
    """
    if type(obj) == a_class:
        return True
    return False
