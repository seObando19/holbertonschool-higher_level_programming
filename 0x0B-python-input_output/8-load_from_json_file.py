#!/usr/bin/python3
"""
import  json module
"""


import json


def load_from_json_file(filename):
    """
        function that creates an Object from a “JSON file”
    """
    with open(filename, encoding='utf8') as myFile:
        return json.load(myFile)
