#!/usr/bin/python3
"""
Module documentation:  This help to get a handle
on what methods are available to your object
"""


class MyList(list):
    """
    class doc:  MyList
    """
    def print_sorted(self):
        """
        Return a string representation of the sorted list
        """
        sorted_list = sorted(self)
        print(sorted_list)

