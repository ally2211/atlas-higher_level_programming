#!/usr/bin/python3
"""
class doc:  determine if same object
"""


def is_same_class(obj, a_class):
    """
    function to compare classes
    """
    if type(obj) is a_class:
        return True
    else:
        return False
