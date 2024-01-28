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
    
    def __eq__(self, other):
        return isinstance(other, BaseGeometry)
    
    def dir_self(self):
        return dir(self)