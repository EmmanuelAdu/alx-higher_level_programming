#!/usr/bin/python3
"""Defines A python_to_JSON class function"""


def class_to_json(obj):
    """Return the dictionary representation of a simple data structure"""

    return obj.__dict__
