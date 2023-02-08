#!/usr/bin/python3

def read_file(filename=""):
    """
    Function that reads a file
    """
    with open(filename, mode="r", encoding="utf-8") as fileName:
        while True:
            line = fileName.readline()
            if not line:
                break
            print(line)
