#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    list_cpy = my_list
    if idx < 0:
        return (list_cpy)
    elif (idx >= len(my_list)):
        return (list_cpy)
    else:
        list_cpy[idx] = element
        return (list_cpy)
