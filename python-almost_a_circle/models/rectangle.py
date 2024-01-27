#!/usr/bin/python3
"""
Module Doc: Rectangle Class
"""
# Assuming the Base class is defined in models/base.py
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base class.
    Represents a rectangle with width, height, and optional x, y coordinates, and id.
    """
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle. Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle. Defaults to 0.
            id (int, optional): An optional id of the rectangle. Defaults to None.
        """
        super().__init__(id)  # Initialize the base class with the id
        # Set the dimensions and coordinates using the property setters
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: Gets or sets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value  # Here, you might want to add validation for width

    @property
    def height(self):
        """int: Gets or sets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value  # Here, you might want to add validation for height

    @property
    def x(self):
        """int: Gets or sets the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value  # Here, you might want to add validation for x

    @property
    def y(self):
        """int: Gets or sets the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value  # Here, you might want to add validation for y
