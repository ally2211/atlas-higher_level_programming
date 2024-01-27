import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Unit tests for the Rectangle class."""

    def test_rectangle_existence(self):
        """Test that a Rectangle with width=1 and height=2 exists and has correct attributes."""
        rect = Rectangle(1, 2)  
        # Assuming default values for x, y, and id are acceptable
        self.assertIsNotNone(rect, "Rectangle instance should not be None")
        self.assertEqual(rect.width, 1, "Rectangle width should be 1")
        self.assertEqual(rect.height, 2, "Rectangle height should be 2")

    def test_non_integer_width(self):
        """Test that passing a non-integer width."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_non_integer_height(self):
        """Test that passing a non-integer height."""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_rectangle_creation(self):
        """Test creating a rectangle and accessing its attributes."""
        r = Rectangle(10, 5, 2, 3, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 1)

    def test_rectangle_setters(self):
        """Test the property setters for width, height, x, and y."""
        r = Rectangle(10, 5)
        r.width = 15
        r.height = 10
        r.x = 5
        r.y = 5
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 5)


if __name__ == '__main__':
    unittest.main()
