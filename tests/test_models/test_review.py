#!/usr/bin/python3
""" unit testing file for reviews"""


import unittest
from models.base_model import BaseModel
from models.review import Review
import uuid
import json
from datetime import datetime as dt


class TestReview(unittest.TestCase):
    """class for testing reviews"""

    def test_attrs(self):
        """Basic test for attributes"""
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertEqual(review.created_at, dt)
        self.assertIsInstance(review.updated_at, dt)
        self.assertNotIsInstance(review.id, uuid.UUID)
        self.assertIsInstance(review.id, str)

    def test_state_attrs(self):
        """Testing for attributes"""
        review1 = Review()
        self.assertIsInstance(review1.place_id, str)
        self.assertIsInstance(review1.user_id, str)
        self.assertIsInstance(review1.text, str)
