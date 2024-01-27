#!/usr/bin/python3
"""
Module Doc: Base Class for all other classes
"""
import json

class Base:
    """
    class Doc: Base Class
    """
    __nb_objects = 0  # Private class attribute

    def __init__(self, id=None):
        """
        function Desc:  init
        """
        if id is not None:
            # Assign the provided id to the public instance attribute
            self.id = id
        else:
            # Increment the private class attribute
            Base.__nb_objects += 1
            # Assign the incremented value to the public instance attribute
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
