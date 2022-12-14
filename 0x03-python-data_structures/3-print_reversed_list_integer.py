#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        length = len(my_list) * -1
        loop_index = -1
        while (loop_index >= length):
            print("{:d}".format(my_list[loop_index]))
            loop_index -= 1
