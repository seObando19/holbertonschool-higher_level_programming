#!/usr/bin/python3
"""
Write an empty class BaseGeometry.
"""


class BaseGeometry(Exception):
    def area(self):
        """
            Method that raises an Exception with
            the message area() is not implemented
        """
        raise Exception("area() is not implemented")
