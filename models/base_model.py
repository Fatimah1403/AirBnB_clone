#!/usr/bin/python3
"""
    Module for class BaseModel
"""

import uuid
from uuid import uuid4
from datetime import datetime
import models
from models import FileStorage


class BaseModel:

    """
    All other classes will inherit this
    """

    def __init__(self, *args, **kwargs):

        """
        Initializing instance attributes
        *args: varying number of arguments
        **kwargs: key-values arguments; dictionary
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Instance of a class represented as a string
        Returns a string with the format
        [<class name>] (<id>) <instance attributes>.
        """

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime
        Calls the save() method of the storage module to save the instance
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns the new_dict dictionary containing all
        the keys and values of the instance as well as
        the __class__, created_at, and updated_at keys
        This dictionary will be used to serialize
        the instance into a JSON representation
        """

        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
