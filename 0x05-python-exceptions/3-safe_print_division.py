#!/usr/bin/python3
def safe_print_division(a, b):
    ret = None
    try:
        ret = a / b
        print(ret)
    except ZeroDivisionError:
        ret = None
    finally:
        print("Inside result:", "{}".format(ret))
    return ret
