#!/usr/bin/python3
""" Test for place class"""

import unittest
from models.place import Place
import os
import models.base_modelimport BaseModel
from models.engine.file_storage import FileStorage


class TestPlace(uniitest.TestCase):
    """class testing the place class model """

    def setUp(self):
        """ set up class method """
        FileStorage._FileStorage__file_path = "test.json"
        self.place = Place()
        self.place.city_id = "234"
        self.place.user_id = "234"
        self.place.name_id = "Fatimah"
        self.place.description = "Fine"
        self.place.number_rooms = 10
        self.place.max_guest = 7
        self.place.price_by_night = 500
        self.place.latitude = 55.0
        self.place.longitude = 54.0
        self.place.amenity_ids = ["perfect"]

    def test_attribute_place(self):
        """Test te attributes of place class """
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)

    def test_place_inherit_basemodel(self):
        """ check whether place class inherits from BaseModel"""
        self.assertIsInstance(self.place, Place)

    def testpublic(self):
        """ Test for public id """
        self.assertEqual(str, type(Place().id))


if __name__ == "__main__":
    unittest.main()
