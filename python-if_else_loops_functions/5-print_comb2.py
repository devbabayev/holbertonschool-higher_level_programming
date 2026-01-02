#!/usr/bin/python3
for comb in range(0, 100):
    if comb < 10:
        print(str(0)+str("{}".format(comb)), end=", ")
    else:
        print("{}".format(comb), end=", ")
