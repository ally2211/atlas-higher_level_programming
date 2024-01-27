#!/usr/bin/python3
"""
Module Doc: Base Class for all other classes
"""
import json
import os


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

    @classmethod
    def load_from_file(cls):
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as file:
            json_string = file.read()
        list_of_dicts = cls.from_json_string(json_string)
        instances = []
        for d in list_of_dicts:
            instance = cls.create(**d)
            instances.append(instance)
        return instances

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        if list_objs is None or list_objs = []:
            raise ValueError("list_objs cannot be None or empty")
        list_dictionaries = []
        if list_objs:
            for obj in list_objs:
                list_dictionaries.append(obj.to_dictionary())

        filename = f"{cls.__name__}.json"

        with open(filename, 'w') as file:
            file.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Factory method to create a new Rectangle instance"""
        # Creating a dummy instance with default values
        dummy_instance = cls(1, 1)  # default values
        # Updating dummy instance with actual values from dictionary
        dummy_instance.update(**dictionary)
        return dummy_instance
