#!/usr/bin/python3
"""
Has a function that returns if the object
is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Function that returns if the object
    is exactly an instance of the specified class

    ....
        Parameters:
            obj (object): Object to be checked

            a_class (cls): Reference

        Return:
            True, if instance.
    """
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
