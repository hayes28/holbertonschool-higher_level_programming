#!/usr/bin/python3
"""""
Unit test for max_integer([..])
"""
import unittest
max_integer = __import__('6_max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_docstrings(self):
        """
        Testing for module documentation
        """
        self.assertTrue(len(__import__('6-max_integer').__doc__) > 1)
        """
        Testing for function documentation
        """
        self.assertTrue(len(max_integer.__doc__) > 1)

    def test_valid(self):
        """
        Testing working case with positive integers
        """
        self.assertEqual(max_integer([1, 2, 3, 10, 2]), 10)
        """
        Testing working case with negative integers
        """
        self.assertEqual(max_integer([-1, -2, -3, -10, -2]), -10)
        """
        Testing floats
        """
        self.assertAlmostEqual(max_integer([1.3, 5, 9.1]), 9.1)
        """
        Testing single length list
        """
        self.assertEqual(max_integer([1]), 1)
        """
        Testing if only a string is passed
        """
        self.assertEqual(max_integer("banana"), "b")

    def test_invalid(self):
        """
        Testing if string is passed
        """
        self.assertRaises(TypeError, max_integer, "banana")
        """
        Testing if nothing passed
        """
        self.assertEqual(max_integer(), None)

if __name__ == '__main__':
    unittest.main()
