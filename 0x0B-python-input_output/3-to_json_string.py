#!/usr/bin/python3
"""
Function that returs the JSON Rep of an object(string)

Functions:

    to_json_string(my_obj)
"""
import json


def to_json_string(my_obj):
    """
    Function that returns the json representation of an object

        Parameters:
            my_obj(string): String to be parsed

        Return:
            Json Rep
    """
    return json.dumps(my_obj)
