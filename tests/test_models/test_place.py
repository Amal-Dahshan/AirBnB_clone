#!/usr/bin/python3
"""Unittests for Place class"""

import unittest
from models import place
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for Place Class"""

    def test_instantiation(self):
        """check for instance """
        place1 = Place()
        self.assertIsInstance(place1, Place)


    def test_attributes(self):
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertIsInstance(Place.city_id, str)
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertIsInstance(Place.user_id, str)
        self.assertTrue(hasattr(Place, "name"))
        self.assertIsInstance(Place.name, str)
        self.assertTrue(hasattr(Place, "description"))
        self.assertIsInstance(Place.description, str)
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertIsInstance(Place.number_rooms, int)
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertIsInstance(Place.number_bathrooms, int)
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertIsInstance(Place.max_guest, int)
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertIsInstance(Place.price_by_night, int)
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertIsInstance(Place.latitude, float)
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertIsInstance(Place.longitude, float)
        self.assertTrue(hasattr(Place, "amenity_ids"))


    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(place.__doc__) > 0)

    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(Place.__doc__) > 0)

    def test_method_doc(self):
        """ check for method documentation """
        for func in dir(Place):
            self.assertTrue(len(func.__doc__) > 0)
