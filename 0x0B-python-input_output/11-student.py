#!/usr/bin/python3
"""
Class student
"""


class Student:
    """
    Clas Student

    atr:
        first_name
        Last_name
        age

    method:
        def to_json(self)
    """
    def __init__(self, first_name, Last_name, age):
        """
        Inialization of class
        """
        self.first_name = first_name
        self.Last_name = Last_name
        self.age = age

    def to_json(self):
        """
        retrieves a dictionary representation of a Student instance
        """
        return self.__dict__
