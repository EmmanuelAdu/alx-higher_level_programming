#!/usr/bin/python3
'''Defining a class square'''


class Square:
    '''Initializing a private init size

    Args:
         size(int): the size of the square class
    '''
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        '''Get the current size of the the square'''
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Define and return the square size'''
        return (self.__size * self.__size)
