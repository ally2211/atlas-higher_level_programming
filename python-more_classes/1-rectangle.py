#!/usr/bin/python3
"""
a module to represent a rectangle
"""


class Rectangle:
    """
    A class to represent a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        constructor for rectangle class
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter for width
        """
        return self.__width

    @property
    def height(self):
        """
        getter for height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        setter for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        setter for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
