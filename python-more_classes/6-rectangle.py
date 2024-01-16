#!/usr/bin/python3
"""
a module to represent a rectangle
"""


class Rectangle:
    """
    A class to represent a rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        constructor for rectangle class
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        return area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        return perimeter of rectangle
        """
        return self.__width + self.__width + self.__height + self.__height

    def __str__(self):
        """
        returns string representation of rectangle using the # char
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle_str += "#"
            if i < self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        """
        returns official string representation of rectangle
        this string can be used with eval() to a create a new instance
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Destructor for the Rectangle class.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
