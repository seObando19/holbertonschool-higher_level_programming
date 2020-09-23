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
        """
	Initialize square object
        """
        self.size = size

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
