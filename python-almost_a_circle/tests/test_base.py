#!/usr/bin/python3
# test_base.py
import unittest
from base import Base


class TestBase(unittest.TestCase):
    
    def test_id_assigned_explicitly(self):
        """Test if the id is assigned correctly when explicitly provided."""
        obj = Base(5)
        self.assertEqual(obj.id, 5)
        
    def test_id_auto_increment(self):
        """Test if the id auto-increments correctly when not provided."""
        Base._Base__nb_objects = 0  # Resetting for consistent testing
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        
    def test_id_none(self):
        """Test if the id increments correctly starting from 1 when id is None."""
        Base._Base__nb_objects = 0  # Resetting for consistent testing
        obj = Base(None)
        self.assertEqual(obj.id, 1)
        
if __name__ == '__main__':
    unittest.main()
