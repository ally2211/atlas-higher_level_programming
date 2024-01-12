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
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the sqaure instance
        with size and tuple
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """
        Getter for position
        """
        return self.__position

    @property
    def size(self):
        """
        Getter for size
        """
        return self.__size

    @position.setter
    def position(self, value):
        """
        setter for position with value and type setting
        """
        # check if int
                # Check for if value is a Tuple
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        # Check if have exactly 2 items in Tuple
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        # Check if both items are integers
        if not all(isinstance(item, int) and item >= 0 for item in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            return

        # Print the top margin (number of newlines before the square)
        print("\n" * self.position[1], end="")

        for i in range(self.__size):
            # Print the left margin (number of spaces before the square)
            print(" " * self.position[0], end="")

            # Print the square's row
            print("#" * self.__size)


if __name__ == '__main__':
    Square()
