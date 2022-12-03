#!/usr/bin/python3
def islower(c):
    for letters in range(ord('a'), ord('z') + 1):
        if letters == ord(c):
            return True
        else:
            return False
