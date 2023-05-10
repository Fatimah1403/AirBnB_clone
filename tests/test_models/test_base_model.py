#!/usr/bin/python3
""" BaseModel class unittest """

from datetime import datetime
import time
import os
import json
from models.base_model import BaseModel
import unittest
import uuid 
import pep8


class TestBaseModel(unittest.TestCase):
    """
    The Basemodel class Testcase

    """
    def setUp(self):
        """ set up test methods """
        print("setUp")

    def tearDown(self):
        """ tear down test methods """
        print("tearDown")

    def test_base_model_pep8_working(self):
        """ Test for pep8 style whether it's working wit base model module """
        style = pep8.StyleGuide(quit=True)
        result = style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style error (and warnings).")

    def test_base_model_pep8_working_test_base_model(self):
        """ Test for pep8 style whether it's working wit base model module """
        style = pep8.StyleGuide(quit=True)
        result = style.check_files(["tests/test_models/test_base_model.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found code style error (and warnings).")

    def test_base_model_id_is_a_string(self):
        """ Test whether the id is a string """
        base_m = BaseModel()
        self.assertIsInstance(base_m.id, str)

    def test_base_model_uuid_correct_format(self):
        """ To know whether UUID is in correct format """
        base_m = BaseModel()
        self.assertIsInstance(uuid.UUID(base_m.id), uuid.UUID)

     def test_base_model_uuid_not_correct_format(self):
        """ To know whether UUID is in correct format """
        base_m = BaseModel()
        base_m.id = 'Python Test'
        warn = "The hexadecimal string is wrong"

        with self.assertRaises(ValueError) as msg:
            uuid.UUID(base_m.id)
        self.assertEqual(warn, str(msg.exception))

    def test_base_model_no_args(self):
        """ "Base model with no arguments. """



































