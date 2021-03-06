#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle:
    """
        method initialized
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """
        getter width
    """
    @property
    def width(self):
        return self.__width

    """
        setter width
    """
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """
        getter height
    """
    @property
    def height(self):
        return self.__height

    """
        setter height
    """
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """
        method for return Area to rectangle
    """
    def area(self):
        return self.width * self.height

    """
        method for return perimeter to rectangle
    """
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
