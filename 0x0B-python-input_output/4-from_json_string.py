#!/usr/bin/python3
"""Define a Json_to_Object function"""
import json


def from_json_string(my_str):
    """Return the object representation of a Json_string"""

    return json.loads(my_str)
