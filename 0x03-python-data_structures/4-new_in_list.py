#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    i = 0
    copylist = my_list.copy()
    if idx < 0:
        return (my_list)
    for run in my_list:
        i = i + 1
    if idx > i - 1:
        return (my_list)
    copylist[idx] = element
    return (copylist)
