#!/usr/bin/python3
import json


"""
A function that returs the JSON Rep of an object(string)
"""


def to_json_string(my_obj):
    """
    Function that returns the json representation of an object
    """
    return json.dumps(my_obj)
