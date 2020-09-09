#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_List = list.copy(my_list)
    for value in range(len(my_list)):
        if my_list[value] % 2 == 0:
            new_List[value] = True
        else:
            new_List[value] = False
    return new_List
