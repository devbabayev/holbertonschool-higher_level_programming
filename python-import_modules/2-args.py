#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    count = len(argv) - 1

    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument:".format(count))
        print("{}: {}".format(count, sys.argv[1]))
    else:
        print("{} arguments".format(count))
        for i in range(0, count):
            print("{}: {}".format(count, sys.argv[i]))
