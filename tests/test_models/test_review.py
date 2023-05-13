#!/usr/bin/python3
""" Review test class"""

import unittest
import os
from models.base_model import BaseModel
from models.review import review
from moedels.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """ Review class that inherits from BaseModel """
    r = Review()

    def setUp(self):
        """Set up method """
        FileStorage._FileStorage__file_path = "test.json"
        self.rev = Review()
        self.rev.place_id = "456"
        self.rev.user_id = "345"
        self.rev.text = "456"
        self.rev.save()

    def test_attribute_type(self):
        """ check the attributes types"""
        self.assertEqual(type(self.r.place_id), str)
        self.assertEqual(type(self.r.user_id), str)
        self.assertEqual(type(self.r.text_id), str)

    def test_attribute_if_true(self):
        """Tests attribute whether they are true """
        self.assertEqual(hasattr(self.r, "place_id"), True)
        self.assertEqual(hasattr(self.r, "user_id"), True)
        self.assertEqual(hasattr(self.r, "text_id"), True)

    def test_docs_Review(self):
        """ Test the docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def test_subclass_review(self):
        """ Test whether review is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)
        self.assertIsinstance(self.rev, Review)

    def test_public(self):
        """Test for public id """
        self.assertEqual(str, type(Review().id))


if __name__ == "__main__":
    unittest.main()
