#!/usr/bin/python3
"""
class doc:  determine if same object
"""


class BaseGeometry:
    """
    Class doc:  Empty BaseGeometry class
    """
    def __init__(self):
        pass

    def area(self):
        """
        area: method to calculate area
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        integer_validator: method to validate integers
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
