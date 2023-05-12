#!/usr/bin/python3
""" City class that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """ City class
    Attributes:
        name(str): city's name
        state_id: State.id

    """
    state_id = ""
    name = ""
