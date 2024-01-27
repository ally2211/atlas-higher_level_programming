import unittest
from io import StringIO
import sys
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
            
    def test_non_integer_x(self):
        """Test that passing a non-integer x."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, x="3", y=4)
            
    def test_non_integer_y(self):
        """Test that passing a non-integer y."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, x=3, y="4")
    
    def test_invalid_init_width(self):
        """Test that initializing with invalid x."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2, x=1, y=0)

    def test_invalid_init_height(self):
        """Test that initializing with invalid x."""
        with self.assertRaises(ValueError):
            Rectangle(1, -2, x=1, y=0)
            
    def test_invalid_init_widthzero(self):
        """Test that initializing with invalid x."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_invalid_init_heightzero(self):
        """Test that initializing with invalid x."""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_invalid_init_x(self):
        """Test that initializing with invalid x."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, x=-1, y=0)

    def test_invalid_init_y(self):
        """Test that initializing with invalid y."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, x=0, y=-1)

    def test_invalid_set_x(self):
        """Test that setting x to an invalid value."""
        rect = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            rect.x = -1

    def test_invalid_set_y(self):
        """Test that setting y to an invalid value."""
        rect = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            rect.y = -1
    
    def test_area_calculation(self):
        """Test the area calculation of the rectangle."""
        rect = Rectangle(10, 5)
        self.assertEqual(rect.area(), 50)

    def test_str_method(self):
        """Test the string representation of a Rectangle instance."""
        rect = Rectangle(3, 2, 1, 1, 123)  # Create a Rectangle instance
        expected_str = '[Rectangle] (123) 1/1 - 3/2'
        self.assertEqual(rect.__str__(), expected_str)
    
    def test_to_dictionary_exists(self):
        """Test that the to_dictionary method exists."""
        rect = Rectangle(10, 5, 2, 3, 1)
        self.assertTrue(hasattr(rect, 'to_dictionary'),
                        "to_dictionary does not exist")
  
    def test_save_to_file_with_none(self):
        """Test save_to_file method with None as argument raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle.save_to_file(None)

    def test_save_to_file_with_empty(self):
        """Test save_to_file method with None as argument raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle.save_to_file([])
        
    def test_update_method(self):
        """Test the update method of the Rectangle class."""
        rectangle = Rectangle(5, 5)
        rectangle.update(width=10, height=2, x=2, y=3)

        self.assertEqual(rectangle.width, 10, "The width updated to 10")
        self.assertEqual(rectangle.height, 2, "The height updated to 2")
        self.assertEqual(rectangle.x, 2, "The x should be updated to 2")
        self.assertEqual(rectangle.y, 3, "The y should be updated to 3")

    def test_create_method_with_multiple_kwargs(self):
        """Test the create method with multiple keyword arguments."""
        # Create a Rectangle instance using the create method with kwargs
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})

        # Check if the properties are set correctly
        self.assertEqual(rect.id, 89, "The id should be set to 89")
        self.assertEqual(rect.width, 1, "The width should be set to 1")
        self.assertEqual(rect.height, 2, "The height should be set to 2")
        self.assertEqual(rect.x, 3, "The x position should be set to 3")

    def test_create_method_with_full_kwargs(self):
        """Test the create method with a full set of keyword arguments."""
        # Create a Rectangle instance using the create method with kwargs
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})

        # Check if the properties are set correctly
        self.assertEqual(rect.id, 89, "The id should be set to 89")
        self.assertEqual(rect.width, 1, "The width should be set to 1")
        self.assertEqual(rect.height, 2, "The height should be set to 2")
        self.assertEqual(rect.x, 3, "The x position should be set to 3")
        self.assertEqual(rect.y, 4, "The y position should be set to 4")

    def setUp(self):
        """Redirect stdout to capture print statements."""
        self.capturedOutput = StringIO()
        sys.stdout = self.capturedOutput

    def tearDown(self):
        """Reset stdout to default."""
        sys.stdout = sys.__stdout__

    def test_display_method(self):
        """Test the visual output of the display method with x and y offsets."""
        rect = Rectangle(3, 2, 1, 2)  # width=3, height=2, x=1, y=2
        expected_output = "\n\n ###\n ###\n"  # Considering the newline and space offsets

        rect.display()
        self.assertEqual(self.capturedOutput.getvalue(), expected_output)

    def test_display_method_no_offset(self):
        """Test the visual output of the display method without x and y offsets."""
        width, height = 3, 2
        rect = Rectangle(width, height)  # No x and y offsets provided
        expected_output = ("#" * width + "\n") * height

        rect.display()
        self.assertEqual(self.capturedOutput.getvalue(), expected_output)

    def test_display_method_no_y_offset(self):
        """Test the visual output of the display method without x and y offsets."""
        width, height, x = 3, 2, 2
        rect = Rectangle(width, height, x)
        expected_output = (" " * x + "#" * width + "\n") * height

        rect.display()
        self.assertEqual(self.capturedOutput.getvalue(), expected_output)

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
