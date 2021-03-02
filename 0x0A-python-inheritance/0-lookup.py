#!/usr/bin/python3
"""Module for lookup method."""


def lookup(obj):
    """
    Args:
        obj: The list object.
    Return:
        The list of available attributes and methods of an object.
    """
    return dir(obj)
