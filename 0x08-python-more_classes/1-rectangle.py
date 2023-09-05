#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """Create Private Instances for class Rectangle that takes 2 args

    Args:
         width - width of rectangle
         height - height of rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Create a property for the width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set conditions and exceptions for the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Create a property for the height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set conditions and exceptions for the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
