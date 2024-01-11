#!/usr/bin/python3
"""
This is a module that defines a class Square.
It has a mismatched attribute of size.
"""


class Square:
"""
Class documentation:  this class initializes instance of size
but mismatches with __size
"""

    def __init__(self, size=0):
        """
        Initialize the sqaure instance.o some tests - valueError and Type Error
        also type and value checking
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        # Check if the size is non-negative
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Return the area of the square.
        """
        return self.__size * self.__size


if __name__ == '__main__'
    Square()
