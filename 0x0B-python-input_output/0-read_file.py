#!/usr/bin/python3
"""Creating a function that reads a text"""


def read_file(filename=""):
    """Open and prints the contents of file to stdout"""
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end="")
