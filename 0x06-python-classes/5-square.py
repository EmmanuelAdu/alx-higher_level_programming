#!/usr/bin/python3
'''Define a class square and print a square'''


class Square:
    '''Define an init private size

    Args:
         size(int): the size of the square
    '''
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        '''Get the current size'''
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Return the square of the size'''
        return (self.__size * self.__size)

    def my_print(self):
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
