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

    @property
    def size(self):
        """
        Getter for size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter for size with value and type setting
        """
        # Check if int
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        # Check if is non negative
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Return the area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        print # square times
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()


if __name__ == '__main__':
    Square()
