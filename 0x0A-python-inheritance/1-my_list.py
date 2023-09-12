#!/usr/bin/python3
"""Define an inherited class list MyList"""


class MyList(list):
    """Returns a sorted built-in list elements

    Args:
         list - the parent list inherited
    """
    def print_sorted(self):
        """Prints list in ascending sorted order"""
        print(sorted(self))
