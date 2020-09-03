#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    size = len(argv)
    acum = 0
    if size == 1:
        print(0)
    else:
        for i in range(1, size):
            acum += int(argv[i])
        print("{}".format(acum))
