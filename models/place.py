#!/usr/bin/python3
"""module for Place class"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that inherits from BaseModel class
    Attributes:
        city_id (str): city id
        user_id (str): user id
        name (str): the name of the place
        description (str): a brief description of the place
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): maxImum number of guests
        price_by_night (int): the price for a night
        latitude (float): latitude of the place
        longitude (float): longitude of the place
        amenity_ids (list): list of amenity ids
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
