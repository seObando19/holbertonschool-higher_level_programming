#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle:
    """
        method initialized
    """
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
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

    """
        should print the rectangle with the character #
    """
    def __str__(self):
        valPrint = ""
        if self.width is 0 or self.height is 0:
            return valPrint
        else:
            w = self.width
            h = self.height
            for i in range(h):
                if i + 1 < h:
                    valPrint += "#" * w + "\n"
                else:
                    valPrint += "#" * w
        return valPrint

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Delete base class part of the instance
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
