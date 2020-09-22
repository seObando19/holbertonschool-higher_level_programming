#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
        print("Inside result: ", end="")
    except:
        print("Inside result: ", end="")
        return None
    finally:
        print("{}".format(result))
        return result
