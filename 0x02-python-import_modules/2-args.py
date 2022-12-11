#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    len = len(sys.argv)
    counter = 1

    if len == 1:
        print("0 arguments.")
    elif len == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    elif len > 2:
        print("{} arguments:".format(len - 1))
        while (len != 1):
            print("{}: {}".format(counter, sys.argv[counter]))
            counter = counter + 1
            len = len - 1
