#!/usr/bin/python3
import json
"""
import  json module
"""


def save_to_json_file(my_obj, filename):
    """
        function that writes an Object to a text file,
        using a JSON representation
    """
    with open(filename, "w", encoding='utf8') as myFile:
        json.dump(my_obj, myFile)
