#!/usr/bin/python3
"""
Module Doc: covert from json
"""
import json


def load_from_json_file(filename):
    """
    load from json to a file
    """
    with open(filename, 'r') as file:
        my_list = json.load(file)
    return my_list
