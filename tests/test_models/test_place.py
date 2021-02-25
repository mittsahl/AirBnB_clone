#!/usr/bin/python3
"""Unit testing file for places"""


import unittest
from models.base_model import BaseModel
from models.place import Place
import uuid
import json
from datetime import datetime as dt


class TestPlace(unittest.TestCase):
    """class for unit testing Places"""

    def test_attrs(self):
        """Basic test for attributes"""
        cidy1 = Place()
        self.assertIsInstance(cidy1, BaseModel)
        self.assertIsInstance(cidy1.created_at, dt)
        self.assertIsInstance(cidy1.updated_at, dt)
        self.assertNotIsInstance(cidy1.id, uuid.UUID)

