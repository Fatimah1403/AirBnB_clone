#!/usr/bin/python3
"""Test State class """

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.state import State
import os


class TestState(unittest.TestCase):
    """ Testing the state class"""

    def setUp(self):
        """ Set up method """
        FileStorage._FileStorage__file_path = "test.json"
        self.state = State()
        self.state.name = "New York"
        self.state.save()

    def test_name_is_string(self):
        """ Testing if name is a string"""
        self.assertTrue(type(self.state.name), is str)

    def test_docstring_state(self):
        """ test for docstrings """
        self.assertIsNotNone(State.__doc__)

    def test_to_dict_state(self):
        """ Test if state to dicionary work"""
        self.assertEqual('to_dict' in dir(self.state), True)

    def test_public_state(self):
        """ Test if state is public"""
        self.assertEqual(str, type(State().id))

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))

    def tearDown(self):
        os.remove(FileStorage._FileStorage__file_path)


if __name__ == "__main__":
    unittest.main()
