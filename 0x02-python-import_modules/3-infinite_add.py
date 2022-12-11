#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    def add():
        result = 0
        index = 1
        length = len(sys.argv)
        if (length == 1):
            print(0)
        elif (length) > 1:
            while (length != 1):
                result += int(sys.argv[index])
                index += 1
                length -= 1

        print("{:d}".format(result))

    add()
