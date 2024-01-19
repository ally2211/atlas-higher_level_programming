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
        for i in range(len(self)):
            try:
                isinstance(i, int)
            except (TypeError):
                raise TypeError
       
        sorted_list = sorted(self)
        print(sorted_list)
        
    def __str__(self):
        return str(sorted(self))
