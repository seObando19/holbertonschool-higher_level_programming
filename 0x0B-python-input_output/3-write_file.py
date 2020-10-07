#!/usr/bin/python3
"""
    function that writes a string
"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file

    Return:
    the number of characters written
    """
    with open(filename, "w") as myFile:
        return myFile.write(text)
