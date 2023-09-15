#!/usr/bin/python3
"""Define a write object_to_textfile using Json Representation"""
import json


def save_to_json_file(my_obj, filename):
    """Write object to file using JSON Representation strings

    Args:
         my_obj - object to write
         filename - file
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
