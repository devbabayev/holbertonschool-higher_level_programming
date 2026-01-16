#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        print("{} / {} = {}".format(a, b, a / b))
    except TypeError:
        return None
    finally:
        print("Inside result {}".format(a / b))
