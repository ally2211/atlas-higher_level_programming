#!/usr/bin/python3
"""
Module Doc: covert to json
"""
import json


def to_json_string(my_obj):
    """
    dump to JSON
    """
    # Convert set to list
    if isinstance(my_obj, set):
        my_obj = list(my_obj)
    json.dumps(my_obj)
    return json.dumps(my_obj)
