#!/usr/bin/python3
"""Define class Rectangle """


class Rectangle:
    """Introduces a static method to return the bigger rectangle

    Attributes:
               number_of_instances(int) - keeps track of class instances made
               print_symbol(any type) - prints a string represetation of class
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """Finding the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Finding the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the bigger area

        Args:
             rect_1(Rectangle) - first rectangle
             rect_2(Rectangle) - second rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a Rectangle with width and height equal to size

        Args:
             size(int) - size of the square
        """
        return (cls(size, size))

    def __str__(self):
        """Printing the object representation of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle_str = ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                rectangle_str += str(self.print_symbol)
            if i < self.__height - 1:
                rectangle_str += '\n'
        return rectangle_str

    def __repr__(self):
        """Return the string representation of the Class Rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message for every deletion of rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
