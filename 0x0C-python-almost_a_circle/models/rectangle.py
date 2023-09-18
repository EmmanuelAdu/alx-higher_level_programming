#!/usr/bin/python3
"""Define an inherited class Rectangle from Base"""
from models.base import Base


class Rectangle(Base):
    """Represent a class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize class public instance

        Args:
             width(int) - The width of Rectangle
             height(int) - The height of the Rectangle
             x(int) - The x coordinate of the Rectangle
             y(int) - The y coordinate  of the Rectangle
             id(int) - The identity of the Rectangle

        Raises:
               TypeError - If either width or height or x or y not (int)
               ValueError - If either width or height <= 0
               ValueError - If either x or y < 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get height of the Rectangle"""
        return self.__width

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get x-cordinate of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-cordinate of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y-cordinate of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-cordinate of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Find the area"""
        return (self.__width * self.__height)

    def display(self):
        """Displays the rectangle with # """
        dsp = ""
        for y in range(self.y):
            print("")
        for h in range(0, self.__height):
            for x in range(self.x):
                print(" ", end="")
            for i in range(0, self.__width):
                dsp = "#"
                print(dsp, end="")
            print("")

    def __str__(self):
        """Overiding the str method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)
