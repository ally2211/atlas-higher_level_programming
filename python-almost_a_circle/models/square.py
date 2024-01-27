#!/usr/bin/python3
"""
Module Doc: Square Class
"""
# Rectangle class is defined in models/rectangle.py
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle class.
    Represents a square with a size, and optional x, y coordinates, and id.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Override the __str__ of the Square.
        """
        return ('[Square] ({}) {}/{} - {}'
                .format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """int: Gets or sets the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
