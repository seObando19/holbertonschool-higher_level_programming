#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_Tuple = (0, 0)
    tupleOne = tuple_a + new_Tuple
    tupleTwo = tuple_b + new_Tuple
    return tupleOne[0] + tupleTwo[0], tupleOne[1] + tupleTwo[1]
