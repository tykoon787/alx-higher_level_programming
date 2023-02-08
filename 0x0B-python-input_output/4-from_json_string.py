#!/usr/bin/python3
"""
Function that returns a string object back to a python object


Functions:

    from_json_string(my_str)
"""
import json


def from_json_string(my_str):
    """
    Function to return a string object back to a python object

        Parameters:
            my_str(string): String to be parsed

        Return:
            Python Object
    """
    return json.loads(my_str)
