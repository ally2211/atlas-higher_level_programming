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

    def __init__(self, size):
        """
        Initialize Square instance with size.
        """
        self.__size = size


if __name__ == "__main__":
    Square()
