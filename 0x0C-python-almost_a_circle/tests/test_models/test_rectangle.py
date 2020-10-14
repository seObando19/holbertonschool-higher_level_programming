#!/usr/bin/python3
"""Unittests for Rectangle class
"""
import unittest
import json
import inspect
import pep8
import io
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class
    Args:
        unittest (TestCase): inherited class
    """

    def test_documentation(self):
        """test class Rectangle documentation in methods and functions
        """
        self.assertTrue(len(Rectangle.__doc__) > 0)
        func = inspect.getmembers(Rectangle, predicate=inspect.ismethod)
        for name, method in func:
            self.assertTrue(len(method.__doc__) > 0)
        func2 = inspect.getmembers(Rectangle, predicate=inspect.isfunction)
        for name, method in func2:
            self.assertTrue(len(method.__doc__) > 0)

    def test_pep8_Rectangle_class(self):
        """Test that we conform to PEP8 for rectangle class"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors")

    def test_pep8_test_rectangle(self):
        """Test that we conform to PEP8 in test for rectangle class"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0)