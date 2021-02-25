#!/usr/bin/python3
"""Unittest testing file for States"""


import unittest
from models.base_model import BaseModel
from models.city import City
import uuid
import json
from datetime import datetime as dt

class TestCity(unittest.TestCase):
    """Class for unittesting"""

    def test_attrs(self):
        """Test for attributes"""
        obj = City()
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj.created_at, dt)
        self.assertIsInstance(obj.updated_at, dt)
        self.assertNotIsInstance(obj.id, uuid.UUID)
        self.assertIsInstance(obj.id, str)
    
    def test_state(self):
        """Test state specific attributes"""
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_serialization(self):
        """Testing for serialization"""
        city1 = City()
