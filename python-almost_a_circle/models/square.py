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

    @classmethod
    def create(cls, **kwargs):
        """Factory method to create a new Square instance"""
        return cls(**kwargs)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """
        Override the __str__ of the Square.
        """
        return ('[Square] ({}) {}/{} - {}'
                .format(self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Rectangle instance using args and kwargs.
        Args order is id, width, height, x, y.
        """
        attrs = ['id', 'size', 'x', 'y']

        if args:
            # Update attributes based on args order
            for attr, value in zip(attrs, args):
                if hasattr(self, attr):
                    setattr(self, attr, value)
        else:
            # Update attributes based on kwargs
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

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
