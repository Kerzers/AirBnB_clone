#!/usr/bin/python3
"""module: test_city"""
import unittest
import os
import models
from datetime import datetime
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Tests the class: City"""

    def test_init(self):
        self.assertIsInstance(City(), BaseModel)

    def test_init_id(self):
        """ tests the init method with id"""
        s1 = City()
        s2 = City(1)
        self.assertIsInstance(s2, City)
        self.assertTrue(hasattr(s1, "id"))
        self.assertNotEqual(s1.id, s2.id)
        self.assertIsInstance(s1.id, str)

    def test_init_attributes(self):
        """ tests the init method with created_at/updated_at attribute"""
        s1 = City()
        s2 = City()
        self.assertTrue(hasattr(s1, "name"))
        self.assertIsInstance(s1.created_at, datetime)
        self.assertIsInstance(s1.updated_at, datetime)
        self.assertIsInstance(s1.name, str)
        self.assertNotEqual(s1.created_at, s2.created_at)
        self.assertNotEqual(s1.updated_at, s2.updated_at)

    def test_init_kwargs(self):
        a_dict = {
                'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                'created_at': '2017-09-28T21:03:54.052298',
                '__class__': 'City',
                'my_number': 89,
                'updated_at': '2017-09-28T21:03:54.052302',
                }
        s = City(**a_dict)
        self.assertNotIn("__class__", s.__dict__)
        self.assertDictEqual(a_dict, s.to_dict())
        self.assertIsInstance(s.created_at, datetime)
        self.assertIsInstance(s.updated_at, datetime)

    def test_init_kwargs_empty(self):
        "test_init_kwargs_ tests kwargs if working correctrly if empty"
        self.assertIn(City(), models.storage.all().values())

    def test_to_dict(self):
        "test_to_dict_type tests if working correctrly"
        s = City()
        json_s = s.to_dict()

        self.assertIsInstance(json_s, dict)
        for k in json_s.keys():
            self.assertIsInstance(json_s[k], str)

    def test_to_dict_difference(self):
        "test_to_dict_difference tests if working correctrly"
        s = City()
        self.assertNotEqual(s.__dict__, s.to_dict())

    def test_to_dict_attributes(self):
        "test_to_dict_attributes tests if working correctrly"
        s = City()
        self.assertIn("__class__", s.to_dict())
        s.name = "Miami"
        self.assertIn("name", s.to_dict())

    def test_to_dict_args(self):
        "test_to_dict_args tests if working correctrly"
        s = City()
        with self.assertRaises(TypeError):
            s.to_dict(None)

    def test_save(self):
        "test_save tests if working correctrly"
        s = City()
        s.save()
        self.assertNotEqual(s.created_at, s.updated_at)
