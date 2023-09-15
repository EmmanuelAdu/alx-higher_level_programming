#!/usr/bin/python3
"""Define an append text to file function"""


def append_write(filename="", text=""):
    """Appends and write text to file
    If file does not exist it creates file then appends the text

    Args:
         filename(file) - file to create and append text
         text(str) - data or text to write to file
    Return:
           Then number of characters appended
    """

    with open(filename, "a", encoding="utf-8") as my_file:
        return my_file.write(text)
