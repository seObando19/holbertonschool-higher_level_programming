#!/usr/bin/python3
"""
Write a class Square that defines a square.
"""


class Square:
    """
    Define square
    """
    def __init__(self, size=0):
        """
        Validate size value and Initialize Square attribute
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
