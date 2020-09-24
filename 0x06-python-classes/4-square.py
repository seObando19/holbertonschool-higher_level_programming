#!/usr/bin/python3
"""
Write a class Square that defines a square.
"""


class Square:
    """init Square and raising error"""
    def __init__(self, size=0):
        self.size = size
	'''getter size'''
    @property
    def size(self):
        return self.__size
    '''setter size'''
    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
