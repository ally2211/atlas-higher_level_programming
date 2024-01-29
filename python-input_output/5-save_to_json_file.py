#!/usr/bin/python3
"""
Module Doc: covert from json
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save to filename
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
