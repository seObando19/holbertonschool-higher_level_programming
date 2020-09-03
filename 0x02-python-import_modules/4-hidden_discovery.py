#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    data = dir(hidden_4)
    for i in data:
        if i[1] != '_':
            print(i)
