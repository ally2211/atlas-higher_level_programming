#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_end(self):
        """Test when max integer is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_beginning(self):
        """Test when max integer is at the beginning"""
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)

    def test_max_middle(self):
        """Test when max integer is in the middle"""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one_element(self):
        """Test with only one element in the list"""
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with all negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test with a mix of positive and negative numbers"""
        self.assertEqual(max_integer([-1, 4, -3, 2]), 4)

    def test_all_same_number(self):
        """Test with all elements being the same number"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    # Add more tests if needed

if __name__ == '__main__':
    unittest.main()
