#!/usr/bin/python3
""" Amenity class that inherits from BaseModel"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """ Amenity class
    Attributes:
        name(str): amenity's name

    """
    name = ""
