#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max = 0
        for val in range(len(my_list)):
            if my_list[val] > max:
                max = my_list[val]
        return max
    else:
        return None
