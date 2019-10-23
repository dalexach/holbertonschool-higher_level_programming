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

    def test_empty(self):
        """
        Test for an empty instantiation
        """
        with self.assertRaises(TypeError):
            s1 = Square()

    def test_more_arguments(self):
        """
        Test for an instantiation with 1 more argument
        """
        with self.assertRaises(TypeError):
            s1 = Square(1, 1, 1, 1, 1)

    def test_correct_inst(self):
        """ Test for a correct instantiation. """
        s1 = Square(3, 1, 2, 45)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 2)
        self.assertEqual(s1.id, 45)

    def test_str_rep(self):
        """
        Test for string representation of a square.
        """
        s1 = Square(3, 1, 2, 45)
        self.assertEqual(s1.__str__(), "[Square] (45) 1/2 - 3")

    def test_size_setter(self):
        """
        Test for size setter of square class
        """
        s1 = Square(3, 1, 2, 45)
        s1.size = 27
        self.assertEqual(s1.size, 27)

    def test_update(self):
        """
        Test for update method of square
        """
        s1 = Square(3, 1, 2, 45)
        s1.update(12, 5, 5, 8)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 8)
        self.assertEqual(s1.id, 12)
        s1.update(23)
        self.assertEqual(s1.id, 12)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 8)
        s1.update(y=4, x=12, size=8, id=6)
        self.assertEqual(s1.size, 8)
        self.assertEqual(s1.x, 12)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.id, 6)
        s1.update(x=1)
        self.assertEqual(s1.x, 1)
        s1.update(6, x=23)
        self.assertEqual(s1.id, 6)
        self.assertEqual(s1.x, 1)

    def test_to_dict(self):
        """
        Test for to dictionary function.
        """
        s1 = Square(3, 1, 2, 45)
        s1_d = s1.to_dictionary()
        self.assertDictEqual(s1_d, {'x': 1, 'size': 3, 'id': 45, 'y': 2})
