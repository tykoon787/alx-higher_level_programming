#!/usr/bin/python3
# Function that retursn the list of available
# attributes and methods of an object
"""
Function taht returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Function that returns the list of available
    attributes and methods of an object
    ...
        Parameters:
        obj (object) : Object list to be returned
    """
    return (dir(obj))
