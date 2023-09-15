#!/usr/bin/python3
"""Define a function that creates an Object from a JSON FILE"""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON FILE"""

    with open(filename) as f:
        return json.load(f)
