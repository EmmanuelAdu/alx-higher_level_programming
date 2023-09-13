#!/usr/bin/python3
"""Defines a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a text after each line containing a giving string(searchstring)

    Args:
         search_string(str) - The string to search for before inserting
         new_string(str) - The string to be inserted
    """
    text = ""

    with open(filename) as my_file:
        for line in my_file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as new_file:
        new_file.write(text)
