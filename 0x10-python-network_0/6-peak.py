#!/usr/bin/python3
"""Script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy.
"""


def find_peak(list_of_integers):
    """
    Return the peak in a list of integers
    """
    list_ = list_of_integers
    # if there is no list of integers return None
    if list_ == []:
        return None
    length = len(list_)

    start, end = 0, length - 1
    while start < end:
        mid = start + (end - start) // 2
        if list_[mid] > list_[mid - 1] and list_[mid] > list_[mid + 1]:
            return list_[mid]
        if list_[mid - 1] > list_[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return list_[start]
