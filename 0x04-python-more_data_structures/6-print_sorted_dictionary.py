#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    newList = list(sorted(a_dictionary.keys()))
    for i in range(len(newList)):
        print("{}: {}".format(newList[i], a_dictionary.get(newList[i])))
