#!/usr/bin/python3
"""
Class MyList using inherance of class list
"""


class MyList(list):
    """
        function print_sorted
        prints the list, but sorted (ascending sort)
    """
    def print_sorted(self):
        print(sorted(self))
