#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lent = sys.argv
    if len(lent) <= 1:
        print("{} arguments.".format(len(lent) - 1))
    else:
        if len(lent) - 1 == 1:
            print("{} argument:".format(len(lent) - 1))
        else:
            print("{} arguments:".format(len(lent) - 1))
        for i in range(1, len(lent)):
            print("{} : {}".format(i, lent[i]))
