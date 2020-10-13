#!/usr/bin/python3
"""
    Import module JSON
"""


import json


class Base:
    """
        Class base of all the project

        arguments:
            __nb_objects(integer)
        methods:
            __init__()
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Base class initialization method

            arguments:
                id(integer)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            function that returns the JSON representation
            of an object (string)

            Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            [str]: Json representation.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Write the JSON string representation.

            Args:
             list_objs (JSON object): JSON representation of list_objs.
        """
        filename = cls.__name__ + ".json"
        for value in list_objs:
            list_dict = value.to_dictionary()
        obj = cls.to_json_string(list_dict)
        with open(filename, mode='w', encoding='utf-8') as myFile:
            myFile.write(obj)
