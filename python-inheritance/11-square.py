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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be greater than 0")
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Override the __str__ of the Square.
        """
        return ('[Square] {}/{}'
                .format(self.__size, self.__size))