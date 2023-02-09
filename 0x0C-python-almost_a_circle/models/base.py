#!/usr/bin/python3
"""
This is the Base Model Class containing the Base Class

Classes:
    Base

Functions:
    to_json_string(object, list_dictionary)
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries: dict):
        """
        Function that convertes a dictionary to json_string

            Parameters:
                list_dictionary (dict) : Dictionary

            Return:
                Json String
        """
        if (len(list_dictionaries) == 0):
            return ("[]")
        if (list_dictionaries is None):
            return ("[]")
        else:
            return json.dumps(list_dictionaries)
