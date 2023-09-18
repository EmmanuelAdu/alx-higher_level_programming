#!/usr/bin/python3
"""Define inherited class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This represents an inherited Square from Rectangle(sub-parent)"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes its own attributes

        Args:
             size(int) - Size of the square
             x(int) - x coordinate of the square
             y(int) - y coordinate of the square
             id(int) - the identity of the square
        """
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of square when print is called"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Gets or returns the value of size"""
        return self.__width

    @size.setter
    def size(self, value):
        """Appropriately sets the size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value
