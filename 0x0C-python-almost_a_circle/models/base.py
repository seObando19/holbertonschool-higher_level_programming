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
        if not list_dictionaries:
            return json.dumps(list())
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Write the JSON string representation.

            Args:
             list_objs (JSON object): JSON representation of list_objs.
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode='w', encoding='utf-8') as myFile:
            if list_objs is None:
                obj = cls.to_json_string(list())
            else:
                list_dict = [value.to_dictionary() for value in list_objs]
                obj = cls.to_json_string(list_dict)
            myFile.write(obj)

    @staticmethod
    def from_json_string(json_string):
        """
            list of the JSON string representation
            Args:
                json_string (str): string representing
                a list of dictionaries
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """

        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
