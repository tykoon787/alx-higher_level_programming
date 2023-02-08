#!/usr/bin/python3

"""
Function to read a file from file name

"""


def read_file(filename=""):
    """
    Reads a file, filename
    """
    with open(filename, mode="r", encoding="utf-8") as fileName:
        # Run until you find a break statement
        while True:
            # split the lint into a list
            line = fileName.read().splitlines()
            # Check for an empty line
            if not line:
                break
            else:
                # Loop throught the list containing the string while printinh
                for i in line:
                    if i != "":
                        print(i)
                    else:
                        print("")
