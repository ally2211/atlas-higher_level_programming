#!/usr/bin/python3
"""
Module Doc: Rectangle Class
"""
# Rectangle that inherits from BaseGeometry
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry class.
    Represents a rectangle with width, height,
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be greater than 0")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be greater than 0")
        self.__width = width
        self.__height = height
