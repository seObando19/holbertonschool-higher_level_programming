#!/usr/bin/python3
"""
    Class Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define class Rectangle
    Args:
        BaseGeometry (BaseGeometry): superclass
    """
    def __init__(self, width, height):
        """
            Inialization od Rectangle class

            Args:
                width: width of rectangle
                height: height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
