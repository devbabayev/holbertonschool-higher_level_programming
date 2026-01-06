#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = len(sys.argv)

    sum = 0
    for i in range(1, argv):
        sum = int(sum + sys.argv[i])

