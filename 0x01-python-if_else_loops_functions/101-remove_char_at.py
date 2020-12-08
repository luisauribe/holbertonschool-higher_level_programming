#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    for x in str:
        if i != n:
            print("{}".format(x), end="")
        i = i+1
    return ""
