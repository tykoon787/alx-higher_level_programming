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
        elif (list_dictionaries is None):
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Function that writes the list of objects (instances) to a json file

            Parameters:
                list_objs : List of objects

        """
        # Convert the list of instances to json string
        to_write = cls.to_json_string(list_objs)
        classname = cls.__name__
        filename = classname + ".json"
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(to_write)
