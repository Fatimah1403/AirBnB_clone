#!/usr/bin/python3
"""A User class that inherits from BaseModel """

from models.base_model import BaseModel


class User(BaseModel):
    """ User Class
    Attributes:
        email:(str) - the user email
        password:(str) - the  user password.
        first_name:(str) - the first name of the user
        last_name:(str) - the last name of the user
    """
    emai = ""
    password = ""
    first_name = ""
    last_name = ""
