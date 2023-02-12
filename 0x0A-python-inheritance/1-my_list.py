#!/usr/bin/python3
# Clas myList inheriting from List


class MyList(list):
    def print_sorted(self):
        """
        Prints a list, but sorted
        """
        final_list = list(self)
        final_list.sort()
        print(final_list)
