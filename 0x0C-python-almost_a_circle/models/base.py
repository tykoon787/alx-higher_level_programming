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
    def to_json_string(list_dictionaries):
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
        classname = cls.__name__
        filename = classname + ".json"
        with open(filename, mode="w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                to_write = cls.to_json_string(
                    [item.to_dictionary() for item in list_objs])
                f.write(to_write)

    @classmethod
    def from_json_string(cls, json_string):
        """
        Function that Convertes a json string to a list of the JSON string rep

            Parameters:
                json_string (str): Json string to load

            Return:
                Object
        """
        if type(json_string) != str or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes set
        """
        if cls.__name__ == "Rectangle":
            temp = cls(1, 2)
        if cls.__name__ == "Square":
            temp = cls(1)

        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        filenames = ["Rectangle.json", "Square.json"]
        filename = cls.__name__ + ".json"
        for filename in filenames:
            if filename is filenames:
                with open(filename, mode="r", encoding="utf-8") as f:
                    json_string = f.read().splitlines()
                    list_of_instances = cls.from_json_string(json_string)
                    final = []
                    for item in list_of_instances:
                        dict = item.to_dictionary()
                        created_instance = cls.create(**dict)
                        final.append(created_instance)
                return (final)
            else:
                return ([])
