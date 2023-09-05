#!/usr/bin/python3
"""Define Class Rectangle"""


class Rectangle:
    """Create a private instance for the height and width of the rectangle

    Args:
         width - (int) represents the width of the rectangle
         height - (int) represents the height of the rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Creating the private width attribute
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set conditions for exceptions of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Create private height attribute
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set conditions for exceptions of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
