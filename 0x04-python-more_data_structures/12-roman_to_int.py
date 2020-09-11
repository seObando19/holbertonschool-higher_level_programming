#!/usr/bin/python3
def roman_to_int(roman_string):
    mydict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    if type(roman_string) != str and roman_string is None:
        return 0
    for i in range(len(roman_string)):
        if i > 0 and mydict[roman_string[i]] > mydict[roman_string[i - 1]]:
            res += mydict[roman_string[i]] - (mydict[roman_string[i - 1]] * 2)
        else:
            res += mydict[roman_string[i]]
    return res
