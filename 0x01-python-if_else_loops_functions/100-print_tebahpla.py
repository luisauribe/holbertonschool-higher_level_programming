#!/usr/bin/python3
for x in range(122, 96, -1):
    if x % 2 == 0:
        lower = chr(x)
    else:
        lower = chr(x - 32)
    print("{}".format(lower), end="")
