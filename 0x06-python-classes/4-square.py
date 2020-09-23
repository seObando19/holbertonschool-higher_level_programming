#!/usr/bin/python3
"""
Write a class Square that defines a square.
"""


class Square:
    """Create an instance of a square object

    Attributes:
        size: integer number
    """
    def __init__(self, size=0):
        """ Initialize square object

        Args:
            size (int): side of the square
       """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    def area(self):
        return self.__size ** 2
