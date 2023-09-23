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
        return self.width

    @size.setter
    def size(self, value):
        """Appropriately sets the size"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            i = 0
            for arg1 in args:
                if i == 0:
                    if not isinstance(arg1, int) and arg1 is not None:
                        raise TypeError("id must be an integer")
                    self.id = arg1
                elif i == 1:
                    self.size = arg1
                elif i == 2:
                    self.x = arg1
                elif i == 3:
                    self.y = arg1
                i += 1
        else:
            for k, v in kwargs.items():
                if k == "id":
                    if not isinstance(v, int) and v is not None:
                        raise TypeError("id must be an integer")
                if k == "size":
                    self.size = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v

    def to_dictionary(self):
        """Represents the dictionary representation of a square"""
        my_dict = {'id': self.id, 'size': self.size, 'x': self.x,
                   'y': self.y}
        return my_dict
