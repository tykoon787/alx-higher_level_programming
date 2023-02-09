#!/usr/bin/python3
import json
"""
Base Model Class
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
            json.dumps(list_dictionaries)
