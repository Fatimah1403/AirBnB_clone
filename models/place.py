#!/usr/bin/env python3
""" module for the Place class """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class inheriting from BaseModel

        Attributes:
            city_id (str): public class attribute for the city unique id
            user_id (str): public class attribute for user unique id
            name (str): name of Place
            description (str): description of the place
            number_rooms (int): public class attribute for the rooms number
            number_bathrooms (int): number of the bathroom
            max_guest (int): maximum number of guests
            price_by_night (int): Price of the place during night hours
            latitude (float): gives the latitude co-ordinate of the place
            longitude (float): longitude of the place
            amenity_ids (str): holds the id of a list of amenity in the place

    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
