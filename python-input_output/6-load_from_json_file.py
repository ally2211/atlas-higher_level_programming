#!/usr/bin/python3
"""
Module Doc: covert from json
"""
import json
import os

def load_from_json_file(filename):
    """
    load from json to a file
    """
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    else:
        return []
