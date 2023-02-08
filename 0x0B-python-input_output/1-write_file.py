#!/usr/bin/python3

"""
Function to write a string to a  file in UTF8-Encoding
"""


def write_file(filename="", text=""):
    """
    Write `text` to `filename`, crete new file if `filename` doesn't exist
    """
    with open(filename, mode="w", encoding="utf-8") as fileName:
        fileName.write(text)
