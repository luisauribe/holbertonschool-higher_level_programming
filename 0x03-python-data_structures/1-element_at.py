#!/usr/bin/python3
def element_at(my_list, idx):
    i = 0
    if idx < 0:
        return (None)
    for run in my_list:
        i = i + 1
        if run == idx + 1:
            return run
    if idx > i - 1:
        return (None)
