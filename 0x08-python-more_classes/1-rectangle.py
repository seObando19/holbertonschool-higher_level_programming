#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle:

    def __init__(self, width=0, height=0):
        """
            method initialized
        """
        self.width = width
        self.height = height

    def width(self):
        """
            getter method
        """
        return self.__width

    def width(self, value):
        """
            setter method
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """
            getter method
        """
        return self.__height

    def height(self, value):
        """
            setter method
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
