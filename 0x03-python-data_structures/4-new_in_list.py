#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_lista = list.copy(my_list)
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_lista[idx] = element
    return new_lista
