#!/usr/bin/python3
"""
Module Doc: Square Class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle class.
    Represents a square with a size.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.
        """
        super().__init__(size, size)
