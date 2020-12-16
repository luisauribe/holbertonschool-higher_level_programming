#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    cp = my_list.copy()
    for run in range(len(cp)):
        if cp[run] % 2 == 0:
            cp[run] = True
        else:
            cp[run] = False
    return cp
