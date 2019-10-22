#!/usr/bin/python3
"""
Unit test for the Square class
"""

import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Test cases for the Sqare class
    """

    def tearDown(self):
        """
        Reset the nb_objects
        """
        Base._Base__nb_objects = 0

    def test_docstring(self):
        """
        Testing docstring
        """
        self.assertIsNotNone(Square.__doc__)

    def test_documentation(self):
        """
        Test to see if documentation is correct and created
        """
        self.assertTrue(hasattr(Square, "__init__"))
        self.assertTrue(Square.__init__.__doc__)
        self.assertTrue(hasattr(Square, "create"))
        self.assertTrue(Square.create.__doc__)
        self.assertTrue(hasattr(Square, "to_json_string"))
        self.assertTrue(Square.to_json_string.__doc__)
        self.assertTrue(hasattr(Square, "from_json_string"))
        self.assertTrue(Square.from_json_string.__doc__)
        self.assertTrue(hasattr(Square, "save_to_file"))
        self.assertTrue(Square.save_to_file.__doc__)
        self.assertTrue(hasattr(Square, "load_from_file"))
        self.assertTrue(Square.load_from_file.__doc__)
