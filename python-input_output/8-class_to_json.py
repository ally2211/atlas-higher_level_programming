#!/usr/bin/python3
"""
Module Doc:  given an instant of a class return dictionary
"""


def class_to_json(obj):
    """
    Write a function that returns 
    the dictionary description 
    with simple data structure 
    (list, dictionary, string, integer and boolean) 
    for JSON serialization of an object:
    """
    serializable_types = (list, dict, str, int, bool)
    obj_dict = {}
    for attr in dir(obj):
        # Get the attribute's value
        value = getattr(obj, attr)
        # Check if the attribute is serializable and not a built-in attribute or method
        if isinstance(value, serializable_types) and not attr.startswith("__"):
            obj_dict[attr] = value
    return obj_dict
