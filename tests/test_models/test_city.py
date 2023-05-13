#!/usr/bin/python3
""" Test for City class """

import unittest
import os
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
    """ City class that inherits from BaseModel """

    def setUp(self):
        """ set up method"""
        FileStorage._FileStorage__file_path = "test.json"
        self.city = City()
        self.city.name = "Selden"
        self.city.save()

    def tearDown(self):
        """Tear down method """
        pass

    def test_city_is_string(self):
        """ Test city is a string"""
        self.assertTrue(type(self.id) is str)
        self.assertTrue(type(self.city) is str)

    def tet_attributes_city():
        """ Test city attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertEqual(hasattr(self.city, "name"), True)

    def test_other_attributes(self):
        """Check other existing attributes """
        self.assertEqual(hasattr(self.city, "name"), True)
        self.assertEqual(hasattr(self.city, "state_id"), True)

    def test_document_city(self):
        """ checking docstring"""
        self.assertIsNotNone(City.__doc__)

    def test_public(self):
        """ Test public attributes"""
        self.assertEqual(str, type(City().id))

    def test_save_City(self):
        """test if the save works"""
        self.assertNotEqual(self.city.created_at, self.city.updated_at)
        self.city.save()


if __name__ == "__main__":
    unittest.main()
