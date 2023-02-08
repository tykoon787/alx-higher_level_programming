#!/usr/bin/python3

"""
Function to read a file from file name

"""


def read_file(filename=""):
    """
    Reads a file, filename
    """
    with open(filename, mode="r", encoding="utf-8") as fileName:
        while True:
            line = fileName.readline()
            if not line:
                break
            print(line)
