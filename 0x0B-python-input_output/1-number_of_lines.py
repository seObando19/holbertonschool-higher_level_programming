#!/usr/bin/python3
"""
    Module for number lines
"""


def number_of_lines(filename=""):
    """
    function that returns the number
    of lines of a text file
    """

    with open(filename, encoding='utf8') as myFile:
        return len(myFile.readlines())
