#!/usr/bin/python3
import json
"""
This is the Base Model Class containing the Base Class

Classes:
    Base

Functions:
    to_json_string(object, list_dictionary)
"""


class Base():
    """
    A  Base Class

    ...
    Attributes
    ----------
    nb_objects : int
        Number of objects created
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(self, list_dictionaries):
        """
        Function that convertes a dictionary to json_string

            Parameters:
                list_dictionary (dict) : Dictionary

            Return:
                Json String
        """
        if not list_dictionaries:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)
