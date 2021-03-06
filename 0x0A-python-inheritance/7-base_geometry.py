#!/usr/bin/python3
"""
Write an empty class BaseGeometry.
"""


class BaseGeometry:
    """
    Write an empty class BaseGeometry.
    """
    def area(self):
        """
            Method that raises an Exception with
            the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Method than validates value
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
