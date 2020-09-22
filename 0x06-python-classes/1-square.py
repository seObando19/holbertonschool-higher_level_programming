#!/usr/bin/python3
"""
Write a class Square that defines a square.
"""


class Square:
    """
    function inizialited
    """
    def __init__(self, size):
        self.__size = size

    """
    Square that defines a square
    """
    def retrieve(self):
        return self.__size ** 2
