#!/usr/bin/python3
""" Filestorage class """

import datetime
from os import path
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ class for storing and receiving data for the project """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return the dictionary __objects """
        return FileStorage.__objects

    def classes(self):
        """ Dictionary of all classes """
        classes_allowed = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review}

    def attributes(self):
        """ Attributes and their classnames"""
        attributes = {
                "BaseModel": {
                    "id": str,
                    "created_at": datetime.datetime,
                    "updated_at": datetime.datetime},
                "User": {
                    "email": str,
                    "password": str,
                    "first_name": str,
                    "last_name": str},

                "State": {
                    "name": str},

                "City": {
                    "state_id": str,
                    "name": str},

                "Amenity": {
                    "name": str},

                "Place": {
                    "city_id": str,
                    "user_id": str,
                    "name": str,
                    "description": str,
                    "number_rooms": int,
                    "number_bathrooms": int,
                    "max_guest": int,
                    "price_by_night": int,
                    "latitude": float,
                    "longitude": float,
                    "amenity_ids": list},

                "Review": {
                    "place_id": str,
                    "user_id": str,
                    "text": str}
        }
        return attributes

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        k = obj.__class__.__name__ + '-' + str(obj.id)
        FileStorage.__objects[k] = obj

    def save(self):
        """  serializes __objects to the JSON file (path: __file_path) """
        n_dictionary = {}
        for key, value in self.__objects.items():
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
        try:
            with open(FileStorage.__file_path, "r", encoding='utf-8') as f:
                json_dict = json.load(f)
                for k, v in json_dict.items():
                    base_file = FileStorage.classes[v["__class__"]](**v)
                    FileStorage.__objects[k] = base_file
        except FileNotFoundError:
            pass
