#!/usr/bin/python3
"""
class doc:  determine if same object
"""

class BaseGeometry:
    def __init__(self):
        pass
    
    def __str__(self):
        return "This is a BaseGeometry object."

    def __eq__(self, other):
        return isinstance(other, BaseGeometry)
    
    def dir_self(self):
        return dir(self)