#!/usr/bin/python3
"""
Function that returns True if the object is an instance of a is
class that inherited (directly or indirectly) from the specified
class ; otherwise False
"""


def inherits_from(obj, a_class):
    """
    Function that returns True if the object is an instance of a is
    class that inherited (directly or indirectly) from the specified
    class ; otherwise False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
