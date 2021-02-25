#!/usr/bin/python3
"""unit test for ammenities"""

import unittest 
from models.base_model import BaseModel
from models.amenity import Amenity
import uuid
import json
from datetime import datetime as dt


class TestAmenity(unittest.TestCase):
    """Unit test class for ammenity"""

    def test_basic(self):
        """Test for attributes"""
        u = Amenity()
        self.assertIsInstance(u, BaseModel)
        self.assertIsInstance(u.created_at, dt)
        self.assertIsInstance(u.updated_at, dt)
        self.assertNotIsInstance(u.id, uuid.UUID)
        self.assertIsInstance(u.id, str)

    def test_specific(self):
        """ Test for state attributes"""
        s = Amenity()
        self.assertIsInstance(s.name, str)
