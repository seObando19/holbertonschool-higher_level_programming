#!/usr/bin/python3
"""
    Module append
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file

    Return:
     returns the number of characters added
    """
    with open(filename, "a", encoding='utf8') as myFile:
        return myFile.write(text)
