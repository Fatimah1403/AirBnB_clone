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


class TestUser_save(unittest.TestCase):
    """Unittests for testing save method of the  class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_oneuser_save(self):
        """ save only one user details"""
        us = User()
        sleep(0.08)
        first_updat_at = us.updated_at
        us.save()
        self.assertLess(first_updat_at, us.updated_at)

    def test_multipleuser_save(self):
        """save multiple users details """
        us = User()
        sleep(0.08)
        first_updat_at = us.updated_at
        us.save()
        second_updat_at = us.updated_at
        self.assertLess(first_updat_at, us.updated_at)
        sleep(0.08)
        us.save()
        self.assertLess(second_updat_at, us.updated_at)

    def test_save_arg(self):
        """Save arguments """
        us = User()
        with self.assertRaises(TypeError):
            us.save(None)

    def test_save_updated_file(self):
        """Testing save updated files """
        us = User()
        us.save()
        us_id = "User." + us.id
        with open("storage.json", "r") as f:
            self.assertIn(us_id, f.read())


class TestUser_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        us = User()
        self.assertIn("id", us.to_dict())
        self.assertIn("created_at", us.to_dict())
        self.assertIn("updated_at", us.to_dict())
        self.assertIn("__class__", us.to_dict())

    def test_to_dict_contains_added_attributes(self):
        us = User()
        us.middle_name = "Kehinde"
        us.number = 40
        self.assertEqual("Kehinde", us.middle_name)
        self.assertIn("number", us.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        us = User()
        us_dict = us.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        us = User()
        us.id = "123456"
        us.created_at = us.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(us.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        us = User()
        self.assertNotEqual(us.to_dict(), us.__dict__)

    def test_to_dict_with_arg(self):
        us = User()
        with self.assertRaises(TypeError):
            us.to_dict(None)


if __name__ == "__main__":
    unittest.main()
