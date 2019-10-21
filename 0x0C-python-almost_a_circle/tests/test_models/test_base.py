#!/usr/bin/python3
"""
Unit test for the Base class
"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """
    Test cases for the Base class
    """
    def test_docstring(self):
        """
        Testing docstring
        """
        self.assertIsNotNone(Base.__doc__)

    def test_documentation(self):
        """
        Test to see if documentation is correct and created
        """
        self.assertTrue(hasattr(Base, "__init__"))
        self.assertTrue(Base.__init__.__doc__)
        self.assertTrue(hasattr(Base, "create"))
        self.assertTrue(Base.create.__doc__)
        self.assertTrue(hasattr(Base, "to_json_string"))
        self.assertTrue(Base.to_json_string.__doc__)
        self.assertTrue(hasattr(Base, "from_json_string"))
        self.assertTrue(Base.from_json_string.__doc__)
        self.assertTrue(hasattr(Base, "save_to_file"))
        self.assertTrue(Base.save_to_file.__doc__)
        self.assertTrue(hasattr(Base, "load_from_file"))
        self.assertTrue(Base.load_from_file.__doc__)

    def test_base_creation(self):
        """
        Testing the creation of the base
        """
        b = Base()
        test = str(b)
        b1 = Base(12)
        b2 = Base()
        self.assertTrue(test[:29], '<models.base.Base object at ')
        self.assertTrue(b.id, 1)
        self.assertTrue(b1.id, 12)
        self.assertTrue(b2.id, 2)

    def test_base_class_id(self):
        """
        Testing the increment of the nb_objects
        """
        b = Base()
        test = b.id
        b1 = Base()
        b2 = Base(id=33)
        self.assertTrue(test + 1, b1)
        self.assertTrue(b2.id, 33)
