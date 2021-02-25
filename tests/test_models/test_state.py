#!/usr/bin/python3
""" Unit testing for states"""


import unittest
from models.base_model import BaseModel
from models.state import State
import uuid
import json
from datetime import datetime as dt


class Test_States(unittest.TestCase):
    """class for states unittest"""

    def test_attrs(self):
        """Testing attributes"""
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertIsInstance(state.created_at, dt)
        self.assertIsInstance(state.updated_at, dt)
        self.assertIsInstance(state.id, str)

    def test_spef(self):
        """State only attributes"""
        state1 = State()
        self.assertIsInstance(state1, State)
