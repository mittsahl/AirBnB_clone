#!/usr/bin/python3
"""review data"""
from models.base_model import BaseModel

class Review(BaseModel):
    """review data"""
    text = ""
    user_id = ""
    place_id = ""
