#!/usr/bin/python3
"""Module for MyInt class."""


class MyInt(int):
    """MyInt class."""
    def __eq__(self, other):
        """If are equals, inverting it."""
        return int(self) != int(other)

    def __ne__(self, other):
        """If are not-equals, inverting it."""
        return int(self) == int(other)
