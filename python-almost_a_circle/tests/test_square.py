import unittest
from io import StringIO
import sys
from models.base import Base
from models.square import Square
from test_rectangle import TestRectangle


class TestSquare(TestRectangle):
    """Unit tests for the Square class."""
    
    def test_square_existence(self):
        """Test that a Rectangle with width=1 and height=2 exists and has correct attributes."""
        square = Square(1)  
        # Assuming default values for x, y, and id are acceptable
        self.assertIsNotNone(square, "square instance should not be None")
        self.assertEqual(square.size, 1, "square size should be 1")
        
    def test_square_existence2(self):
        """Test if a square object is created successfully with two parameters."""
        square = Square(1, 2)  # Assuming the first parameter is side length and the second is x
        self.assertIsNotNone(square, "Square instance should not be None")
        self.assertEqual(square.size, 1, "Incorrect side length")
        self.assertEqual(square.x, 2, "Incorrect x-coordinate")
    
    def test_square_existence_with_three_params(self):
        """Test if a square object is created successfully with three parameters."""
        square = Square(1, 2, 3)  # Assuming parameters are side length, x, and y
        self.assertIsNotNone(square, "Square instance should not be None")
        self.assertEqual(square.size, 1, "Incorrect side length")
        self.assertEqual(square.x, 2, "Incorrect x-coordinate")
        self.assertEqual(square.y, 3, "Incorrect y-coordinate")

    def test_non_integer_size(self):
        """Test that passing a non-integer width."""
        with self.assertRaises(TypeError):
            Square("1")

    def test_non_integer_x(self):
        """Test that passing a non-integer width."""
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_non_integer_y(self):
        """Test that passing a non-integer width."""
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_negative_size(self):
        """Test that passing a non-integer width."""
        with self.assertRaises(ValueError):
            Square(-1)         

    def test_negative_x(self):
        """Test that passing a non-integer width."""
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_negative_y(self):
        """Test that passing a non-integer width."""
        with self.assertRaises(ValueError):
            Square(1, 2, -3) 

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