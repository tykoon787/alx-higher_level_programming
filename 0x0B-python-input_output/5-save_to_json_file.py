#!/usr/bin/python3

"""
Function that saves an object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that saves an object to a text file

        Parameters:
            my_obj(object): Object
            filename(string): Name of the File

        Return:
            No of bytes written
    """
    parsed_object = json.dumps(my_obj)
    with open(filename, mode="w", encoding="utf-8") as f:
        return (f.write(parsed_object))
