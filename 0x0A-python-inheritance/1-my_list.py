#!/usr/bin/python3
# Clas myList inheriting from List
"""
Class inheriting from list
"""


class MyList(list):
    """
    Class inheriting from my list
    """
    def print_sorted(self):
        """
        Prints a list, but sorted
        """
        final_list = list(self)
        final_list.sort()
        print(final_list)
