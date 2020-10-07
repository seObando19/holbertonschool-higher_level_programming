#!/usr/bin/python3

"""
Class Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Class Square
    """
    def __init__(self, size):
        """
            Inialization od Square class

            Args:
                size: size of square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
            Implement area method
        """
        return self.__size * self.__size
