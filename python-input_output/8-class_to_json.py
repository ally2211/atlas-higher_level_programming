#!/usr/bin/python3


def class_to_json(obj):
    """
    Write a function that returns 
    the dictionary description 
    with simple data structure 
    (list, dictionary, string, integer and boolean) 
    for JSON serialization of an object:
    """
    obj_dict = {}
    for key in dir(obj):
        value = getattr(obj, key)
        if key[0] != '_' and not callable(value):
            obj_dict[key] = value
    return obj_dict
