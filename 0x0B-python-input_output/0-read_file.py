#!/usr/bin/python3
"""
    Module read
"""


def read_file(filename=""):
    """
    function that reads a text file
    and print it stdout.
    """

    with open(filename, "r", encoding='utf8') as myFile:
        print(myFile.read(), end="")
