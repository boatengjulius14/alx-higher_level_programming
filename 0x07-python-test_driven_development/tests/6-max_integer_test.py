#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Definition of class TestMaxInteger, subclass
    of unittest.TestCase"""

    def test_max_digits(self):
        """Tests both positive and negative int and float
        values
        """
        self.assertEqual(max_integer([4, 99, 58, 99, 2]), 99)
        self.assertEqual(max_integer([2.89, -10.3, -58, 2.9]), 2.9)
        self.assertEqual(max_integer([10]), 10)
        self.assertEqual(max_integer([]), None)

    def test_raises(self):
        """test error classes raised"""
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, 'Hello', 8, 1000)

    def test_strings(self):
        """test strings"""
        self.assertEqual(max_integer(["You", "yam", "Yoghurt"]), 'yam')
        self.assertEqual(max_integer("Julius""v"), 'v')
        self.assertEqual(max_integer(""), None)
