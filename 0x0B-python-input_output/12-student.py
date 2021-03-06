#!/usr/bin/python3
"""
Class student
"""


class Student:
    """
    Representation of a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Inialization of class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        newDict = {}
        for value in attrs:
            try:
                newDict[value] = self.__dict__[value]
            except:
                pass
        return newDict
