#!/usr/bin/python3

"""
Function that creates an object from a JSON FILE

Functions:

    def load_from_json_file(filename)
"""
import json


def load_from_json_file(filename):
    """
    Function that returns an object from a file
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        data_read = f.read()
        json.loads(data_read)
