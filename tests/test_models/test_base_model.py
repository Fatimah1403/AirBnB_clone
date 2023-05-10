#!/usr/bin/python3
""" BaseModel class unittest """

from datetime import datetime
import time
import os
import json
from models.base_model import BaseModel
import unittest
import uuid


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
