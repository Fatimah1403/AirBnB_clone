#!/usr/bin/python3
""" Test user class """

import unittest
from time import sleep
from datetime import datetime
import models
from models.user import User
import os


class Testuser(unittest.TestCase):
    """ Testing the User class """

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_no_args_instantiated(self):
        self.assertEqual(User, type(User()))

    def test_id_is_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_str(self):
        self.assertEqual(str, type(User().email))

    def test_password_str(self):
        self.assertEqual(str, type(User().password))

    def test_first_name_is_str(self):
        self.assertEqual(str, type(User().first_name))

    def test_last_name_is_str(self):
        self.assertEqual(str, type(User().last_name))

    def test_three_users_unique_id(self):
        """Test user unique id """
        us1 = User()
        us2 = User()
        us3 = User()
        self.assertNotEqual(us1.id, us2.id, us3.id)

    def test_two_users_different_created_at(self):
        """Test two users created at different time """
        us1 = User()
        sleep(0.08)
        us2 = User()
        self.assertLess(us1.created_at, us2.created_at)

    def test_two_users_different_updated_at(self):
        """Test two users updated at different time """
        us1 = User()
        sleep(0.08)
        us2 = User()
        self.assertLess(us1.updated_at, us2.updated_at)

    def test_string_rep(self):
        """ test string reprisentation"""
        us = User()
        us.id = "12345"
        dt = datetime.today()
        dt_repr = repr(dt)
        us.created_at = us.updated_at = dt
        us_str = us.__str__()
        self.assertIn("'id': '12345'", us_str)
        self.assertIn("[User] (12345)", us_str)
        self.assertIn("'created_at': " + dt_repr, us_str)
        self.assertIn("'updated_at': " + dt_repr, us_str)

    def test_instant_with_kwargs(self):
        """ Test instantiation with kwargs"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        us = User(id="234", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(us.id, "243")
        self.assertEqual(us.created_at, dt)
        self.assertEqual(us.updated_at, dt)

    def test_unused_args(self):
        """Test for unused arguments """
        us = User(None)
        us_dict_val = us.__dict__.values()
        self.assertNotIn(None, us_dict_val)



































if __name__ == "__main__":
    unittest.main()
