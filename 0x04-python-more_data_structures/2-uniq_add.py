#!/usr/bin/python3
def uniq_add(my_list=[]):
    container = set(my_list)
    result = 0
    for i in container:
        result = result + i
    return (result)
