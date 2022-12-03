#!/usr/bin/python3
for letter_code in range(ord('a'), ord('z')):
    letters = chr(letter_code);
    if letters not in "qe":
        print(letters, end="")
