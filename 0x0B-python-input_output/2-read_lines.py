#!/usr/bin/python3
"""
    function that reads n lines of a text file
"""


def read_lines(filename="", nb_lines=0):
    """
     function that reads n lines of a text file
     and prints it to stdout.
    """
    with open(filename, encoding='utf8') as myFile:
        if nb_lines <= 0 or nb_lines > len(myFile.readlines()):
            print(myFile.read(), end="")
        else:
            myFile.seek(0)
            for line in range(nb_lines):
                print(myFile.readline(), end="")
