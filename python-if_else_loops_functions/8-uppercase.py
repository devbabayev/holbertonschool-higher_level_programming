#!/usr/bin/python3
def uppercase(str):
    for i in str:
        letter = i
        if ord(letter) > 96 and ord(letter) < 123:
            letter = ord(letter) - 32
        print("{}".format(chr(letter), end=""))
