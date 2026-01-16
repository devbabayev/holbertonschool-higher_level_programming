#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        print("Inside result {}".format(a / b))
    except TypeError:
        return None
    finally:
        print("{} / {} = {}".format(a / b))
