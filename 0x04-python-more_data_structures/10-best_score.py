#!/usr/bin/python3
def best_score(a_dictionary):
    val_max = None
    if a_dictionary:
        val_max = max(a_dictionary, key=a_dictionary.get)
    return val_max
