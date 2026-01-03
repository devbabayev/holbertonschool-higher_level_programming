#!/usr/bin/python3
def uppercase(str):
    for i in str:
        letter = i
        sentence = " "
        if ord(letter) > 96 and ord(letter) < 123:
            sentence = sentence + str(ord(letter) - 32)
        else:
            sentence = sentence + letter
