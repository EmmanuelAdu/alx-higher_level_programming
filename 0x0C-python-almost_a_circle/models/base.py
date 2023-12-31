#!/usr/bin/python3
"""Defines a main class "Base" for all other projects in this task"""

import turtle
import json
import csv
import os


class Base:
    """This is the main base

    Private Class Attribute:
            __nb_objects(int) - to find the no. of class objects instantiated
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a base

        Args:
             id(int) - the identity of base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        if (type(list_dictionaries) != list or not
                all(type(d) == dict for d in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)
