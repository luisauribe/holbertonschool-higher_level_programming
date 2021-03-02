#!/usr/bin/python3
"""Module for MyList class."""


class MyList(list):
    """This class inherits from list."""
    def print_sorted(self):
        """This method print the sorted list."""
        print(sorted(self))
