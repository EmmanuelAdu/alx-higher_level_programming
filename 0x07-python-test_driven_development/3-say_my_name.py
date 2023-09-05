#!/usr/bin/python3
"""Define function that prints name of a person"""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first_name> <last_name>

    Args:
         first_name(str) - the first name to be passed
         last_name(str) - the second name to pass (optional)

    Raises:
           TypeError: If either of first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
