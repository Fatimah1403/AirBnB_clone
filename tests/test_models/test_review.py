#!/usr/bin/python3
""" Review test class"""

import unittest
import os
from models.base_model import BaseModel
from models.review import review
from moedels.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """ Review class that inherits from BaseModel """

