#!/usr/bin/python3
"""
function that adds 2 integers.
"""


def add_integer(a, b=98):
    """Add two numbers

    Args:
        a (int):first param
        b (int):second param

    Return:
        int: add of two params
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return a + b
