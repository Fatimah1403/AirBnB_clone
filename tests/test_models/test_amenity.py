#!/usr/bin/python3
""" Testing for amenity class"""

import unittest
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """ Amenity class that inherits from BaseModel"""
    amn = Amenity()

    def setUp(self):
        """set up the
        test for testing amenities"""
        FileStorage._FileStorage__file_path = "test.json"
        self.amenity = Amenity()
        self.amenity.name = "pool"
        self.amenity.save()

    def test_instance_User(self):
        """ Test subclasses of BaseModel """
        self.assertIsInstance(self.amn, Amenity)

    def testpublic(self):
        """Test for public id """
        self.assertEqual(str, type(Amenity().id))

    def test_if_class_exists(self):
        """tests if class exists"""
        res = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.amn)), res)

    def test_attribute_name(self):
        """ Check attributes name """
        self.assertEqual(hasattr(self.amn, "name"), True)

    def test_atrr_type_Amenity(self):
        """test attribute type for Amenity"""
        self.assertEqual(type(self.amenity.name), str)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amn, 'name'))
        self.assertTrue(hasattr(self.amn, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))

    def test_public_state(self):
        """ Test if state is public"""
        self.assertEqual(str, type(State().id))

    def tearDown(self):
        os.remove(FileStorage._FileStorage__file_path)


if __name__ == "__main__":
    unittest.main()
