#!/usr/bin/python3
"""
Module Doc: Rectangle Class
"""
# Assuming the Base class is defined in models/base.py
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base class.
    Represents a rectangle with width, height,
    and optional x, y coordinates, and id.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.
        """
        super().__init__(id)  # Initialize the base class with the id
        # Set the dimensions and coordinates using the property setters
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """
        calculate area of rectangle
        """
        return self.width * self.height

    def display(self):
        """
        print # for rectangle
        """
        for i in range(self.height):
            for j in range(self.width):
                print('#', end='')
            print()  # Newline after each row

    def __str__(self):
        """
        overriding ___str___ method
        """
        return '[Rectangle] ({}) {}/{} - {}/{}'.format
        (self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """int: Gets or sets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """int: Gets or sets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """int: Gets or sets the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """int: Gets or sets the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
