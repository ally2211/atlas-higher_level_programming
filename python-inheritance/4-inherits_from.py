#!/usr/bin/python3
"""
class doc:  determine if same object
"""


def inherits_from(obj, a_class):
    """
    function to check if an object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class.  Therefore given a=True, it would return False.
    """
    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return True
    else:
        return False
