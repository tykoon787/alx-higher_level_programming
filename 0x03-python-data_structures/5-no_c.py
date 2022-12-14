#!/usr/bin/python3

def no_c(my_string):
    str_list = list(my_string)
    index = 0
    for x in str_list:
        if x == 'c' or x == 'C':
            str_list[index] = ""
        index += 1
    return "".join(str_list)
