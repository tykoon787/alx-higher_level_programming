#!/usr/bin/python3

"""
Function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    Appends a file and Returns the number of bytes added to the file

        Parameter:
                filename (string) : File name
                text (string) : String to be appended

        Returns:
                Number of bytes added
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return (f.write(text))
