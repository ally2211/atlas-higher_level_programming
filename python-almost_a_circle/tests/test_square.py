import unittest
from io import StringIO
import sys
import os
import json
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

    def test_square_zero(self):
        """Test that passing zero size."""
        with self.assertRaises(ValueError):
            Square(0) 

    def test_str_method(self):
        """Test the string representation of a Rectangle instance."""
        square = Square(2, 1, 1, 123)  # Create a Square instance
        expected_str = '[Square] (123) 1/1 - 2'
        self.assertEqual(square.__str__(), expected_str)
        
    def test_update_method(self):
        """Test the update method of the Square class."""
        square = Square(5)
        square.update(size=10, x=2, y=3)

        self.assertEqual(square.size, 10, "The side should be updated to 10")
        self.assertEqual(square.x, 2, "The x- should be updated to 2")
        self.assertEqual(square.y, 3, "The y- should be updated to 3")

    def test_create_method_with_multiple_kwargs(self):
        """Test the create method with multiple keyword arguments."""
        # Create a Square instance using the create method with kwargs
        square = Square.create(**{'id': 89, 'size': 1, 'x': 3})

        # Check if the properties are set correctly
        self.assertEqual(square.id, 89, "The id should be set to 89")
        self.assertEqual(square.size, 1, "The width should be set to 1")
        self.assertEqual(square.x, 3, "The x position should be set to 3")

    def test_create_method_with_full_kwargs(self):
        """Test the create method with a full set of keyword arguments."""
        # Create a Rectangle instance using the create method with kwargs
        square = Square.create(**{'id': 89, 'size': 1, 'x': 3, 'y': 4})

        # Check if the properties are set correctly
        self.assertEqual(square.id, 89, "The id should be set to 89")
        self.assertEqual(square.size, 1, "The size should be set to 1")
        self.assertEqual(square.x, 3, "The x position should be set to 3")
        self.assertEqual(square.y, 4, "The y position should be set to 4")

    def test_to_dictionary_exists(self):
        """Test that the to_dictionary method exists in Square."""
        square = Square(2, 1, 1, 123)
        self.assertTrue(hasattr(square, 'to_dictionary'), "to_dictionary method does not exist")

    def test_save_to_file_with_none(self):
        """Test save_to_file method with None as argument raises ValueError."""
        with self.assertRaises(ValueError):
            Square.save_to_file(None)

    def test_save_to_file_with_empty(self):
        """Test save_to_file method with None as argument raises ValueError."""
        with self.assertRaises(ValueError):
            Square.save_to_file([])

    def test_save_to_file_single_rectangle(self):
        """Test save_to_file with a single Rectangle instance."""
        square = Square(1, 2)
        Square.save_to_file([square])
        filename = f"{Square.__name__}.json"
        self.assertTrue(os.path.exists(filename))

        with open(filename, 'r') as file:
            contents = file.read()
            data = json.loads(contents)
            expected = [square.to_dictionary()]
            self.assertEqual(data, expected)

        # Clean up: Remove the file after test
        if os.path.exists(filename):
            os.remove(filename)

    def test_load_from_file_no_file(self):
        """Test load_from_file raises an error when the file does not exist."""
        # Ensure the file does not exist
        filename = f"{Square.__name__}.json"
        if os.path.exists(filename):
            os.remove(filename)

        result = Square.load_from_file()
        self.assertEqual(result, [])

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