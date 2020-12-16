#!/usr/bin/python3
def max_integer(my_list=[]):
    l = len(my_list)
    my_list.sort()
    if l != 0:
        return my_list[-1]
    else:
        return None
