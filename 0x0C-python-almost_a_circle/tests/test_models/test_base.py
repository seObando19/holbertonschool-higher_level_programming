#!/usr/bin/python3
"""
Unit testing for Base class
"""


import inspect
import json
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """
        Test cases for Base class
        Args:
            unittest (TestCase): inherited class
    """

        def test_AA_documentation(self):
        """test class Base documentation in methods and functions
        """
        self.assertTrue(len(Base.__doc__) > 0)
        func = inspect.getmembers(Base, predicate=inspect.ismethod)
        for name, method in func:
            self.assertTrue(len(method.__doc__) > 0)
        func2 = inspect.getmembers(Base, predicate=inspect.isfunction)
        for name, method in func2:
            self.assertTrue(len(method.__doc__) > 0)

    def test_pep8_Base_class(self):
        """Test that we conform to PEP8 for base class"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors")

    def test_pep8_test_base(self):
        """Test that we conform to PEP8 in test for base class"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors")