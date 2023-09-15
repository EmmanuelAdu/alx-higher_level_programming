#!/usr/bin/python3
"""Defines a function to return JSON Representation strings"""
import json


def to_json_string(my_obj):
    """Return json representation of a string(my_obj)"""

    return json.dumps(my_obj)
