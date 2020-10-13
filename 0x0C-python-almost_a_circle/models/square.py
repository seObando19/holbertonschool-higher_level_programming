#!/usr/bin/python3
"""
Define Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """

    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            Initialize square class
            Arguments:
                size (int): value to square side.
                x (int): integer number.Defaults to 0.
                y (int): integer numer. Defaults to 0.
                id (int): integer number.Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
            Return descriptor of Rectangle
            [Square] (<id>) <x>/<y> - <size>
        """
        respond = "[Square] ({}) {}/{} - {}"
        return respond.format(self.id, self.x,
                              self.y, self.width)

    @property
    def size(self):
        """
            Method get for size atribute
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            Method set for size atribute

            Arguments:
                value (int): value integer
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
           That assigns an argument to each attribute

            Arguments:
                args()
                kwargs()
        """
        attr = ['id', 'size', 'x', 'y']
        if 0 < len(args) <= 4:
            for i in range(len(args)):
                super().__setattr__(attr[i], args[i])
        else:
            for j in kwargs:
                super().__setattr__(j, kwargs[j])

    def to_dictionary(self):
        """
            Method that returns the dictionary
            representation of a Square
        """
        myDict = {'id': self.id,
                  'size': self.width,
                  'x': self.x,
                  'y': self.y}
        return myDict
