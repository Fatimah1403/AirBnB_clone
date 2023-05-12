#!/usr/bin/python3
""" BaseModel class unittest """

from datetime import datetime
import time
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
import uuid
import pep8
from models import storage


class TestBaseModel(unittest.TestCase):
    """
    The Basemodel class Testcase

    """
    def setUp(self):
        """ set up test methods """
        FileStorage._FileStorage__file_path = "file.json"

    def tearDown(self):
        """ tear down test methods """
        self.adjStorage()

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

    def test_base_model_instantiation(self):
        """ "Base model test for instantiation. """
        base_m = BaseModel()
        self.assertEqual(str(type(base_m)), \
                         "<class 'models.base_model.BaseModel'>")
        self.assertTrue(issubclass(type(base_m), BaseModel))
        self.assertIsInstance(base_m, BaseModel)

    def test_base_model_datetime_created(self):
        """ Test for the basemodel created datetime status """
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_base_model_datetime_updated(self):
        """ Test for the basemodel updated datetime status """
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_all_storage_obj(self):
        """ Test for storage objects """
        self.assertIn(BaseMode(), models.storage.all().values)

    def test_all_str(self):
        """ Test for all strings"""
        date_time = datetime.today()
        date_repr = repr(date_time)
        base_m = BaseModel()
        base_m.id = "1234567"
        base_m.created_at = base_m.updated_at = date_time
        base_m_str = base_m.__str__()
        self.asserIn("[BaseModel] (1234567)", base_m_str)
        self.assertIn("'id': '1234567'", base_m_str)
        self.assertIn("'created_at': " + date_repr, base_m_str)
        self.assertIn("'updated_at': " + date_repr, base_m_str)

    def test_two_models(self):
        """ Test two models which are not equal"""
        base_m1 = BaseModel()
        base_m2 = BaseModel()
        self.assertNotEqual(base_m1.id, base_m2)

    def test_none_kwargs(self):
        """ Test wen kwargs are none"""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_kwargs(self):
        """ Test while kwargs are present"""
        date_time = datetime.today()
        date_iso = date_time.isoformat()
        base_m = BaseModel(id="234", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(base_m.id, "234")
        self.assertEqual(base_m.created_at, date_time)
        self.assertEqual(base_m.updated_at, date_time)


class Test_save(unittest.TestCase):

    @classmethod
    def setUp(self):
        """set up method """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """ Tear down method"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def testsave(self):
        """ save method testing """
        base_m = BaseModel()
        Update_at = base_m.updated_at
        base_m.save()
        self.assertLess(Update_at, base_m.updated_at)

    def testsave_arg(self):
        """ saving arguments tested """
        base_m = BaseModel()
        with self.assertRaises(TypeError):
            base_m.save(None)

    def testsave_update(self):
        """saving updates """
        base_m = BaseModel()
        base_m.save()
        base_m_id = "BaseModel." + base_m.id
        with open("file.json", "r") as f:
            self.assertIn(base_m_id, f.read())


class Test_to_dict(unittest.TestCase):
    """ Testing the dict method"""

    def testto_dict(self):
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123"
        bm.created_at = bm.updated_at = dt
        todict = {
            "id": "123",
            "created_at": dt.isoformat(),
            "updated_at": dt.isoformat(),
            "__class__": "BaseModel"
        }
        self.assertDictEqual(bm.to_dict(), todict)

    def testtype(self):
        """checking the type of dictionary converted """
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def testto_dict_arg(self):
        """dictionary with arguments checking """
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)

    def testto_dict_arg1(self):
        """checking the arhuments of dict are not equal """
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def testto_dict_created_at(self):
        """ Test dict at created_at time """
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))

    def testto_dict_updated_at(self):
        """ Test dict at updated_at time"""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def testattr(self):
        """ Test BaseModel attributes"""
        bm = BaseModel()
        bm_name = 'Fatimah'
        bm_num = 90
        self.assertNotIn('name', bm.to_dict())
        self.assertNotIn('my_number', bm.to_dict())

    def testmuldict(self):
        """Testing for multiple attributes """
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


if __name__ == '__main__':
    unittest.main()
