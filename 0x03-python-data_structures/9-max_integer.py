#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    if len(my_list) == 0:
        return "None"
    for val in range(len(my_list)):
        if my_list[val] > max:
            max = my_list[val]
    return max
