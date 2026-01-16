#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if '0' < value < '9':
            print("{:d}".format(value))
            return True
    except TypeError:
        print("{} is not an integer".format(value))
        return False
