#!/usr/bin/python3
"""Defines a function that returns no. of strings written"""


def write_file(filename="", text=""):
    """Returns the no. of strings written to stdout

    Args:
         filename(file) - the file to write to
         text(str) - the text to write to file
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        return my_file.write(text)
