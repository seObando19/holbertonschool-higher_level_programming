#!/usr/bin/python3
for i in range(9):
    for a in range(i + 1, 10):
        if i == 8 and a == 9:
            print("{:d}{:d}".format(i, a), sep='')
        else:
            print("{:d}{:d}".format(i, a), end=', ')
