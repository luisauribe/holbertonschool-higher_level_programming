#!/usr/bin/python3
def multiply_by_2(a_dictionary):
        container = a_dictionary.copy()
        for run in a_dictionary:
                container[run] = container[run] * 2
        return container
