#!/usr/bin/python3
"""
Define Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """
        Rectangle class that inherance from Base class

        inherance:
            base.py
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Base class initialization method

            Arguments:
                id (cls): base class
                width (int): value integer
                height (int): value integer
                x (int): value integer
                y (int): value integer
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            Method get for width atribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Method set for width atribute

            Arguments:
                value (int): value integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
            Method get for height atribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Method set for height atribute

            Arguments:
                value (int): value integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
            Method get for x atribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            Method set for x atribute

            Arguments:
                value (int): value integer
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
            Method get for y atribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            Method set for y atribute

            Arguments:
                value (int): value integer
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
            Method than return area of rentangle
        """
        return self.__width * self.__height

    def display(self):
        """
            Method for represation of rectangle with symbol #
        """
        rect = []
        for _ in range(self.y):
            print('')
        for _ in range(self.height):
            rect.append(' ' * self.x + '#' * self.width)
        print(*rect, sep="\n")

    def __str__(self):
        """
            Return descriptor of Rectangle

            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        respond = "[Rectangle] ({}) {}/{} - {}/{}"
        return respond.format(self.id,
                              self.__x,
                              self.__y,
                              self.__width,
                              self.__height)

    def update(self, *args, **kwargs):
        """
            That assigns an argument to each attribute

            Arguments:
                args()
                kwargs()
        """
        attr = ['id', 'width', 'height', 'x', 'y']
        if 0 < len(args) <= 5:
            for i in range(len(args)):
                super().__setattr__(attr[i], args[i])
        else:
            for j in kwargs:
                super().__setattr__(j, kwargs[j])

    def to_dictionary(self):
        """
            Method that returns the dictionary
            representation of a Rectangle
        """
        myDict = {'id': self.id,
                  'width': self.width,
                  'height': self.height,
                  'x': self.x,
                  'y': self.y}
        return myDict
