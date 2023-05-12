#!/usr/bin/env python3
""" module for review class """


from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class inheriting from BaseModel

        Attributes:
            place_id (str): public class attribute to hold the
            unique id of Place class instance
            user_id (str): id of the User class instance
            text: (str): review text
    """
    place_id = ""
    user_id = ""
    text = ""
