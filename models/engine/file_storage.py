#!/usr/bin/python3
""" Filestorage class """

import datetime
import os
import json


class FileStorage:
    """ class for storing and receiving data for the project """

    def all(self):
        """ return the dictionary __objects """
        return Filestorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        k = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[k] = obj

    def save(self):
        """  serializes __objects to the JSON file (path: __file_path) """
        n_dictionary = {}
        for key, value in FileStorage.__objects.items():
            n_dictionary[key] = value.to_dict()
            """ open file in write mode,
            if the file does not exist, it's created
            """
            with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
                json.dump(n_dictionary, f)

    def reload(self):
        """ deserializes the JSON file to __objects (only if
        the JSON file (__file_path) exists ; otherwise,
        do nothing. If the file doesn’t exist, no exception should be raised)
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as f:
                json_dict = json.loads(f.read())
                for k, v in json_dict.items():
                    self.__objects[k] = eval(v['__class__'])(**v)
