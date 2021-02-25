#!/usr/bin/python3
"""Unittesting basemodel"""

import unittest
from models.base_model import BaseModel
import uuid
import json
from datetime import datetime as dt

class TestBaseModel(unittest.TestCase):
    """Unit test class form basemodel"""

    def test_attrs(self):
        """Test for specific attributes"""
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)
        self.assertIsInstance(base.created_at, dt)
        self.assertIsInstance(base.updated_at, dt)
        self.assertNotIsInstance(base.id, uuid.UUID)
        self.assertIsInstance(base.id, str)

    def test_str(self):
        """Testing str for basemodel"""
        base1 = BaseModel()
        strang = "[{}] ({}) {}".format(type(base1).__name__, base1.id, base1.__dict__)
        self.assertEqual(str(base1), strang)
    
    def test_to_dict(self):
        """Testing to dict method"""
        base2 = BaseModel()
        deect = {}
        deect['__class__'] = "BaseModel"
        deect['created_at'] = str(base2.created_at.isoformat())
        deect['updated_at'] = str(base2.updated_at.isoformat())
        deect['id'] = base2.id
        self.assertEqual(deect, base2.to_dict)

    def test_save(self):
        """Testing the save method"""
        base3 = BaseModel()
        update = base3.updated_at
        base3.save()
        new = base3.updated_at
        self.assertNotEqual(update, new)

