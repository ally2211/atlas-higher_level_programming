import unittest
from io import StringIO
import sys
from models.base import Base
from models.square import Square

class TestSquare(unittest.TestCase):
    """Unit tests for the Square class."""
        
    def test_square_creation(self):
        """Test creating a rectangle and accessing its attributes."""
        r = Square(10, 2, 3, 1)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 1)

    def test_square_setters(self):
        """Test the property setters for width, height, x, and y."""
        r = Square(10)
        r.width = 10
        r.height = 10
        r.x = 5
        r.y = 5
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 5)


if __name__ == '__main__':
    unittest.main()