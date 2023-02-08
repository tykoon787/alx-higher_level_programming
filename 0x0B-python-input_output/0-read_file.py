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
            line = fileName.read().splitlines()
            if not line:
                break
            else:
                for i in line:
                    if i != "":
                        print(i)
                    else:
                        print("")
