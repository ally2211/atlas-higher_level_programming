#!/usr/bin/python3
"""
Module Doc: Base Class for all other classes
"""


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
            self.id = id  # Assign the provided id to the public instance attribute
        else:
            Base.__nb_objects += 1  # Increment the private class attribute
            self.id = Base.__nb_objects  # Assign the incremented value to the public instance attribute
