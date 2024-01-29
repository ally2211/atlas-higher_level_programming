#!/usr/bin/python3
"""
Module Doc:  returns dictionary of student
"""


class Student:
    """
    Class doc that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        """
        # Check if attrs is a list
        if isinstance(attrs, list):
            # Check if every element in attrs is a string
            all_strings = True
            for attr in attrs:
                if not isinstance(attr, str):
                    all_strings = False
                    break

            # If all elements in attrs are strings, return specified attributes
            if all_strings:
                attributes = {}
                for attr in attrs:
                    if hasattr(self, attr):
                        attributes[attr] = getattr(self, attr, None)
                return attributes

        # If attrs is not a list of strings, return all attributes
        attributes = {}
        for attr in dir(self):
            if not attr.startswith("__") and not callable(getattr(self, attr)):
                attributes[attr] = getattr(self, attr)
        return attributes
