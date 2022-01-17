#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    testing max integer
    """

    def test_empty(self):
        """test if empty list"""
        self.assertEqual(max_integer([]), None)

    def test_negatives(self):
        """checks negative numbers"""
        self.assertEqual(max_integer([-7, -8, -9]), -6)

    def test_type(self):
        """makes sure input is a list"""
        self.assertIs(list, list)

    def test_invalid(self):
        self.assertRaises(TypeError, max_integer((11, 13)))

    def test_module_docstring(self):
        """Tests for module docsting"""
        modstring = __import__('6-max_integer').__doc__
        self.assertTrue(len(modstring) > 1)

    def test_function_docstring(self):
        """Tests for function docstring"""
        funcstring = max_integer.__doc__
        self.assertTrue(len(funcstring) > 1)

if __name__ == "__main__":
    unittest.main()
