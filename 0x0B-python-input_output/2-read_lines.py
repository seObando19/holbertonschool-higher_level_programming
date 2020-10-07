#!/usr/bin/python3
"""
    function that reads n lines of a text file
"""


def read_lines(filename="", nb_lines=0):
    """
     function that reads n lines of a text file
     and prints it to stdout.
    """
    with open(filename, "r", encoding='utf8') as myFile:
        if nb_lines <= 0 or nb_lines > len(myFile.readlines()):
            print(myFile.read(), end="")
        else:
            totLines = 0
            for line in myFile:
                totLines += 1
                print(myFile.readline(), end="")
                if totLines == nb_lines:
                    break
