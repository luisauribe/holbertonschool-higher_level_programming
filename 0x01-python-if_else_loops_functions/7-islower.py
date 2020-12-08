#!/usr/bin/python3
def islower(c):
    for x in range(97, 122):
        if x == ord(c):
            return True
    return False
